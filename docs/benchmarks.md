# Benchmarks and scenario resources

[Back to the repository overview](../README.md) · [Evaluation guide](evaluation-resources.md)

`formal benchmark` identifies a resource with an explicit comparison protocol or benchmark interface. `benchmark-supporting` and `simulation-ready scenario` resources can improve reproducibility but do not, by themselves, guarantee comparable demand, seeds, metrics, or baselines.

| Resource | Paper/source | Project | Code | Context | Type | Scope | Evaluation | Tasks | Limitation |
|---|---|---|---|---|---|---|---|---|---|
| CityFlow scenarios | [Paper/source](https://doi.org/10.1145/3308558.3314139) | [Project](https://github.com/cityflow-project/CityFlow) | [Official/project](https://github.com/cityflow-project/CityFlow) | signalized | simulation-ready scenario | varied | closed-loop capable | traffic optimization | No fixed cross-study protocol |
| LibSignal | [Paper/source](https://doi.org/10.1007/s10994-023-06412-y) | [Project](https://github.com/DaRL-LibSignal/LibSignal) | [Official/project](https://github.com/DaRL-LibSignal/LibSignal) | signalized | formal benchmark | varied | closed-loop | traffic optimization | Simulator- and scenario-dependent |
| RESCO | [Paper/source](https://openreview.net/forum?id=LqRSh6V0vR) | [Project](https://github.com/Pi-Star-Lab/RESCO) | [Official/project](https://github.com/Pi-Star-Lab/RESCO) | signalized | formal benchmark | varied | closed-loop | traffic optimization | Limited V2X and VRU realism |
| MixedTrafficPlus | [Paper/source](https://doi.org/10.1109/ICRA55743.2025.11127732) | — | [Official/project](https://github.com/xiaochy/MixedTrafficPlus) | non-signalized | formal benchmark | varied | closed-loop | traffic optimization; motion planning; safety assessment | Simulation-only evaluation |
| OpenCDA-MARL | [Paper/source](https://doi.org/10.1109/LRA.2026.3664656) | [Project](https://github.com/radar-lab/OpenCDA-MARL) | [Official/project](https://github.com/radar-lab/OpenCDA-MARL) | non-signalized | formal benchmark | single | closed-loop | V2X cooperation; motion planning; safety assessment | Limited field validation |
| V2Xverse | [Paper/source](https://doi.org/10.1109/TPAMI.2025.3560327) | [Project](https://github.com/CollaborativePerception/V2Xverse) | [Official/project](https://github.com/CollaborativePerception/V2Xverse) | non-signalized | formal benchmark | varied | open- and closed-loop | V2X cooperation; motion planning; perception | CARLA-dependent realism |
| MDrive | [Paper/source](https://doi.org/10.48550/arXiv.2605.10904) | [Project](https://arxiv.org/abs/2605.10904) | [Official/project](https://github.com/ucla-mobility/MDrive) | non-signalized | formal benchmark | varied | closed-loop | V2X cooperation; motion planning; safety assessment | Limited external validation |
| Five-city traffic-control data | [Paper/source](https://doi.org/10.1038/s41597-026-06892-2) | — | — | signalized | benchmark-ready resource | network | not fixed | traffic optimization | No fixed benchmark protocol |
| InTAS | [Paper/source](https://doi.org/10.52825/scp.v1i.102) | — | [Author-released](https://github.com/silaslobo/InTAS) | both | simulation-ready scenario | network | closed-loop capable | traffic optimization; V2X cooperation | No fixed benchmark protocol |
| TAPAS Cologne | [Paper/source](https://sumo.dlr.de/docs/Data/Scenarios/TAPASCologne.html) | — | — | both | simulation-ready scenario | network | closed-loop capable | traffic optimization | Network and demand quality caveats |
| LuST | [Paper/source](https://doi.org/10.1109/VNC.2015.7385539) | [Project](https://github.com/lcodeca/LuSTScenario) | [Official/project](https://github.com/lcodeca/LuSTScenario) | both | simulation-ready scenario | network | closed-loop capable | traffic optimization; V2X cooperation | Version-sensitive validation |
| MoST | [Paper/source](https://doi.org/10.1109/VNC.2017.8275627) | [Project](https://github.com/lcodeca/MoSTScenario) | [Official/project](https://github.com/lcodeca/MoSTScenario) | both | simulation-ready scenario | network | closed-loop capable | traffic optimization; V2X cooperation | No fixed control protocol |
| CommonRoad | [Paper/source](https://doi.org/10.1109/IVS.2017.7995802) | [Project](https://commonroad.in.tum.de/) | [Official/project](https://github.com/CommonRoad/commonroad-io) | both | formal benchmark | varied | open- and closed-loop capable | motion planning; safety assessment | Not intersection-control specific |

Machine-readable source: [`data/benchmarks.csv`](../data/benchmarks.csv).
