from AGENTS.computation_agent import run as compute
from AGENTS.evidence_agent import run as evidence
from AGENTS.problem_formulation_agent import run as formulate
from AGENTS.reviewer_agent import run as review
from AGENTS.theory_agent import run as theory
from safety.policy import authorize


def run(context: dict) -> dict:
    """Run the physics research pipeline and apply research-integrity governance."""
    result = {
        "problem": formulate(context),
        "theory": theory(context),
        "computation": compute(context),
        "evidence": evidence(context),
        "review": review(context),
    }
    governance = authorize("research_release", context)
    result.update(
        {
            "system": "F81",
            "governance": governance,
            "release_allowed": governance["allowed"],
            "human_review_required": True,
            "autonomous_scientific_authority": False,
        }
    )
    return result
