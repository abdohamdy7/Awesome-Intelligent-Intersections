# Awesome Intelligent Intersections

<p align="center">
  <a href="docs/papers.md"><img alt="Papers" src="https://img.shields.io/badge/papers-46-22577A"></a>
  <a href="docs/datasets.md"><img alt="Datasets" src="https://img.shields.io/badge/datasets-44-2A9D8F"></a>
  <a href="docs/benchmarks.md"><img alt="Benchmarks" src="https://img.shields.io/badge/benchmarks-13-E9C46A"></a>
  <a href="docs/simulators.md"><img alt="Simulators" src="https://img.shields.io/badge/simulators-19-F4A261"></a>
  <img alt="Paper status" src="https://img.shields.io/badge/survey-manuscript%20in%20preparation-6C63FF">
</p>

A taxonomy-driven collection of research, implementations, datasets, benchmarks, simulation platforms, and deployment evidence for **ITS-enabled intelligent-intersection planning and control**.

This repository accompanies the survey:

> **From Challenges to Deployment: A Survey on Intelligent Intersection Planning and Control With Connected Autonomous Vehicles and Mixed Traffic**  
> Abdulrahman Ahmad, Ameena S. Al-Sumaiti, Sumbal Malik, Young Ji Byon, Khalifa Al Hosani, and Majid Khonji.  
> *Manuscript in preparation.*

The collection covers signalized, non-signalized, hybrid signal-CAV, and signal-free autonomous intersection management (AIM), with explicit attention to mixed traffic, CV/CAV market penetration rate (MPR), vulnerable road users (VRUs), V2X assumptions, evaluation evidence, and deployment readiness.

<p align="center">
  <img src="assets/figures/taxonomy.png" alt="Taxonomy of ITS-enabled intelligent-intersection planning and control" width="100%">
</p>

## Explore the collection

| Topic | What it contains |
|---|---|
| [Research-paper index](docs/papers.md) | Paper, venue, operating context, traffic composition, method family, evidence level, and verified code status |
| [Signalized intersections](docs/signalized-intersections.md) | Signal timing, estimation, signal-trajectory coordination, learning, multimodal and priority-aware control |
| [Non-signalized intersections and AIM](docs/non-signalized-and-aim.md) | Gap acceptance, reservation AIM, distributed control, mixed traffic, negotiation, learning |
| [Mixed traffic and MPR](docs/mixed-traffic-and-mpr.md) | Capability-based interpretation of penetration, observability, controllability, and reporting requirements |
| [Foundation-model assistance](docs/foundation-models.md) | LLM, VLM, MLLM, and VLA roles, authority boundaries, verification, and fallback |
| [Datasets](docs/datasets.md) | Intersection context, data modalities, acquisition, participants, scale, and supported tasks |
| [Benchmarks](docs/benchmarks.md) | Formal benchmarks, benchmark-ready resources, and simulation-ready scenarios |
| [Simulation and co-simulation](docs/simulators.md) | Traffic, autonomy, V2X, and multidomain platforms with capabilities and limitations |
| [Deployment readiness](docs/deployment-readiness.md) | E0-E3 validation environments, deployed architectures, programs, and remaining evidence gaps |

## Taxonomy

Every included study can be described across three coupled dimensions instead of being placed in only one topic bucket:

| Dimension | Questions captured |
|---|---|
| **D1 - Operating context and assumptions** | Intersection type, traffic composition, MPR, sensing, V2X, infrastructure, and control authority |
| **D2 - Planning and control methods** | Rule-based/traffic-engineering, optimization, learning, cooperative V2X, foundation-model assistance, and coordination architecture |
| **D3 - Evaluation and deployment** | Metrics, datasets, simulators, validation environment, field evidence, and readiness factors |

This representation prevents a full-CAV simulation result from being interpreted as evidence for low-penetration mixed traffic or public-road deployment.

## Implementation-aware paper records

Code links are checked against the paper, author, laboratory, or project repository. A dash means that no public implementation was located as of the record's `last_verified` date; it does **not** prove that code does not exist.

| Paper | Context | Method | Code |
|---|---|---|---|
| [PressLight](https://doi.org/10.1145/3292500.3330949) | Signalized | Learning | [Official](https://github.com/wingsweihua/presslight) |
| [CoLight](https://doi.org/10.1145/3357384.3357902) | Signalized network | Learning | [Official](https://github.com/wingsweihua/colight) |
| [LLMLight](https://doi.org/10.1145/3690624.3709379) | Signalized | Foundation-model-assisted | [Official](https://github.com/usail-hkust/LLMTSCS) |
| [CoLLMLight](https://openreview.net/forum?id=KeJqoEVOeY) | Signalized network | Foundation-model-assisted | [Official](https://github.com/usail-hkust/CoLLMLight) |
| [PromptGAT](https://doi.org/10.1609/aaai.v38i1.27758) | Signalized | Foundation-model-assisted transfer | [Official](https://github.com/DaRL-LibSignal/PromptGAT) |
| [TrafficGPT](https://doi.org/10.1016/j.tranpol.2024.03.006) | Cross-cutting | Tool orchestration | [Official](https://github.com/lijlansg/TrafficGPT) |

See the [complete paper index](docs/papers.md) for all seeded records.

## Resource snapshot

The first repository release is seeded directly from the survey's active comparison tables:

- **46** representative research papers across signalized, non-signalized/AIM, mixed-traffic, and foundation-model-assisted methods;
- **44** operational, trajectory, interaction, motion-planning, and cooperative-perception datasets;
- **13** formal benchmarks and benchmark-supporting scenario resources;
- **19** traffic, automated-driving, V2X, and multidomain simulation platforms;
- **8** control-architecture and program-level deployment records.

The machine-readable source files are in [`data/`](data/). Generated resource pages can be rebuilt with:

```bash
python scripts/build_pages.py
python scripts/validate_repository.py
```

## Scope rules

Included resources must directly support intersection-level planning, control, coordination, evaluation, or deployment. Freeway automation, parking, generic smart-city mobility, and full-stack automated-driving resources are included only when they contribute direct intersection-level evidence or reusable evaluation support.

Foundation-model work is tagged as:

- **Direct** - generates or coordinates candidate intersection-control actions;
- **Enabling** - supports understanding, adaptation, tool use, simulation, or operator interaction;
- **Adjacent** - relevant autonomous-driving evidence without direct validation as an intersection-management system.

## Contributing

Community additions and corrections are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and use the structured issue forms. New entries should provide a stable paper/resource link, taxonomy tags, and an implementation link only when its relationship to the publication can be verified.

## Citation

The survey citation will be updated after a preprint or DOI becomes available. Until then, cite this repository using [`CITATION.cff`](CITATION.cff) and describe the survey as a manuscript in preparation.

## License

A public-use license has not yet been assigned. The authors should select a license before the public release; third-party papers, software, datasets, and trademarks remain subject to their respective licenses and terms.
