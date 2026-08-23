# F81 Agentic Physics Research Assistant

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A governed multi-agent reference architecture for physics research support across problem formulation, theoretical analysis, computational reasoning, evidence review, uncertainty handling, reproducibility, and qualified human scientific review.

F81 is designed for researchers, students, engineers, and technical teams who need a structured way to move from a physics question to a traceable research package without collapsing assumptions, equations, computation, evidence, uncertainty, and scientific judgment into one opaque step.

The repository supports analysis and research organization. It does not autonomously establish scientific truth, claim experimental confirmation, fabricate evidence, replace peer review, or exercise independent scientific authority.

## Research workflow

```text
research question
      |
      v
problem formulation
      |
      v
theory analysis
      |
      v
computational reasoning
      |
      v
evidence review
      |
      v
uncertainty + reproducibility
      |
      v
qualified human scientific review
```

The workflow is intentionally fail closed. Unsupported assumptions, dimensional inconsistencies, failed verification, missing evidence provenance, uncharacterized uncertainty, or unresolved contradictions remain visible as blockers.

## Multi-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Problem Formulation Agent | Defines the physical system, research question, variables, assumptions, boundary conditions, observables, and intended claim | What exactly is being studied, under which assumptions and physical regime? |
| Theory Agent | Reviews governing principles, candidate models, approximations, equations, limiting cases, and dimensional consistency | Is the theoretical model appropriate and internally consistent for the stated regime? |
| Computation Agent | Structures numerical, symbolic, simulation, or computational reasoning and verification | Are calculations reproducible, numerically sound, and consistent with the theoretical assumptions? |
| Evidence Agent | Tracks literature, experimental evidence, computational evidence, contradictions, and provenance | What evidence supports or challenges the result, and how reliable is that evidence? |
| Reviewer Agent | Consolidates uncertainty, reproducibility, evidence quality, unresolved limitations, and qualified human review | Is the research package ready for scientific interpretation by a qualified human? |

The agents produce complementary evidence. No individual agent can independently elevate a tentative result into a proven or experimentally confirmed scientific conclusion.

## Repository structure

