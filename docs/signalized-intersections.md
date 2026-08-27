# Signalized intersections

[Back to the repository overview](../README.md) · [Complete paper index](papers.md)

Signalized-intersection research spans more than phase selection. The survey separates five streams by the information consumed and the decision produced. This makes it easier to compare a detector-based controller with a trajectory optimizer or a multimodal priority policy without treating them as interchangeable.

![Signalized-intersection research streams](../assets/figures/signalized-research-streams.png)

## Research streams

| Research stream | Main information | Typical decision or output | Representative records |
|---|---|---|---|
| Traffic-responsive signal control | Counts, occupancies, queues, phase state | Phase, split, cycle, offset | Webster; SCOOT; RHODES; SURTRAC |
| State estimation and prediction | Detector events, probe trajectories, SPaT/MAP | Queue, arrival profile, turning demand, near-term state | Liu et al.; Priemer and Friedrich; Feng et al. |
| Signal-trajectory or eco-driving coordination | SPaT/MAP, vehicle states, route or platoon intent | Speed advisory, trajectory, platoon approach, sometimes signal timing | Kamalanathsharma and Rakha; Fayazi and Vahidi; Xu et al. |
| Learning-based control | Encoded traffic state, reward, graph context | Phase or timing policy | PressLight; CoLight; MPLight; AttendLight |
| Multimodal, priority, and safety-aware control | Transit/emergency requests, pedestrian and cyclist state, conflict indicators | Priority, phase extension, service order, protective timing | priority and VRU-aware studies in the paper index |

## Reading the evidence correctly

- A signal controller and a vehicle advisory system have different control authority even when both use SPaT.
- Closed-loop simulation is stronger than trace replay for evaluating an adaptive controller, but it is not field evidence.
- Network-level results should report coordination topology and communication assumptions.
- Mixed-traffic claims should state which vehicles are observable, connected, and controllable—not only a market-penetration percentage.

The machine-readable records and verified implementation status are in [`data/papers.csv`](../data/papers.csv).
