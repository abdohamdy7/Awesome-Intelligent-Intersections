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

| Record | Kind | Control authority | Highest evidence | Main remaining gap |
|---|---|---|---|---|
| Adaptive traffic signal control | Architecture | Traffic signals | E3 | Cross-site transfer, detector robustness, and lifecycle benefits |
| Signalized control with CV/CAV assistance | Architecture | Signals plus advisory/cooperation | E2 | Larger mixed fleets, degraded V2X, and end-to-end safety |
| Centralized reservation AIM | Architecture | Infrastructure manager plus equipped vehicles | E2 | Dense mixed traffic, VRUs, failures, and public-road integration |
| Decentralized or cooperative AIM | Architecture | Vehicle agents and/or roadside coordination | E2 | Compliance, interoperability, communications, and institutional authority |
| USDOT Connected Vehicle Pilots | Program | Cooperative applications and infrastructure | E3 | Transferable control-level outcome evidence |
| Compass4D / C-Roads | Program | Cooperative ITS services | E3 | Harmonized end-to-end benefit and safety reporting |
| SIP-adus | Program | Automated-driving and infrastructure cooperation | E3 | Generalization beyond deployment corridors and configurations |
| Wuxi C-V2X | Program | Large-scale connected-vehicle services | E3 | Public control-performance and reproducibility detail |

The structured records are in [`data/deployment.csv`](../data/deployment.csv). Program deployment is contextual evidence; it should not be cited as validation of a specific controller unless that controller and its measured outcomes were directly evaluated.
