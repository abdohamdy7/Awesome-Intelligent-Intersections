# Data schema

The CSV files are the source of truth for the generated collection pages. Use UTF-8, one record per row, stable kebab-case IDs, and ISO `YYYY-MM-DD` verification dates.

| File | Purpose | Generated page |
|---|---|---|
| `papers.csv` | Representative research papers and implementation status | [`docs/papers.md`](../docs/papers.md) |
| `datasets.csv` | Operational, trajectory, planning, and V2X datasets | [`docs/datasets.md`](../docs/datasets.md) |
| `benchmarks.csv` | Formal benchmarks and scenario resources | [`docs/benchmarks.md`](../docs/benchmarks.md) |
| `simulators.csv` | Traffic, autonomy, communications, and co-simulation platforms | [`docs/simulators.md`](../docs/simulators.md) |
| `deployment.csv` | Control architectures and deployment programs | [`docs/deployment-readiness.md`](../docs/deployment-readiness.md) |

## Paper code status

- `official`: the repository identifies itself as the official implementation or is linked by the publication/project.
- `author-released`: maintained by an author or author organization, without an explicit official claim.
- `third-party`: independent reproduction; label it clearly.
- `not-found`: no public implementation was located on the verification date.

Never infer an implementation link from title similarity alone. See [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the verification checklist.
