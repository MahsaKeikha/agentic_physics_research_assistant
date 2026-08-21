from orchestration.orchestrator import run

def test_full_pipeline_and_review_gate():
    result=run({"objective":"test"})
    assert result["review"]["decision"]=="human_review_required"
    assert "theory" in result and "computation" in result
