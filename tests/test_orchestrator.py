from orchestration.orchestrator import run
from safety.policy import authorize


def valid_context():
    return {
        "objective": "physics research review",
        "problem_formulation_reviewed": True,
        "assumptions_reviewed": True,
        "dimensional_consistency_reviewed": True,
        "computation_verified": True,
        "evidence_provenance_reviewed": True,
        "uncertainty_reviewed": True,
        "reproducibility_reviewed": True,
        "human_approval": True,
    }


def test_full_pipeline_and_review_gate():
    result = run(valid_context())
    assert result["review"]["decision"] == "human_review_required"
    assert "theory" in result and "computation" in result
    assert result["autonomous_scientific_authority"] is False


def test_complete_review_can_release_research_package():
    assert run(valid_context())["release_allowed"] is True


def test_missing_human_approval_fails_closed():
    context = valid_context()
    context["human_approval"] = False
    assert run(context)["release_allowed"] is False


def test_unsupported_proof_claim_is_never_authorized():
    assert authorize("claim_proven", valid_context())["allowed"] is False


def test_dimensional_inconsistency_blocks_release():
    context = valid_context()
    context["dimensional_inconsistency"] = True
    assert run(context)["release_allowed"] is False


def test_failed_computation_verification_blocks_release():
    context = valid_context()
    context["computation_failed_verification"] = True
    assert run(context)["release_allowed"] is False


def test_missing_evidence_provenance_blocks_release():
    context = valid_context()
    context["evidence_provenance_missing"] = True
    assert run(context)["release_allowed"] is False


def test_reproducibility_gap_blocks_release():
    context = valid_context()
    context["reproducibility_gap"] = True
    assert run(context)["release_allowed"] is False