```text
AGENTS/
├── problem_formulation_agent.py
├── theory_agent.py
├── computation_agent.py
├── evidence_agent.py
└── reviewer_agent.py

SKILLS/
├── dimensional_analysis.py
├── model_selection.py
├── literature_synthesis.py
├── uncertainty_reasoning.py
└── reproducible_research.py

TOOLS/
├── equation_register.py
├── evidence_tracker.py
├── reproducibility_check.py
├── uncertainty_table.py
└── unit_checker.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The architecture separates domain reasoning from deterministic evidence handling, orchestration, state, evaluation, observability, and governance.

## Problem formulation

A strong physics workflow begins by defining the problem precisely before choosing equations or numerical methods.

A formulation record can include:

```text
problem_id
research_question
physical_system
observables
independent_variables
dependent_variables
parameters
initial_conditions
boundary_conditions
symmetries
constraints
assumptions
physical_regime
approximation_regime
reference_frame
expected_outputs
claim_scope
```

The Problem Formulation Agent should identify whether the task is, for example, explanatory, predictive, inferential, computational, comparative, experimental, or model-building.

Ambiguous problem statements should remain visibly ambiguous instead of being silently converted into more convenient assumptions.

## Assumptions as first-class evidence

Physics results often depend as much on assumptions as on algebra.

Important assumptions can include:

- isolated versus open system
- linear versus nonlinear behavior
- continuum approximation
- equilibrium versus nonequilibrium
- weak versus strong coupling
- classical versus quantum regime
- nonrelativistic versus relativistic regime
- stationary versus time-dependent behavior
- idealized geometry
- negligible dissipation
- perturbative approximation
- mean-field approximation
- symmetry assumptions
- material idealizations

F81 keeps assumptions explicit and traceable to downstream equations and conclusions.

If a conclusion only holds in a narrow regime, the result should be labeled accordingly.

## Theory analysis

The Theory Agent reviews the governing framework before computation begins.

Potential theoretical tasks include:

- identifying conservation laws
- selecting governing equations
- deriving relations
- checking limiting behavior
- evaluating approximations
- identifying symmetries
- checking invariants
- determining scaling behavior
- comparing competing models
- checking consistency with established physical principles

The theory stage should distinguish between exact relations, approximations, empirical models, phenomenological models, and heuristic reasoning.

## Equation registry

`TOOLS/equation_register.py` provides a deterministic structure for recording equations and their role in the analysis.

A useful equation record can include:

```text
equation_id
expression
variable_definitions
units
origin
assumptions
validity_regime
approximation_status
source
used_by
```

Equation provenance matters. An equation copied from a source without its assumptions or validity regime can be misleading.

## Dimensional analysis

Dimensional consistency is one of the strongest low-cost verification tools in physics.

`SKILLS/dimensional_analysis.py` and `TOOLS/unit_checker.py` support checks around:

- units on both sides of an equation
- derived-unit consistency
- dimensionless groups
- scaling behavior
- normalization
- conversion errors
- hidden unit conventions

A dimensionally inconsistent equation is treated as a research blocker until resolved.

Dimensional consistency is necessary but not sufficient. A dimensionally valid expression can still be physically wrong.

## Units and conventions

Research artifacts should identify unit systems and conventions explicitly.

Examples include:

- SI units
- Gaussian or cgs conventions
- natural units
- atomic units
- geometrized units
- normalized simulation units

The workflow should not silently mix conventions.

When natural or normalized units are used, conversion back to measurable quantities should be documented where relevant.

## Model selection

`SKILLS/model_selection.py` supports comparison among candidate physical models.

Model selection should consider:

- intended scale
- parameter range
- validity regime
- approximations
- known failure modes
- empirical support
- computational cost
- interpretability
- required precision
- compatibility with available evidence

A more complicated model is not automatically a better model. The preferred model should be appropriate to the physical question and evidence.

## Limiting cases

Useful verification often comes from checking known limits.

Examples include:

- zero coupling
- large or small parameter limits
- low velocity
- weak field
- high or low temperature
- classical limit
- continuum limit
- equilibrium limit
- symmetry-restored cases

If a derived expression fails a well-established limiting case, the discrepancy should be investigated before release.

## Approximation tracking

Approximations should be registered rather than buried in prose.

A useful approximation record includes:

```text
approximation
justification
small_parameter
expected_error
validity_range
breakdown_condition
downstream_equations
```

This makes it easier to identify when a result is being applied outside its valid regime.

## Computational reasoning

The Computation Agent organizes numerical or symbolic analysis.

Potential computational modes include:

- symbolic algebra
- numerical integration
- differential-equation solvers
- eigenvalue problems
- optimization
- Monte Carlo methods
- parameter sweeps
- finite-difference methods
- finite-element methods
- spectral methods
- particle simulations
- statistical inference

F81 is method-neutral. The important requirement is that the computational path is explicit and verifiable.

## Numerical verification

Computational results should be checked for more than successful execution.

Relevant checks include:

- convergence
- resolution dependence
- time-step dependence
- mesh dependence
- tolerance sensitivity
- initial-condition sensitivity
- boundary-condition sensitivity
- numerical stability
- conservation behavior
- solver agreement
- benchmark comparison
- floating-point limitations

A result should not be treated as physically meaningful merely because a numerical solver returned a value.

## Analytical versus numerical agreement

Where analytical approximations or exact solutions exist, they can serve as verification references.

Useful comparisons include:

```text
numerical_result
analytical_reference
difference
relative_error
expected_approximation_error
regime
```

Disagreement may indicate a numerical bug, an invalid approximation, a unit problem, or genuinely different physical regimes.

## Simulation provenance

A reproducible simulation should preserve:

- code version
- model version
- input parameters
- initial conditions
- boundary conditions
- solver
- solver version
- tolerances
- random seeds where relevant
- hardware or backend where relevant
- run identifier
- output files
- postprocessing version

Results without sufficient provenance should not be presented as reproducible computation.

## Evidence discipline

The Evidence Agent distinguishes different kinds of support.

Evidence can include:

- peer-reviewed literature
- experimental measurements
- observational data
- established theory
- benchmark datasets
- validated simulations
- independent calculations
- technical reports
- preprints
- internal results

`TOOLS/evidence_tracker.py` provides a structured way to attach provenance and relevance to each evidence item.

## Literature synthesis

`SKILLS/literature_synthesis.py` supports disciplined comparison of sources.

A literature record should capture, where relevant:

```text
source
claim
method
physical_regime
sample_or_dataset
result
uncertainty
limitations
relationship_to_current_problem
```

The number of citations alone is not an evidence-quality metric.

Sources can disagree because of different assumptions, regimes, methods, measurement conditions, or unresolved scientific questions.

## Contradictory evidence

F81 treats unresolved contradictory evidence as a first-class review issue.

When sources disagree, the workflow should identify:

- whether they study the same physical regime
- whether definitions differ
- whether measurement methods differ
- whether systematic errors differ
- whether assumptions differ
- whether later work supersedes earlier work
- whether the contradiction remains genuinely unresolved

The system should not force an artificial consensus.

## Experimental evidence boundary

A theoretical or computational result is not experimental confirmation.

The workflow should distinguish:

```text
theoretical prediction
computational result
simulation result
experimental measurement
replication
independent confirmation
```

F81 must not use phrases such as "experimentally confirmed" unless appropriate experimental evidence and qualified human review support the claim.

## Uncertainty

`SKILLS/uncertainty_reasoning.py` and `TOOLS/uncertainty_table.py` provide explicit uncertainty handling.

Sources of uncertainty can include:

- measurement uncertainty
- parameter uncertainty
- numerical error
- model uncertainty
- approximation error
- initial-condition uncertainty
- calibration uncertainty
- sampling uncertainty
- systematic error
- literature disagreement

A useful uncertainty table can contain:

```text
quantity
nominal_value
uncertainty_type
uncertainty_magnitude
source
propagation_method
materiality
```

Uncertainty should not be hidden simply because a central estimate is convenient.

## Uncertainty propagation

Depending on the problem, uncertainty can be propagated using:

- analytical propagation
- linearization
- covariance methods
- Monte Carlo sampling
- interval methods
- sensitivity analysis
- Bayesian methods

The chosen method should match the structure of the uncertainty and the required precision.

## Significant figures

Reported numerical precision should reflect actual uncertainty.

A result with poorly constrained parameters should not be presented with many unsupported decimal places.

Apparent precision is not equivalent to physical accuracy.

## Sensitivity analysis

Sensitivity analysis helps determine which assumptions and parameters materially affect a result.

Relevant outputs include:

- local parameter sensitivity
- global parameter sensitivity
- dominant uncertainty contributors
- threshold effects
- bifurcation or transition regions
- approximation breakdown regions

Sensitivity results can help prioritize future measurement or modeling work.

## Statistical reasoning

When statistical inference is part of the physics problem, F81 should track:

- null and alternative hypotheses
- likelihood or objective function
- priors where applicable
- selection effects
- multiple testing
- confidence or credible intervals
- effect size
- goodness of fit
- residual structure
- model comparison

Statistical significance should not be automatically translated into physical importance.

## Causal claims

A correlation, fit, or predictive model does not by itself establish a causal physical mechanism.

Causal language should be matched to the design, model assumptions, intervention structure, and evidence.

When the workflow supports only association or model consistency, conclusions should remain at that level.

## Reproducibility

`SKILLS/reproducible_research.py` and `TOOLS/reproducibility_check.py` support the reproducibility layer.

A reproducibility package can include:

- research question
- assumptions
- governing equations
- source data
- code
- software environment
- parameter values
- unit conventions
- computational settings
- random seeds
- generated outputs
- figures
- uncertainty analysis
- evidence sources

The goal is for another qualified researcher to understand how the result was produced and what would be required to reproduce it.

## Replication versus reproducibility

F81 distinguishes:

- **reproducibility**, obtaining the same result using the same data and analysis pipeline
- **replication**, obtaining consistent evidence through an independent dataset, experiment, measurement, or analysis

A reproducible result can still be wrong. Independent replication provides a different level of confidence.

## Provenance

Provenance should connect conclusions back to the evidence and computation that support them.

Useful lineage includes:

```text
claim
supporting_equations
supporting_computation
supporting_evidence
assumptions
uncertainty
limitations
review_state
```

Claims without traceable support should be downgraded or blocked.

## Human scientific review

The Reviewer Agent consolidates the research package for qualified human interpretation.

Review should consider:

- problem clarity
- assumption validity
- dimensional consistency
- theoretical coherence
- computational verification
- evidence provenance
- contradictory evidence
- uncertainty completeness
- reproducibility
- claim strength
- unresolved limitations

Human review is required for release of consequential scientific claims.

## Claim-strength discipline

F81 distinguishes different levels of scientific language.

Examples include:

```text
calculation suggests
model predicts
simulation produces
result is consistent with
observations support
evidence favors
experiment detects
independent replication confirms
```

The strongest wording should only be used when the supporting evidence warrants it.

The system must not autonomously claim that a result is proven, experimentally confirmed, or a scientific discovery.

## Research integrity

The repository is designed to preserve research integrity by blocking:

- fabricated evidence
- invented citations
- hidden assumptions
- omitted material uncertainty
- unsupported confirmation claims
- silent unit conversion
- selective removal of contradictory evidence
- undocumented computational changes

When evidence is unavailable, the correct output is an evidence gap, not invented support.

## Observability

The `observability/` layer provides execution traces for the research workflow.

Useful research telemetry includes:

- assumptions registered
- equations registered
- dimensional checks
- computation verification status
- evidence items tracked
- contradictory evidence flags
- uncertainty completeness
- reproducibility status
- unresolved limitations
- human-review state

Observability supports auditability. It should not be confused with scientific evidence itself.

## Fail-closed research governance

F81 blocks research release when material evidence is incomplete.

Reference blockers include:

- problem formulation incomplete
- physical regime undefined
- unsupported assumption
- dimensional inconsistency
- unit mismatch
- governing model unsupported
- computation verification failed
- numerical convergence unresolved
- evidence provenance missing
- contradictory evidence unresolved
- uncertainty material but uncharacterized
- reproducibility incomplete
- experimental-confirmation claim unsupported
- proof claim unsupported
- scientific-discovery claim unsupported
- qualified human review missing

The system should expose uncertainty and disagreement instead of optimizing for a confident narrative.

## Explicit failure states

Useful states include:

```text
PROBLEM FORMULATION INCOMPLETE
PHYSICAL REGIME UNDEFINED
ASSUMPTION UNSUPPORTED
DIMENSIONAL CONSISTENCY FAILED
UNIT CHECK FAILED
MODEL VALIDITY UNRESOLVED
COMPUTATION VERIFICATION FAILED
NUMERICAL CONVERGENCE UNRESOLVED
EVIDENCE PROVENANCE MISSING
CONTRADICTORY EVIDENCE UNRESOLVED
UNCERTAINTY INCOMPLETE
REPRODUCIBILITY FAILED
EXPERIMENTAL CONFIRMATION NOT ESTABLISHED
PROOF CLAIM NOT ESTABLISHED
DISCOVERY CLAIM NOT AUTHORIZED
HUMAN SCIENTIFIC REVIEW REQUIRED
```

## End-to-end reference workflow

A typical F81 research task follows this sequence:

1. Define the research question and intended claim.
2. Define the physical system, observables, variables, parameters, initial conditions, and boundary conditions.
3. Register assumptions and the physical regime.
4. Identify governing laws and candidate models.
5. Record equations and their provenance.
6. Perform dimensional and unit checks.
7. Examine limiting cases and approximation validity.
8. Define the computational method where needed.
9. Verify numerical convergence, stability, and benchmark behavior.
10. Track simulation or calculation provenance.
11. Map supporting and contradictory evidence.
12. Characterize and propagate uncertainty.
13. Run sensitivity analysis where material.
14. Check reproducibility requirements.
15. Match claim language to the demonstrated evidence level.
16. Apply fail-closed research gates.
17. Require qualified human scientific review.

## Evaluation and held-out suite

The repository includes evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test research integrity, not only whether the system produces mathematically sophisticated text.

Useful dimensions include:

- problem-definition completeness
- assumption tracking
- dimensional-consistency enforcement
- unit checking
- model-validity reasoning
- computation-verification enforcement
- convergence awareness
- evidence provenance
- contradiction handling
- uncertainty handling
- reproducibility enforcement
- unsupported-claim detection
- human-review enforcement

Strong held-out cases should deliberately include plausible-looking but dimensionally inconsistent equations, unsupported assumptions, irreproducible computations, missing provenance, contradictory evidence, or overclaimed conclusions.

## Reproduce the reference implementation

Install development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run the repository checks:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

CI under `.github/workflows/ci.yml` validates Python 3.10, 3.11, and 3.12.

## L3 Gold Standard

F81 follows the library's L3 Gold Standard structure through specialist-agent separation, deterministic evidence tools, explicit state and orchestration, safety and integrity controls, observability, held-out evaluation, CI, fail-closed research gates, and qualified human scientific review.

This maturity designation describes the engineering and governance structure of the repository. It does not mean that a generated physics result is scientifically proven, peer reviewed, experimentally validated, or accepted by the scientific community.

## Extending F81

Common extensions include:

- symbolic algebra systems
- numerical solvers
- simulation frameworks
- notebook environments
- literature databases
- experimental data repositories
- uncertainty libraries
- provenance databases
- experiment tracking
- equation databases
- model registries
- computational clusters
- versioned datasets
- peer-review workflows

New integrations should preserve assumptions, provenance, units, uncertainty, reproducibility, and human scientific authority.

## Example applications

F81 can serve as a reference architecture for research involving:

- classical mechanics
- electromagnetism
- thermodynamics
- statistical mechanics
- fluid dynamics
- condensed matter
- optics
- relativity
- quantum physics
- plasma physics
- computational physics
- theoretical modeling
- experimental-data interpretation

Each domain requires its own physical expertise and validation standards.

## Design principles

1. Define the physical problem before selecting equations.
2. Treat assumptions and validity regimes as part of the result.
3. Enforce dimensional and unit consistency early.
4. Verify computation rather than trusting successful execution.
5. Preserve evidence and equation provenance.
6. Characterize uncertainty and numerical error explicitly.
7. Keep contradictory evidence visible.
8. Separate reproducibility from independent replication.
9. Match scientific language to the actual strength of evidence.
10. Keep final scientific authority with qualified human researchers.

## Documentation

Additional architecture documentation is available under `docs/`, including `docs/ARCHITECTURE.md`.

## Citation and reuse

Use the repository metadata and citation information supplied by the project when referencing this implementation. The repository can be studied, cited, adapted, and extended subject to its license terms.

## Responsible use

Use F81 as a physics research support and multi-agent scientific-governance reference. Validate assumptions, equations, numerical methods, uncertainty, evidence, reproducibility, and scientific claims against the actual research problem before relying on conclusions. Final scientific interpretation remains with appropriately qualified researchers.