from dataclasses import dataclass, field
@dataclass
class RunState:
    stage: str = "intake"
    assumptions: list = field(default_factory=list)
    findings: list = field(default_factory=list)
