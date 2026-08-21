# Agentic Physics Research Assistant

F81 of the Agentic AI Library.

A standalone multi agent reference system for physics research support with explicit problem formulation, theory analysis, computational reasoning, evidence discipline, uncertainty handling, reproducibility, and human review.

## Actual implementation

- [AGENTS](AGENTS)
- [TOOLS](TOOLS)
- [SKILLS](SKILLS)
- [Orchestration](orchestration/orchestrator.py)
- [Memory](memory/store.py)
- [State](state/run_state.py)
- [Schemas](schemas/context.schema.json)
- [Safety](safety/policy.py)
- [Evaluations](evals/evaluate.py)
- [Benchmarks](benchmarks/cases.json)
- [Tests](tests/test_orchestrator.py)
- [Architecture](docs/ARCHITECTURE.md)

## Run

```bash
python run.py
```

## Test

```bash
python -m pytest -q
```
