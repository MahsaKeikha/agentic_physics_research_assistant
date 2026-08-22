# F81 | Agentic Physics Research Assistant | L3 Gold Standard | v1.0

A governed multi-agent reference system for physics research support with explicit problem formulation, theory analysis, computational reasoning, evidence discipline, uncertainty handling, reproducibility, and qualified human review.

## Research pipeline

- Problem formulation
- Theory analysis
- Computational reasoning
- Evidence review
- Scientific reviewer

Tools and skills cover dimensional analysis, model selection, literature synthesis, uncertainty reasoning, reproducible research, equation registration, evidence tracking, reproducibility checks, uncertainty tables, and unit checking.

## Gold-standard research integrity

F81 is fail closed. Research release requires reviewed problem formulation and assumptions, dimensional-consistency review, verified computation, evidence provenance, uncertainty review, reproducibility review, and explicit qualified human approval.

Release is blocked for dimensional inconsistencies, failed computation verification, unsupported assumptions, missing evidence provenance, uncharacterized material uncertainty, reproducibility gaps, or unresolved contradictory evidence.

The reference system cannot autonomously claim a result is proven or experimentally confirmed, fabricate evidence, hide uncertainty, or exercise autonomous scientific authority.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

The behavioral verification layer includes eight direct research-integrity tests and a 10-scenario held-out suite.
