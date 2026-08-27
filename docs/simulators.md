# Simulation and co-simulation platforms

[Back to the repository overview](../README.md) · [Evaluation guide](evaluation-resources.md)

Capability labels describe native or commonly supported workflows at a survey level; they are not guarantees for a particular version. **Direct** denotes an explicit capability, **partial** normally requires extensions or coupling, and **external** requires another platform.

| Platform | Category | Granularity | Access | Mixed | MPR | V2X | Closed loop | Tasks | Limitation |
|---|---|---|---|---|---|---|---|---|---|
| [SUMO](https://eclipse.dev/sumo/) | traffic and signal | microscopic | open | direct | direct | partial | traffic/control | traffic optimization; motion planning; safety assessment; interaction analysis | No native perception detailed vehicle dynamics or packet-level V2X |
| [PTV Vissim/Viswalk](https://www.ptvgroup.com/en/products/ptv-vissim) | traffic and signal | microscopic | commercial | partial | direct | partial | traffic/control | traffic optimization; safety assessment; interaction analysis | CAV behavior and V2X require custom or external models |
| [Aimsun Next](https://www.aimsun.com/aimsun-next/) | traffic and signal | multiresolution | commercial/academic | partial | direct | partial | traffic/control | traffic optimization; safety assessment; interaction analysis | Perception detailed dynamics and V2X require coupling |
| [CityFlow](https://github.com/cityflow-project/CityFlow) | traffic and signal | microscopic | open | partial | partial | no | traffic/control | traffic optimization | Abstract road-user behavior with no native sensing or V2X |
| [CAVSim](https://github.com/RadetzkyLi/CAVSim) | traffic and signal | microscopic | open | partial | partial | partial | vehicle/agent | traffic optimization; V2X cooperation; motion planning; safety assessment; interaction analysis | CAV-centric with limited HDV/VRU and communication fidelity |
| [CARLA](https://carla.org/) | automated driving | vehicle/agent | open | partial | partial | partial | vehicle/agent | motion planning; safety assessment; perception; interaction analysis | Limited traffic-engineering fidelity and no packet-level V2X |
| [MetaDrive](https://metadriverse.github.io/metadrive/) | automated driving | vehicle/agent | open | partial | partial | no | vehicle/agent | motion planning; safety assessment; perception; interaction analysis | Limited traffic-engineering and V2X fidelity |
| [SMARTS 2.0](https://github.com/huawei-noah/SMARTS) | automated driving | vehicle/agent | open | partial | partial | partial | vehicle/agent | V2X cooperation; motion planning; safety assessment; perception; interaction analysis | Traffic demand and packet-level V2X require external models |
| [Waymax](https://github.com/waymo-research/waymax) | automated driving | vehicle/agent | non-commercial | partial | no | no | vehicle/agent | motion planning; safety assessment; interaction analysis | No raw sensing explicit MPR modeling or operational V2X |
| [CarSim](https://www.carsim.com/) | automated driving | vehicle/agent | commercial | partial | no | no | vehicle/agent | motion planning; safety assessment | No network traffic perception or V2X without coupling |
| [ns-3](https://www.nsnam.org/) | V2X communication | packet/network | open | no | no | partial | network/application | V2X cooperation | Requires external mobility and control models |
| [OMNeT++/INET](https://omnetpp.org/) | V2X communication | packet/network | academic/commercial | no | no | partial | network/application | V2X cooperation | Vehicular mobility and V2X require dedicated extensions |
| [Simu5G](https://simu5g.org/) | V2X communication | packet/network | open | no | no | partial | network/application | V2X cooperation | Direct V2X sidelink requires an appropriate extension |
| [Artery/Artery-C](https://github.com/riebl/artery) | V2X communication | packet/network | open | direct | direct | direct | cross-domain | V2X cooperation | Traffic-control effects require explicit control feedback |
| [5G-LENA NR-V2X](https://5g-lena.cttc.es/) | V2X communication | packet/network | open | no | no | direct | network/application | V2X cooperation | Traffic effects require external mobility/control coupling |
| [Veins](https://veins.car2x.org/) | multidomain co-simulation | cross-domain | open | direct | direct | direct | cross-domain | traffic optimization; V2X cooperation; safety assessment | No high-fidelity perception or detailed vehicle dynamics |
| [Eclipse MOSAIC](https://eclipse.dev/mosaic/) | multidomain co-simulation | cross-domain | open/commercial | direct | direct | direct | cross-domain | traffic optimization; V2X cooperation; motion planning; safety assessment | Fidelity depends on selected federates and interfaces |
| [SUMO-CARLA](https://carla.readthedocs.io/en/latest/adv_sumo/) | multidomain co-simulation | cross-domain | open | direct | direct | partial | cross-domain | traffic optimization; motion planning; safety assessment; perception; interaction analysis | No packet-level V2X and synchronization-sensitive |
| [OpenCDA](https://github.com/ucla-mobility/OpenCDA) | multidomain co-simulation | cross-domain | open | direct | direct | partial | cross-domain | V2X cooperation; motion planning; safety assessment; perception; interaction analysis | No packet channel or protocol-level V2X fidelity |

Machine-readable source: [`data/simulators.csv`](../data/simulators.csv).
