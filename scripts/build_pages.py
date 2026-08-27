#!/usr/bin/env python3
"""Build human-readable Markdown indexes from the repository CSV files."""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_rows(name: str) -> list[dict[str, str]]:
    with (ROOT / "data" / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def clean(value: str) -> str:
    return value.strip().replace("|", "\\|").replace("\n", " ")


def link(label: str, url: str) -> str:
    label = clean(label)
    return f"[{label}]({url.strip()})" if url.strip() else label


def table(headers: list[str], rows: list[list[str]]) -> str:
    rendered = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    rendered.extend("| " + " | ".join(clean(cell) for cell in row) + " |" for row in rows)
    return "\n".join(rendered)


def papers_page() -> str:
    rows = read_rows("papers.csv")
    code_labels = {
        "official": "Official",
        "author-released": "Author",
        "third-party": "Third-party",
        "not-found": "—",
    }
    records = []
    for row in rows:
        code = code_labels[row["code_status"]]
        if row["code_url"]:
            code = link(code, row["code_url"])
        records.append(
            [
                link(row["title"], row["paper_url"]),
                row["year"],
                row["venue"],
                row["intersection_context"],
                row["traffic_context"],
                row["method_family"],
                row["evidence_level"],
                code,
            ]
        )
    body = table(
        ["Paper", "Year", "Venue", "Context", "Traffic", "Method", "Evidence", "Code"],
        records,
    )
    return f"""# Research-paper index

[Back to the repository overview](../README.md)

This curated index contains the survey's **core comparison papers** with detailed D1-D3 operating assumptions and evidence fields. For every work cited by the manuscript, use the [complete citation catalog](references.md). Code links are labeled only after their relationship to the publication has been checked; **—** means no public implementation was located as of the row's `last_verified` date.

{body}

Machine-readable source: [`data/papers.csv`](../data/papers.csv). See [CONTRIBUTING.md](../CONTRIBUTING.md) before adding or changing implementation links.
"""


def datasets_page() -> str:
    rows = read_rows("datasets.csv")
    records = [
        [
            link(row["name"], row["url"]),
            row["year"],
            row["context"],
            row["data_provided"],
            row["acquisition"],
            row["participants"],
            row["scale"],
            row["tasks"],
        ]
        for row in rows
    ]
    body = table(
        ["Dataset", "Year", "Context", "Data", "Acquisition", "Participants", "Scale", "Tasks"],
        records,
    )
    return f"""# Datasets

[Back to the repository overview](../README.md) · [Evaluation guide](evaluation-resources.md)

The collection spans operational signal data, trajectories and interactions, motion-planning corpora, and cooperative perception/V2X resources. Inclusion does not imply identical licensing, geographic coverage, or fitness for every task; follow each resource's terms and documentation.

{body}

Machine-readable source: [`data/datasets.csv`](../data/datasets.csv).
"""


def benchmarks_page() -> str:
    rows = read_rows("benchmarks.csv")
    records = [
        [
            link(row["name"], row["url"]),
            row["context"],
            row["type"],
            row["scenario_scope"],
            row["evaluation_mode"],
            row["tasks"],
            row["limitation"],
        ]
        for row in rows
    ]
    body = table(
        ["Resource", "Context", "Type", "Scope", "Evaluation", "Tasks", "Limitation"],
        records,
    )
    return f"""# Benchmarks and scenario resources

[Back to the repository overview](../README.md) · [Evaluation guide](evaluation-resources.md)

`formal benchmark` identifies a resource with an explicit comparison protocol or benchmark interface. `benchmark-supporting` and `simulation-ready scenario` resources can improve reproducibility but do not, by themselves, guarantee comparable demand, seeds, metrics, or baselines.

{body}

Machine-readable source: [`data/benchmarks.csv`](../data/benchmarks.csv).
"""


def simulators_page() -> str:
    rows = read_rows("simulators.csv")
    records = [
        [
            link(row["name"], row["url"]),
            row["category"],
            row["granularity"],
            row["availability"],
            row["mixed_hdv_cav"],
            row["mpr"],
            row["v2x"],
            row["closed_loop_scope"],
            row["tasks"],
            row["limitation"],
        ]
        for row in rows
    ]
    body = table(
        ["Platform", "Category", "Granularity", "Access", "Mixed", "MPR", "V2X", "Closed loop", "Tasks", "Limitation"],
        records,
    )
    return f"""# Simulation and co-simulation platforms

[Back to the repository overview](../README.md) · [Evaluation guide](evaluation-resources.md)

Capability labels describe native or commonly supported workflows at a survey level; they are not guarantees for a particular version. **Direct** denotes an explicit capability, **partial** normally requires extensions or coupling, and **external** requires another platform.

{body}

Machine-readable source: [`data/simulators.csv`](../data/simulators.csv).
"""


REFERENCE_ROLE_LABELS = {
    "method-paper": "Method paper",
    "survey-review": "Survey/review",
    "dataset": "Dataset",
    "benchmark": "Benchmark",
    "simulator-tool": "Simulator/tool",
    "deployment-evidence": "Deployment evidence",
    "evaluation-method": "Evaluation method",
    "standard-guidance": "Standard/guidance",
    "background-foundation": "Background/foundation",
}

REFERENCE_SECTION_LABELS = {
    "signalized": "Signalized intersections",
    "non-signalized-aim": "Non-signalized intersections and AIM",
    "mixed-traffic-mpr": "Mixed traffic and MPR",
    "foundation-models": "Foundation models",
    "evaluation": "Evaluation metrics",
    "evaluation-resources": "Datasets, benchmarks, and simulation",
    "deployment": "Deployment evidence",
    "operating-context": "Operating context",
    "related-work": "Related work",
    "taxonomy": "Taxonomy",
    "review-methodology": "Review methodology",
    "introduction": "Introduction",
    "front-matter": "Front matter",
}

CODE_LABELS = {
    "official": "Official",
    "author-released": "Author",
    "third-party": "Third-party",
    "not-found": "Not found",
    "not-checked": "Not checked",
    "not-applicable": "—",
}


def reference_code_cell(row: dict[str, str]) -> str:
    label = CODE_LABELS[row["code_status"]]
    return link(label, row["code_url"]) if row["code_url"] else label


def references_table(rows: list[dict[str, str]]) -> str:
    records = [
        [
            link(row["title"], row["paper_url"]),
            row["year"],
            row["venue"],
            REFERENCE_ROLE_LABELS[row["primary_role"]],
            ", ".join(REFERENCE_SECTION_LABELS.get(value, value) for value in row["survey_sections"].split("; ")),
            reference_code_cell(row),
        ]
        for row in rows
    ]
    return table(["Reference", "Year", "Venue/source", "Role", "Survey sections", "Code"], records)


def references_overview_page() -> str:
    rows = read_rows("references.csv")
    active_keys = sum(len(row["citation_keys"].split("; ")) for row in rows)
    role_counts = Counter(row["primary_role"] for row in rows)
    role_rows = [[REFERENCE_ROLE_LABELS[role], str(role_counts[role])] for role in REFERENCE_ROLE_LABELS if role_counts[role]]
    section_pages = [
        ("Signalized intersections", "references/signalized.md", "signalized"),
        ("Non-signalized intersections and AIM", "references/non-signalized-aim.md", "non-signalized-aim"),
        ("Mixed traffic and MPR", "references/mixed-traffic-mpr.md", "mixed-traffic-mpr"),
        ("Foundation models", "references/foundation-models.md", "foundation-models"),
        ("Evaluation metrics", "references/evaluation.md", "evaluation"),
        ("Datasets, benchmarks, and simulation", "references/evaluation-resources.md", "evaluation-resources"),
        ("Deployment evidence", "references/deployment.md", "deployment"),
        ("Background, context, and reviews", "references/background-and-reviews.md", "background"),
    ]
    navigation = []
    for label, path, section in section_pages:
        if section == "background":
            count = sum(row["primary_section"] not in {"signalized", "non-signalized-aim", "mixed-traffic-mpr", "foundation-models", "evaluation", "evaluation-resources", "deployment"} for row in rows)
        else:
            count = sum(section in row["survey_sections"].split("; ") for row in rows)
        navigation.append([link(label, path), str(count)])
    direct = sum(row["link_type"] != "scholar-search" for row in rows)
    return f"""# Complete citation catalog

[Back to the repository overview](../README.md) · [Core comparison papers](papers.md)

This catalog contains all **{len(rows)} distinct works** represented by the current survey manuscript's **{active_keys} active citation keys**. Citation aliases that point to the same work are consolidated in one row and retained in `citation_keys`. Every title links to a DOI, publisher, official standard/report, institutional repository, or project page. The smaller core-paper index remains a curated subset with detailed D1-D3 method and evidence fields.

## Browse by survey topic

{table(["Topic page", "Cited references"], navigation)}

References may appear on more than one topic page when the manuscript cites them in multiple sections.

## Primary-role coverage

{table(["Primary role", "References"], role_rows)}

## Link and code status

- **{direct}/{len(rows)} work links** are direct links; no generic search-result fallbacks are used.
- **{sum(row['core_paper'] == 'yes' for row in rows)} core papers** retain manually verified implementation status.
- `Not checked` means implementation discovery has not yet been completed for that non-core paper; it is not a claim that code is unavailable.

Machine-readable source: [`data/references.csv`](../data/references.csv).
"""


def references_section_page(title: str, section: str, intro: str) -> str:
    rows = read_rows("references.csv")
    if section == "background":
        specialist = {"signalized", "non-signalized-aim", "mixed-traffic-mpr", "foundation-models", "evaluation", "evaluation-resources", "deployment"}
        selected = [row for row in rows if row["primary_section"] not in specialist]
    else:
        selected = [row for row in rows if section in row["survey_sections"].split("; ")]
    return f"""# {title}

[Complete citation catalog](../references.md) · [Repository overview](../../README.md)

{intro} This page contains **{len(selected)}** distinct cited works; titles link to the paper or primary source.

{references_table(selected)}

Machine-readable source: [`data/references.csv`](../../data/references.csv).
"""


OUTPUTS = {
    ROOT / "docs" / "papers.md": papers_page,
    ROOT / "docs" / "datasets.md": datasets_page,
    ROOT / "docs" / "benchmarks.md": benchmarks_page,
    ROOT / "docs" / "simulators.md": simulators_page,
    ROOT / "docs" / "references.md": references_overview_page,
    ROOT / "docs" / "references" / "signalized.md": lambda: references_section_page("Signalized-intersection references", "signalized", "Citations used in the signalized planning and control section."),
    ROOT / "docs" / "references" / "non-signalized-aim.md": lambda: references_section_page("Non-signalized and AIM references", "non-signalized-aim", "Citations used in the non-signalized and autonomous-intersection-management section."),
    ROOT / "docs" / "references" / "mixed-traffic-mpr.md": lambda: references_section_page("Mixed-traffic and MPR references", "mixed-traffic-mpr", "Citations used in the cross-cutting mixed-traffic and market-penetration section."),
    ROOT / "docs" / "references" / "foundation-models.md": lambda: references_section_page("Foundation-model references", "foundation-models", "Citations used in the foundation-model-assisted intelligent-intersections section."),
    ROOT / "docs" / "references" / "evaluation.md": lambda: references_section_page("Evaluation-metric references", "evaluation", "Citations supporting the evaluation metrics, constraints, and reporting guidance."),
    ROOT / "docs" / "references" / "evaluation-resources.md": lambda: references_section_page("Dataset, benchmark, and simulation references", "evaluation-resources", "Citations used in the datasets, benchmarks, simulation, and co-simulation section."),
    ROOT / "docs" / "references" / "deployment.md": lambda: references_section_page("Deployment-evidence references", "deployment", "Citations used in the field evidence, architecture, program, and readiness section."),
    ROOT / "docs" / "references" / "background-and-reviews.md": lambda: references_section_page("Background, context, and review references", "background", "References whose primary use is the introduction, taxonomy, related work, methodology, or operating-context discussion."),
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated pages are stale")
    args = parser.parse_args()
    stale: list[Path] = []
    for path, builder in OUTPUTS.items():
        expected = builder()
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != expected:
                stale.append(path.relative_to(ROOT))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8")
            print(f"wrote {path.relative_to(ROOT)}")
    if stale:
        print("Generated pages are stale:", file=sys.stderr)
        for path in stale:
            print(f"  {path}", file=sys.stderr)
        print("Run: python scripts/build_pages.py", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
