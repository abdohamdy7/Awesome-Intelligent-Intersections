# Data schema

The CSV files are the source of truth for the generated collection pages. Use UTF-8, one record per row, stable kebab-case IDs, and ISO `YYYY-MM-DD` verification dates.

| File | Purpose | Generated page |
|---|---|---|
| `references.csv` | Every distinct work actively cited by the current manuscript, retaining all citation-key aliases plus category, section tags, source link, and code status | [`docs/references.md`](../docs/references.md) and [`docs/code.md`](../docs/code.md) |
| `papers.csv` | Core comparison papers with detailed taxonomy and verified implementation status | [`docs/papers.md`](../docs/papers.md) |
| `datasets.csv` | Operational, trajectory, planning, and V2X datasets | [`docs/datasets.md`](../docs/datasets.md) |
| `benchmarks.csv` | Formal benchmarks and scenario resources | [`docs/benchmarks.md`](../docs/benchmarks.md) |
| `simulators.csv` | Traffic, autonomy, communications, and co-simulation platforms | [`docs/simulators.md`](../docs/simulators.md) |
| `deployment.csv` | Control architectures and deployment programs | [`docs/deployment-readiness.md`](../docs/deployment-readiness.md) |

## Paper code status

- `official`: the repository identifies itself as the official implementation or is linked by the publication/project.
- `author-released`: maintained by an author or author organization, without an explicit official claim.
- `third-party`: independent reproduction; label it clearly.
- `not-found`: no public implementation was located on the verification date.
- `not-checked`: implementation discovery has not yet been completed.
- `not-applicable`: code discovery is not meaningful for this source type, or no executable artifact is expected.

Never infer an implementation link from title similarity alone. See [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the verification checklist.

## Complete-catalog roles

`references.csv` assigns one primary role while retaining every survey section in which the work is cited:

| Role | Meaning |
|---|---|
| `method-paper` | Planning, control, prediction, interaction, or other technical method |
| `survey-review` | Survey, review, systematic review, or review-of-reviews |
| `dataset` | Dataset, data portal, or dataset-introduction publication |
| `benchmark` | Formal benchmark or benchmark-supporting scenario resource |
| `simulator-tool` | Simulator, co-simulator, modeling framework, or evaluation tool |
| `deployment-evidence` | Field test, operational program, or deployment assessment |
| `evaluation-method` | Metric, surrogate-safety, emissions, or validation method |
| `standard-guidance` | Standard, specification, handbook, or official guidance |
| `background-foundation` | General theoretical, contextual, or methodological foundation |

`citation_keys` retains all active LaTeX keys associated with the work. This allows duplicate BibTeX records to be consolidated without losing traceability to the manuscript.
