#!/usr/bin/env python3
"""Build human-readable Markdown indexes from the repository CSV files."""

from __future__ import annotations

import argparse
import csv
import sys
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

This index is seeded from the survey's active comparison tables. Taxonomy fields preserve operating assumptions and evidence level. Code links are labeled only after their relationship to the publication has been checked; **—** means no public implementation was located as of the row's `last_verified` date.

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


OUTPUTS = {
    ROOT / "docs" / "papers.md": papers_page,
    ROOT / "docs" / "datasets.md": datasets_page,
    ROOT / "docs" / "benchmarks.md": benchmarks_page,
    ROOT / "docs" / "simulators.md": simulators_page,
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
