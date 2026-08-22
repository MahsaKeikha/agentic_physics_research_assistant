from orchestration.orchestrator import run


def base():
    return {
        "problem_formulation_reviewed": True,
        "assumptions_reviewed": True,
        "dimensional_consistency_reviewed": True,
        "computation_verified": True,
        "evidence_provenance_reviewed": True,
        "uncertainty_reviewed": True,
        "reproducibility_reviewed": True,
        "human_approval": True,
    }


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "human_approval": False}, False),
    ({**base(), "dimensional_inconsistency": True}, False),
    ({**base(), "computation_failed_verification": True}, False),
    ({**base(), "unsupported_assumption": True}, False),
    ({**base(), "evidence_provenance_missing": True}, False),
    ({**base(), "uncertainty_not_quantified": True}, False),
    ({**base(), "reproducibility_gap": True}, False),
    ({**base(), "contradictory_evidence_unresolved": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += run(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
