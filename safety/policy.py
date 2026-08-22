"""Fail-closed research-integrity policy for F81 physics research."""

REQUIRED_REVIEWS = (
    "problem_formulation_reviewed",
    "assumptions_reviewed",
    "dimensional_consistency_reviewed",
    "computation_verified",
    "evidence_provenance_reviewed",
    "uncertainty_reviewed",
    "reproducibility_reviewed",
    "human_approval",
)

BLOCKED_CLAIMS = {
    "claim_proven",
    "claim_experimentally_confirmed",
    "fabricate_evidence",
    "hide_uncertainty",
}


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in BLOCKED_CLAIMS:
        return {"allowed": False, "reason": "unsupported scientific authority is outside reference-system scope"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required scientific review", "missing": missing}

    blockers = []
    if context.get("dimensional_inconsistency"):
        blockers.append("dimensional inconsistency unresolved")
    if context.get("computation_failed_verification"):
        blockers.append("computation verification failed")
    if context.get("unsupported_assumption"):
        blockers.append("unsupported assumption unresolved")
    if context.get("evidence_provenance_missing"):
        blockers.append("evidence provenance incomplete")
    if context.get("uncertainty_not_quantified"):
        blockers.append("material uncertainty not characterized")
    if context.get("reproducibility_gap"):
        blockers.append("reproducibility gap unresolved")
    if context.get("contradictory_evidence_unresolved"):
        blockers.append("contradictory evidence unresolved")

    if blockers:
        return {"allowed": False, "reason": "research-integrity blocker", "blockers": blockers}

    return {"allowed": True, "reason": "research package approved after qualified human review"}


def require_human_review(result: dict) -> dict:
    result["human_review_required"] = True
    return result
