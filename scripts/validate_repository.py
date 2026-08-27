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
    "papers.csv": ["id", "title", "year", "venue", "intersection_context", "traffic_context", "method_family", "coordination_architecture", "evidence_level", "paper_url", "code_url", "code_status", "bibtex_key", "last_verified"],
    "datasets.csv": ["id", "name", "year", "context", "data_provided", "acquisition", "participants", "scale", "tasks", "url", "bibtex_key", "last_verified"],
    "benchmarks.csv": ["id", "name", "context", "type", "scenario_scope", "evaluation_mode", "tasks", "limitation", "url", "bibtex_key", "last_verified"],
    "simulators.csv": ["id", "name", "category", "granularity", "availability", "mixed_hdv_cav", "mpr", "v2x", "closed_loop_scope", "tasks", "limitation", "url", "bibtex_key", "last_verified"],
    "deployment.csv": ["id", "name", "kind", "control_authority", "highest_evidence", "scope", "main_gap", "url", "bibtex_keys", "last_verified"],
}

CONTROLLED = {
    ("papers.csv", "intersection_context"): {"signalized", "non-signalized", "both"},
    ("papers.csv", "coordination_architecture"): {"centralized", "decentralized", "hierarchical", "not-applicable"},
    ("papers.csv", "code_status"): {"official", "author-released", "third-party", "not-found"},
}

EXPECTED_BADGES = {"papers.csv": "papers", "datasets.csv": "datasets", "benchmarks.csv": "benchmarks", "simulators.csv": "simulators"}
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
            row_id = row.get("id", "").strip()
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
                has_code = bool(row["code_url"].strip())
                if (row["code_status"] == "not-found") == has_code:
                    errors.append(f"{filename}:{line}: code_url and code_status disagree")
    return counts


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
