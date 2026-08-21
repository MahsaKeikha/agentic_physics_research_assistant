from AGENTS.problem_formulation_agent import run as formulate
from AGENTS.theory_agent import run as theory
from AGENTS.computation_agent import run as compute
from AGENTS.evidence_agent import run as evidence
from AGENTS.reviewer_agent import run as review

def run(context):
    return {"problem":formulate(context),"theory":theory(context),"computation":compute(context),"evidence":evidence(context),"review":review(context)}
