# Foundation-model assistance

[Back to the repository overview](../README.md) · [Section citation catalog](references/foundation-models.md) · [Core comparison papers](papers.md)

Foundation models can support an intelligent intersection without being granted direct control authority. The survey therefore classifies both the model's role and the safety boundary around it.

![Foundation-model roles and system boundary](../assets/figures/foundation-model-architecture.png)

## Role tags

| Role | Typical uses | Intersection-control claim | Representative linked papers |
|---|---|---|---|
| **Direct** | Generate candidate phases, policies, coordination plans, or high-level driving actions | Requires intersection-specific closed-loop validation and a bounded execution interface | [LLMLight](https://doi.org/10.1145/3690624.3709379); [CoLLMLight](https://openreview.net/forum?id=KeJqoEVOeY); [MTD-GPT](https://doi.org/10.1109/ITSC57777.2023.10421993) |
| **Enabling** | Perception/scene understanding, simulation generation, explanation, operator interaction, tool use, adaptation | Improves a subsystem; does not by itself establish safe control performance | [TrafficGPT](https://doi.org/10.1016/j.tranpol.2024.03.006); [PromptGAT](https://doi.org/10.1609/aaai.v38i1.27758); [MAPLM](https://doi.org/10.1109/CVPR52733.2024.02061) |
| **Adjacent** | General autonomous-driving reasoning, language-conditioned planning, or multimodal driving research | Relevant evidence, but not a validated intersection-management method | [MLLM-AD survey](https://openaccess.thecvf.com/content/WACV2024W/LLVM-AD/html/Cui_A_Survey_on_Multimodal_Large_Language_Models_for_Autonomous_Driving_WACVW_2024_paper.html); [VLA-AD survey](https://openaccess.thecvf.com/content/ICCV2025W/) |

## Authority boundary

| Model output | Recommended execution boundary |
|---|---|
| Explanation or operator summary | Human review; provenance and uncertainty visible |
| Scenario, reward, or configuration proposal | Schema validation, sandbox simulation, and regression tests |
| Candidate signal plan or vehicle maneuver | Deterministic feasibility and safety filter before actuation |
| Direct low-level actuation | Outside the evidence supported by most current foundation-model studies; demands independent safety assurance and fallback |

## Evidence expected for direct-control claims

- A clear action space, update rate, context window, and tool/API specification.
- Validity checks for phase conflicts, minimum timing, clearance, right-of-way, kinematics, and collision avoidance.
- Comparison with strong traffic-engineering, optimization, and learning baselines.
- Closed-loop tests across demand, incidents, sensing noise, communication loss, and out-of-distribution scenes.
- Runtime, cost, repeatability, model/version details, and deterministic fallback behavior.
- Human factors and cybersecurity analysis when natural-language or remote tools affect operations.

The current code-backed examples in the collection include [LLMLight](https://github.com/usail-hkust/LLMTSCS), [CoLLMLight](https://github.com/usail-hkust/CoLLMLight), [PromptGAT](https://github.com/DaRL-LibSignal/PromptGAT), and [TrafficGPT](https://github.com/lijlansg/TrafficGPT).

See the [complete foundation-model citation page](references/foundation-models.md) for all references used by the manuscript section.
