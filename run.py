from orchestration.orchestrator import run

REFERENCE_CONTEXT = {
    "objective": "formulate and review a physics research problem",
    "evidence": [],
    "problem_formulation_reviewed": True,
    "assumptions_reviewed": True,
    "dimensional_consistency_reviewed": True,
    "computation_verified": True,
    "evidence_provenance_reviewed": True,
    "uncertainty_reviewed": True,
    "reproducibility_reviewed": True,
    "human_approval": True,
}

if __name__ == "__main__":
    print(run(REFERENCE_CONTEXT))
