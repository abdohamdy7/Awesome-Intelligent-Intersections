# Non-signalized intersections and AIM

[Back to the repository overview](../README.md) · [Complete paper index](papers.md)

This area ranges from human gap acceptance to centralized reservation systems for fully connected automated vehicles. The survey keeps those operating assumptions visible because an algorithm that controls every vehicle does not automatically transfer to a public mixed-traffic intersection.

![Non-signalized-intersection research streams](../assets/figures/non-signalized-research-streams.png)

## Research streams

| Research stream | Information | Decision or interaction | Central assumption |
|---|---|---|---|
| Gap acceptance and priority rules | Arrival, speed, conflict gap, priority | Enter, yield, or wait | Human or rule-based behavior dominates |
| Centralized reservation AIM | Connected trajectories and requests | Space-time reservation or crossing order | Infrastructure manager can communicate with and constrain participants |
| Optimization-based coordination | Predicted states, constraints, objectives | Sequence, schedule, or trajectory | Models and forecasts are sufficiently accurate |
| Distributed and game-theoretic control | Local state, messages, intent | Negotiated or decentralized actions | Agents follow a communication/behavior protocol |
| Mixed-traffic coordination | Partial CAV state plus inferred HDV behavior | CAV actions, gaps, virtual signals, or advisories | CAVs influence but do not directly control HDVs |
| Learning and interaction-aware planning | Histories, observations, learned representations | Policy, intent prediction, or socially compatible trajectory | Training coverage and safety constraints generalize |

## Assumptions to report

1. Intersection control: priority rules, stop/yield control, virtual signal, or signal-free AIM.
2. Participants: HDV, CV, AV, CAV, pedestrian, cyclist, and other VRU classes.
3. Authority: which actors are observed, communicated with, advised, or directly controlled.
4. Communications: message content, range, latency, loss, and behavior on failure.
5. Safety mechanism: collision constraints, reachability, fallback, or supervisory override.
6. Evidence: synthetic simulation, recorded-data replay, closed-loop simulation, hardware, track, or public road.

Observability is not controllability. Connectivity may improve state estimation while leaving the human driver fully responsible for motion. Conversely, automated vehicles may be controllable without infrastructure connectivity. These distinctions are central to the survey taxonomy.
