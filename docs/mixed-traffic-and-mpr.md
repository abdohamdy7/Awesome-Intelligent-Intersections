# Mixed traffic and market penetration

[Back to the repository overview](../README.md) · [Complete paper index](papers.md)

Market penetration rate (MPR) is useful only when paired with capabilities. Two fleets with the same reported percentage can expose very different information and control authority.

## Capability view

| Participant label | Observable beyond ordinary sensing | V2X connected | Longitudinal/lateral motion controllable by the system |
|---|---:|---:|---:|
| Human-driven vehicle (HDV) | Sometimes | No | No |
| Connected vehicle (CV) | Yes | Yes | No, unless the driver follows an advisory |
| Automated vehicle (AV) | Yes through onboard sensing | Not necessarily | Yes by onboard automation |
| Connected automated vehicle (CAV) | Yes | Yes | Yes, within the automation design domain |

These labels are study-dependent. Every repository record should be checked against the paper's actual definitions.

## MPR interpretation

| Reported regime | What should accompany it |
|---|---|
| 0% connected/automated | Baseline driver and sensing assumptions |
| Low penetration | Which equipped vehicles are sampled; observability and influence mechanisms |
| Intermediate penetration | Fleet composition, randomization, repeated seeds, and sensitivity across rates |
| 100% CAV | Communication/control assumptions and why the case is operationally relevant |
| Unknown or variable | Distribution, time variation, estimation method, and controller robustness |

## Minimum reporting checklist

- Define the denominator and every participant class included in MPR.
- Separate connectivity penetration from automation penetration when they differ.
- State which actors are observable, connectable, advisory-only, or controllable.
- Describe unequipped-driver models and whether they react to equipped vehicles.
- Evaluate more than one penetration level and report random fleet assignments.
- Report communication degradation and sensing uncertainty where V2X is safety- or control-critical.
- Avoid using a full-CAV result as evidence for mixed traffic unless the method and constraints explicitly model both.

For structured filtering, use the `traffic_context` and `coordination_architecture` fields in [`data/papers.csv`](../data/papers.csv).
