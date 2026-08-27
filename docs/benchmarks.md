# Benchmarks and scenario resources

[Back to the repository overview](../README.md) · [Evaluation guide](evaluation-resources.md)

`formal benchmark` identifies a resource with an explicit comparison protocol or benchmark interface. `benchmark-supporting` and `simulation-ready scenario` resources can improve reproducibility but do not, by themselves, guarantee comparable demand, seeds, metrics, or baselines.

| Resource | Context | Type | Scope | Evaluation | Tasks | Limitation |
|---|---|---|---|---|---|---|
| [CityFlow scenarios](https://github.com/cityflow-project/CityFlow) | signalized | simulation-ready scenario | varied | closed-loop capable | traffic optimization | No fixed cross-study protocol |
| [LibSignal](https://github.com/DaRL-LibSignal/LibSignal) | signalized | formal benchmark | varied | closed-loop | traffic optimization | Simulator- and scenario-dependent |
| [RESCO](https://github.com/Pi-Star-Lab/RESCO) | signalized | formal benchmark | varied | closed-loop | traffic optimization | Limited V2X and VRU realism |
| [MixedTrafficPlus](https://doi.org/10.1109/ICRA55743.2025.11127732) | non-signalized | formal benchmark | varied | closed-loop | traffic optimization; motion planning; safety assessment | Simulation-only evaluation |
| [OpenCDA-MARL](https://github.com/radar-lab/OpenCDA-MARL) | non-signalized | formal benchmark | single | closed-loop | V2X cooperation; motion planning; safety assessment | Limited field validation |
| [V2Xverse](https://github.com/CollaborativePerception/V2Xverse) | non-signalized | formal benchmark | varied | open- and closed-loop | V2X cooperation; motion planning; perception | CARLA-dependent realism |
| [MDrive](https://arxiv.org/abs/2605.10904) | non-signalized | formal benchmark | varied | closed-loop | V2X cooperation; motion planning; safety assessment | Limited external validation |
| [Five-city traffic-control data](https://doi.org/10.1038/s41597-026-06892-2) | signalized | benchmark-ready resource | network | not fixed | traffic optimization | No fixed benchmark protocol |
| [InTAS](https://doi.org/10.52825/scp.v1i.102) | both | simulation-ready scenario | network | closed-loop capable | traffic optimization; V2X cooperation | No fixed benchmark protocol |
| [TAPAS Cologne](https://sumo.dlr.de/docs/Data/Scenarios/TAPASCologne.html) | both | simulation-ready scenario | network | closed-loop capable | traffic optimization | Network and demand quality caveats |
| [LuST](https://github.com/lcodeca/LuSTScenario) | both | simulation-ready scenario | network | closed-loop capable | traffic optimization; V2X cooperation | Version-sensitive validation |
| [MoST](https://github.com/lcodeca/MoSTScenario) | both | simulation-ready scenario | network | closed-loop capable | traffic optimization; V2X cooperation | No fixed control protocol |
| [CommonRoad](https://commonroad.in.tum.de/) | both | formal benchmark | varied | open- and closed-loop capable | motion planning; safety assessment | Not intersection-control specific |

Machine-readable source: [`data/benchmarks.csv`](../data/benchmarks.csv).
