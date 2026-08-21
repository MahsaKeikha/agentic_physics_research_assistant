from run import run

def test_smoke():
    result = run({"question": "reference physics problem"})
    assert result["system"] == "F81"
    assert result["human_review_required"] is True
