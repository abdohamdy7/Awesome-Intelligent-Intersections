#!/usr/bin/env python3
"""Validate schemas, controlled fields, counts, URLs, and local Markdown links."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]

SCHEMAS = {
    "references.csv": ["citation_order", "bibtex_key", "citation_keys", "title", "year", "authors", "venue", "publication_type", "primary_role", "primary_section", "survey_sections", "paper_url", "link_type", "core_paper", "code_url", "code_status", "last_verified"],
    "papers.csv": ["id", "title", "year", "venue", "intersection_context", "traffic_context", "method_family", "coordination_architecture", "evidence_level", "paper_url", "code_url", "code_status", "bibtex_key", "last_verified"],
    "datasets.csv": ["id", "name", "year", "context", "data_provided", "acquisition", "participants", "scale", "tasks", "url", "bibtex_key", "last_verified"],
    "benchmarks.csv": ["id", "name", "context", "type", "scenario_scope", "evaluation_mode", "tasks", "limitation", "url", "bibtex_key", "last_verified"],
    "simulators.csv": ["id", "name", "category", "granularity", "availability", "mixed_hdv_cav", "mpr", "v2x", "closed_loop_scope", "tasks", "limitation", "url", "bibtex_key", "last_verified"],
    "deployment.csv": ["id", "name", "kind", "control_authority", "highest_evidence", "scope", "main_gap", "url", "bibtex_keys", "last_verified"],
}

CONTROLLED = {
    ("references.csv", "primary_role"): {"method-paper", "survey-review", "dataset", "benchmark", "simulator-tool", "deployment-evidence", "evaluation-method", "standard-guidance", "background-foundation"},
    ("references.csv", "core_paper"): {"yes", "no"},
    ("references.csv", "code_status"): {"official", "author-released", "third-party", "not-found", "not-checked", "not-applicable"},
    ("papers.csv", "intersection_context"): {"signalized", "non-signalized", "both"},
    ("papers.csv", "coordination_architecture"): {"centralized", "decentralized", "hierarchical", "not-applicable"},
    ("papers.csv", "code_status"): {"official", "author-released", "third-party", "not-found"},
}

EXPECTED_BADGES = {"references.csv": "cited_works", "papers.csv": "core_papers", "datasets.csv": "datasets", "benchmarks.csv": "benchmarks", "simulators.csv": "simulators"}
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def valid_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate_csvs(errors: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for filename, schema in SCHEMAS.items():
        path = ROOT / "data" / filename
        with path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != schema:
                errors.append(f"{path.relative_to(ROOT)}: header does not match documented schema")
            rows = list(reader)
        counts[filename] = len(rows)
        ids: set[str] = set()
        for line, row in enumerate(rows, start=2):
            row_id = row.get("id", row.get("bibtex_key", "")).strip()
            if not row_id:
                errors.append(f"{filename}:{line}: id is required")
            elif row_id in ids:
                errors.append(f"{filename}:{line}: duplicate id {row_id!r}")
            ids.add(row_id)
            for field, value in row.items():
                if field.endswith("url") and value.strip() and not valid_url(value.strip()):
                    errors.append(f"{filename}:{line}: invalid {field}: {value!r}")
            for (controlled_file, field), allowed in CONTROLLED.items():
                if filename == controlled_file and row.get(field, "") not in allowed:
                    errors.append(f"{filename}:{line}: invalid {field}: {row.get(field)!r}")
            if filename == "papers.csv":
                if not row["paper_url"].strip():
                    errors.append(f"{filename}:{line}: paper_url is required")
                has_code = bool(row["code_url"].strip())
                if (row["code_status"] == "not-found") == has_code:
                    errors.append(f"{filename}:{line}: code_url and code_status disagree")
            if filename == "references.csv":
                if not row["paper_url"].strip():
                    errors.append(f"{filename}:{line}: paper_url is required")
                if row["link_type"] == "scholar-search":
                    errors.append(f"{filename}:{line}: generic search fallback is not permitted")
                has_code = bool(row["code_url"].strip())
                code_expected = row["code_status"] in {"official", "author-released", "third-party"}
                if has_code != code_expected:
                    errors.append(f"{filename}:{line}: code_url and code_status disagree")
                if not row["survey_sections"].strip():
                    errors.append(f"{filename}:{line}: survey_sections is required")
                if not row["citation_keys"].strip():
                    errors.append(f"{filename}:{line}: citation_keys is required")
        if filename == "references.csv":
            orders = [int(row["citation_order"]) for row in rows if row["citation_order"].isdigit()]
            if orders != list(range(1, len(rows) + 1)):
                errors.append("references.csv: citation_order must be consecutive from 1")
    return counts


def validate_reference_coverage(errors: list[str]) -> None:
    with (ROOT / "data" / "references.csv").open(encoding="utf-8", newline="") as handle:
        references = list(csv.DictReader(handle))
    with (ROOT / "data" / "papers.csv").open(encoding="utf-8", newline="") as handle:
        papers = list(csv.DictReader(handle))
    reference_core = {row["bibtex_key"].lower() for row in references if row["core_paper"] == "yes"}
    paper_keys = {row["bibtex_key"].lower() for row in papers}
    if reference_core != paper_keys:
        missing = sorted(paper_keys - reference_core)
        extra = sorted(reference_core - paper_keys)
        errors.append(f"references.csv: core-paper mapping differs from papers.csv (missing={missing}, extra={extra})")


def validate_badges(counts: dict[str, int], errors: list[str]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for filename, label in EXPECTED_BADGES.items():
        expected = counts[filename]
        match = re.search(rf"badge/{re.escape(label)}-(\d+)-", readme)
        if not match or int(match.group(1)) != expected:
            errors.append(f"README.md: {label} badge should report {expected}")


def validate_markdown_links(errors: list[str]) -> None:
    for path in [ROOT / "README.md", ROOT / "CONTRIBUTING.md", *sorted((ROOT / "docs").glob("*.md"))]:
        if not path.exists():
            errors.append(f"missing required Markdown file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative = unquote(target.split("#", 1)[0])
            resolved = (path.parent / relative).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: local link escapes repository: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link: {target}")


def main() -> int:
    errors: list[str] = []
    counts = validate_csvs(errors)
    validate_reference_coverage(errors)
    validate_badges(counts, errors)
    validate_markdown_links(errors)
    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    summary = ", ".join(f"{name.removesuffix('.csv')}={count}" for name, count in counts.items())
    print(f"Validation passed ({summary})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
