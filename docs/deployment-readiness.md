# Deployment readiness

[Back to the repository overview](../README.md)

High simulation performance does not establish deployment readiness. The survey uses an evidence ladder that records the highest demonstrated environment while preserving the operating assumptions and remaining gaps.

## Evidence ladder

| Level | Environment | Minimum interpretation |
|---|---|---|
| **E0** | Analytical, optimization instance, or offline/recorded-data study | Concept, estimation, or replay evidence; no closed-loop operational response |
| **E1** | Closed-loop simulation or co-simulation | Controller and environment interact; fidelity and scenario coverage remain model-dependent |
| **E2** | Hardware-in-the-loop, proving ground, test track, or public-road field operational test | Physical interfaces or real traffic are present, usually at limited scale and duration |
| **E3** | Sustained or multi-site operation | Repeated operational evidence with maintenance, monitoring, institutional, and lifecycle considerations |

## Architectures and programs

| Linked record/evidence | Kind | Control authority | Highest evidence | Main remaining gap |
|---|---|---|---|---|
| [Adaptive signal control — RHODES field test](https://rosap.ntl.bts.gov/view/dot/14932) | Architecture | Traffic signals | E3 | Cross-site transfer, detector robustness, and lifecycle benefits |
| [Signalized CV/CAV assistance — GLOSA road test](https://doi.org/10.4271/2020-01-1379) | Architecture | Signals plus advisory/cooperation | E2 | Larger mixed fleets, degraded V2X, and end-to-end safety |
| [Centralized cooperative intersection management](https://doi.org/10.1109/MITS.2025.3643199) | Architecture | Infrastructure manager plus equipped vehicles | E2 | Dense mixed traffic, VRUs, failures, and public-road integration |
| [Distributed cooperative CAV control](https://doi.org/10.1109/TITS.2022.3162038) | Architecture | Vehicle agents and/or roadside coordination | E2 | Compliance, interoperability, communications, and institutional authority |
| [USDOT Connected Vehicle Pilots](https://www.its.dot.gov/pilots/) | Program | Cooperative applications and infrastructure | E3 | Transferable control-level outcome evidence |
| [Compass4D / C-Roads](https://www.c-roads.eu/) | Program | Cooperative ITS services | E3 | Harmonized end-to-end benefit and safety reporting |
| [SIP-adus Tokyo Waterfront](https://www.sip-adus.go.jp/) | Program | Automated-driving and infrastructure cooperation | E3 | Generalization beyond deployment corridors and configurations |
| [Wuxi C-V2X field evidence](https://doi.org/10.1109/JIOT.2020.2974823) | Program | Large-scale connected-vehicle services | E3 | Public control-performance and reproducibility detail |

The structured records are in [`data/deployment.csv`](../data/deployment.csv), and every manuscript citation used in this section is listed on the [deployment reference page](references/deployment.md). Program deployment is contextual evidence; it should not be cited as validation of a specific controller unless that controller and its measured outcomes were directly evaluated.
