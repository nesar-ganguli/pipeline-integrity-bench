# PipelineIntegrityBench — Project Charter, Architecture, and Milestones

**Project:** PipelineIntegrityBench  
**Repository:** `pipeline-integrity-bench`  
**Event:** micro1 Eval Hackathon (2026)  
**Document status:** v1.0 — implementation plan, not a claim that tasks or experiments have been validated  
**Intended reader:** Codex in VS Code and the human project owner  
**Primary outcome:** One original, reproducible benchmark showing whether—and specifically when—frontier AI systems fail to preserve correctness in realistic data-pipeline transformations.

> **Codex operating instruction:** Read this entire document before generating code. Follow the stage gates. Do **not** generate all eight tasks and declare success in one pass. Build a minimal vertical slice, verify reference solutions and grader validity, and then expand. Any checkpoint marked **HUMAN DECISION** requires an explicit owner decision before continuing that branch. Document all choices in `docs/decision-log.md`. Never invent model results or claim a model fails before trials prove it.

## 0. Source of truth, rules, and deadlines

This plan is based on the supplied *Find What AI Can't Do Yet: A Participant's Guide to the micro1 Eval Hackathon* (22 pages) and user-provided event screenshots. The HackerRank event **Instructions** tab at kickoff is authoritative for the final submission schema. Codex must compare these requirements with that tab when it becomes accessible; do not silently treat the sample folder layout as mandatory.

**Published guide requirements:**
- Build **one** individual, original eval grounded in real expertise; ~**5–10 tasks** are recommended.
- Include a **validated reference solution** for every task; every correct reference must pass its grader.
- Prove graders can reject intentionally wrong answers; avoid false passes and false fails.
- Test **at least one frontier model**, with **multiple trials per task**. A practical starting recommendation is **3–5 trials/task**.
- Preserve outputs/transcripts, model IDs/versions, run dates, generation settings, costs and runtime.
- Show concrete, explainable model failures, not merely an aggregate leaderboard or trick questions.
- Use synthetic, public, or properly licensed data only; do not submit proprietary employer/client data or keys.
- Ensure a judge can reproduce from a clean environment with the README.
- Submit through HackerRank: **ZIP under 50 MB** (code/small support files, README; no video), **publicly accessible video link** (maximum 5 minutes), and **short written description**. The README must describe the eval, methods, results, provenance, limitations and AI use.
- **Deadline:** November 9, 2026, **05:15 GMT** (November 8, 2026 at **9:15 PM Pacific**; November 9 at **12:15 AM Eastern**). Event guide lists winners announced November 23, 2026.
- **No fixed target pass rate** exists. A 0% result on every model/trial merits diagnosing a broken task/grader; ~100% on the strongest model provides limited evidence of remaining difficulty.
- Harbor/Docker are **optional**, not an eligibility requirement; if chosen, ensure the exact harness/environment/verification behavior is reproducible.

**Judging rubric (100 points):** Task design 20; grader reliability 20; relevance 15; evidence of limitations 15; reproducibility 15; human expertise/review 10; insight/hot take 5. Prioritize those weights over a fancy UI.

**Pre-work:** The owner must personally read/accept the participant agreement and verify the actual event submission fields. Codex cannot accept agreements or assert submission succeeded.

## 1. Problem statement and research hypothesis

**Practical problem:** LLMs can output valid-looking SQL or PySpark pipelines that run successfully but silently mis-handle real production conditions such as duplicate deliveries, out-of-order changes, deletes, replayed batches, schema changes, and tenant boundaries. Correct syntax or one passing happy-path example is insufficient when incorrect downstream data could drive financial, operational or privacy decisions.

**Research question:** Under which precisely defined data-integrity conditions do current AI coding models create transformations that violate documented data semantics, and how consistent are those failures across repeated independent trials?

**Falsifiable hypothesis:** Some models will handle isolated transformations but lose correctness when multiple interacting conditions occur. This is **not** an assumed result. Predefine cases on engineering grounds, evaluate honestly, and report success if models succeed.

**What we build:** A compact benchmark of 8 original, self-contained, synthetic data-engineering tasks, each with a precise input contract, expected output schema, reference implementation, deterministic grader and negative controls; plus a local CLI harness that executes solutions safely, calls selected model APIs when configured, saves full trials and aggregates reproducible metrics.

**What we do NOT build:** a chatbot, interactive user interface, a new foundation model, a generic LeetCode/SQL exam, a massive data platform, a claim of production compliance, or an eval whose hidden grader expects unstated conventions.

## 2. Decisions already locked in (avoid re-asking)

| Topic | Default decision | Rationale |
|---|---|---|
| Domain | Data pipeline integrity | Real operational importance and owner expertise |
| Scope | 8 tasks as target; acceptable final set 5–10 if some lack quality | Focus over quantity |
| Language | Python 3.11; standard library plus carefully selected pinned dependencies | Portable, easy to audit |
| Core data format | Small synthetic CSV/JSON/JSONL; UTF-8; timestamps with explicit timezone | Reviewable fixtures |
| Model output contract | For first implementation, **Python function code** with a documented `transform(inputs)` interface returning JSON-serializable records | Deterministic invocation and cross-model comparability |
| Grading | Primary code-based exact/schema/set/multiset/decimal checks; no LLM grader for core pass/fail | Repeatable and transparent |
| Execution | Isolated subprocess/container with runtime, memory and file/network restrictions; untrusted code is **never** directly imported into evaluator process | Safety and contamination control |
| Evaluation protocol | Same task, data, prompt template and grader per model; 3 independent trials per task to start | Fairness and stability |
| Results | JSONL raw trial records + CSV summary + saved response/transcript artifacts | Inspectable evidence |
| Orchestration | Python CLI; simple provider adapters | Low complexity |
| Code quality | pytest, type hints, black/ruff or comparable pinned formatter/linter | Reliable handoff |
| Version control | Git, small commits by milestone, no secrets committed | Auditability |
| Hosting | No hosted app or frontend required | Focus on quality |
| Test data | Synthetic, reproducibly generated with fixed seeds where generation is used | No data leakage |
| Baseline | Known-correct oracle and deliberately flawed candidate variants | Grader confidence |

**Important nuance:** The coding interface above is a proposed benchmark *design choice*, not a hackathon-required format. It must be clearly explained and defended. A model may use SQL/PySpark reasoning internally, but the initial execution target is Python. If the owner wants to measure SQL or PySpark code generation directly, that is a distinct benchmark design and requires a deliberate decision; do not mix languages inconsistently within the same reported comparison.

## 3. Questions deliberately deferred (decide at the right milestone)

| Decision | Decision point | Options / criterion | Owner action |
|---|---|---|---|
| Python vs SQL/PySpark as the **graded artifact** | M1, before task authoring | Python is simplest; SQL/DuckDB may best fit research claim; PySpark adds setup cost. Keep all tasks comparable. | **HUMAN DECISION** after reviewing a proof-of-concept task |
| Exact model roster and model IDs | M4, before paid runs | At least one current frontier model; ideally 2 frontier families plus one lower-cost comparator if budget allows | **HUMAN DECISION**; no fake exact IDs |
| Available API budget and maximum runtime | M4 | Determine per-model per-task sampling costs, timeouts and caps | **HUMAN DECISION** |
| 3 vs 5 trials and whether to add models | M5 after pilot | Start 3; scale based on variance and budget | **HUMAN DECISION** |
| Whether to add task-specific hidden fixtures | M2 | Prefer hidden test inputs only when instructions state the general rule clearly; never rely on inaccessible knowledge | Decide after grader review |
| Partial-credit scoring | M3 | Binary main pass plus optional documented sub-scores for schema, records, arithmetic and constraints | Decide based on validity/usefulness |
| Harbor vs custom runner | M1 | Custom minimal CLI by default; Harbor optional if it substantially improves reproducibility | Decide after runner skeleton |
| Packaging execution in Docker | M2/M3 | Strongly recommended for evaluating generated code; may use isolated local runtime plus documented sandbox constraints if Docker unavailable | Confirm available environment |
| Whether to include a model-generated `explanation` | M2 | Prefer optional explanation not affecting the correctness grade; save for error analysis | Decide with task format |
| Additional task difficulty | M5 | Only revise with documented reason; separate pilot development from final frozen test set | Explicitly freeze versions before final comparisons |
| Final task count | M5 | Drop ambiguous/broken tasks rather than pad to 8 | Owner review |
| Public benchmark release | M7 | Public repo vs submit ZIP only, considering leakage and licensing | Owner decision |
| Video host | M7 | Unlisted/public video with access tested in private browser | Owner chooses |

Record each finalized decision in `docs/decision-log.md` with date, reason, alternatives, and impact on prior runs. **Any changed benchmark after initial model testing invalidates direct comparisons unless all relevant models are rerun on the same frozen version.**

## 4. Candidate task portfolio (engineering briefs; NOT final benchmark prompts)

Every task must target a concrete failure mode, a defensible deterministic oracle and explicit semantics. Do **not** transcribe these sketches directly as tasks. The owner must validate all assumptions, expected outputs, and negative cases. Combine tricky conditions only where realistic, and avoid piling on unrelated arbitrary gotchas.

| ID | Scenario | What success means | Typical failure to test |
|---|---|---|---|
| T01 | CDC with inserts, updates, deletes | Reconstruct latest valid record state using explicit operation ordering/tie-breaking | Treat delete as a regular row or resurrect deleted records |
| T02 | Late events vs arrival time | Respect declared event-time / processing-time / watermark semantics | Drop valid late records or overwrite newer events |
| T03 | Duplicate delivery vs legitimate repetition | Deduplicate by specified event identity without erasing distinct same-value events | Deduplicate on amount or timestamp alone |
| T04 | Incremental high-watermark + tie cases | Include exact boundary records and preserve checkpoint semantics | Miss equal-timestamp records or reprocess incorrectly |
| T05 | Schema evolution and type safety | Apply explicit versioned schema rules; distinguish absent, null, and invalid values | Silently coerce/drop fields or confuse null with missing |
| T06 | Financial corrections/reversals | Reconstruct ledger totals and balancing entries with correct signs, idempotency and decimal arithmetic | Count corrected and original entries or lose reversals |
| T07 | Replay and idempotent merge | Same final state after one or multiple deliveries of identical batches | Double-count retry/replayed updates |
| T08 | Multi-tenant key collisions | Respect composite key/tenant scope across joins and updates | Cross-tenant contamination with shared local IDs |

**Per-task mandatory contract:**
1. Business context and realistic consequence of error.
2. Prompt-visible complete rules: columns, datatypes, event ordering, key definitions, precedence, invalid/missing-data behavior, time zone, precision, expected return type.
3. Fixture generation code or checked-in synthetic data.
4. A separate deterministic oracle that computes expected results independently where practical.
5. At least one normal example and one nontrivial edge example whose expected answer is manually inspected.
6. Positive, negative, boundary and metamorphic tests (as applicable).
7. A strict but fair grader insensitive to irrelevant representation differences.
8. A written note explaining *why* the difficulty comes from expertise rather than ambiguous wording.
9. A model-visible view that **excludes** oracle implementation, hidden expected outputs and grader code.
10. One or more intentionally incorrect variants that the grader rejects for the intended reason.

**Semantic conventions (must be made explicit in each applicable task):**
- Timestamp parsing, precision, time zone and ordering tie-break rules.
- Primary key/composite key scopes (especially tenant IDs).
- Duplicate `event_id` vs two distinct events with identical content.
- Whether CDC deletes are tombstones, hard deletes or retained with status.
- Whether a late event is valid, too old or a no-op based on the stated window.
- Missing vs explicit null and invalid types.
- Decimal/currency values: use `Decimal` or integer minor units rather than floating-point money.
- Exactly what constitutes acceptable output: record ordering, key set, numeric tolerance, nulls, empty output, and error behavior.
- Whether the same code is expected to generalize to unseen fixtures, not just memorize supplied samples.

**Bias avoidance:** Do not pick tasks solely because one model failed a prompt. Define engineering scenario and pass criteria first. Pilot to debug ambiguity; explicitly log any post-pilot edits.

## 5. Architecture and execution contract

### Proposed repository layout

```text
pipeline-integrity-bench/
├── README.md
├── MILESTONES.md
├── LICENSE                         # choose compatible license later
├── pyproject.toml                  # pinned/runtime dependency configuration
├── requirements.lock               # or pinned requirements.txt
├── .gitignore
├── .env.example                    # placeholder names ONLY
├── src/pipeline_integrity_bench/
│   ├── __init__.py
│   ├── cli.py                       # validate, oracle, pilot, run, summarize, package
│   ├── config.py
│   ├── schemas.py                   # task/trial/results contracts
│   ├── task_loader.py              # explicit model-visible boundaries
│   ├── prompts.py
│   ├── providers/
│   │   ├── base.py
│   │   ├── openai_adapter.py
│   │   ├── anthropic_adapter.py
│   │   └── optional_other.py
│   ├── runner.py
│   ├── execution.py                # isolation, timeouts, resource limits
│   ├── grader.py
│   ├── metrics.py
│   └── reporting.py
├── tasks/
│   ├── t01_cdc/
│   │   ├── task.yaml               # metadata, specification, allowed execution contract
│   │   ├── prompt.md               # model-visible instructions
│   │   ├── fixtures/               # synthetic model-visible inputs
│   │   └── README.md               # private task rationale, if applicable
│   └── ... t02–t08 ...
├── reference/                       # NEVER copied into model prompt/workspace
│   ├── t01_oracle.py
│   └── ...
├── graders/                         # NEVER copied into model prompt/workspace
│   ├── t01_checks.py
│   └── ...
├── tests/
│   ├── test_task_contracts.py
│   ├── test_execution_sandbox.py
│   ├── test_graders_positive_negative.py
│   ├── test_provider_mock.py
│   └── test_metrics.py
├── fixtures/                         # shared synthetic generator(s), if any
├── scripts/
│   ├── smoke_test.sh
│   ├── verify_submission.sh
│   └── create_submission_zip.py
├── docs/
│   ├── decision-log.md
│   ├── methodology.md
│   ├── task-review-checklist.md
│   ├── experimental-protocol.md
│   └── video-outline.md
├── results/                         # small finalized result artifacts only in ZIP
│   ├── summary.csv
│   ├── metrics.json
│   └── run_manifest.json
└── transcripts/                     # representative, sanitized transcripts
```

**Note:** Use a consistent documented package structure, not arbitrary folders. If official HackerRank instructions require another layout, adapt and note the difference.

### Suggested CLI behavior

```bash
python -m pipeline_integrity_bench.cli validate
python -m pipeline_integrity_bench.cli oracle --all
python -m pipeline_integrity_bench.cli smoke --task t01
python -m pipeline_integrity_bench.cli pilot --task t01 --model MODEL_ID --trials 1
python -m pipeline_integrity_bench.cli run --suite tasks --models MODEL_A MODEL_B --trials 3 --out runs/DATE_RUN/
python -m pipeline_integrity_bench.cli summarize --input runs/DATE_RUN/
python -m pipeline_integrity_bench.cli package --output submission.zip
```

These are **design targets** for commands Codex will implement, not commands that already work. Support `--dry-run`, `--help`, and early validation of missing credentials/unsupported model IDs. Do not require paid API access for local unit tests and oracle tests.

### Model trial lifecycle

1. Load **frozen** task metadata, task prompt and synthetic input fixtures.
2. Render consistent prompt with exact output interface and constraints; calculate stable prompt/task hashes.
3. Start a fresh independent trial (no previous conversation or artifacts).
4. Send through selected provider adapter and save raw response and API metadata.
5. Extract model artifact using a documented robust parser. Never silently repair model code in a way that boosts scores; any normalization must be consistent, minimal and logged.
6. Execute untrusted generated code in a new disposable restricted environment; apply time, memory, CPU/file limits; block secrets and network access.
7. Compare result **semantically** to oracle result. Capture exception, timeout and schema failure separately.
8. Save pass/fail, optional component scores, expected/actual diff, token usage if provided, cost estimate if obtainable, model settings, execution details and timestamps.
9. Repeat with clean state and independent generation for requested number of trials.
10. Aggregate per-task/per-model statistics and report confidence/uncertainty transparently.

### Security and integrity requirements

- Never `exec`, `eval`, or import arbitrary model-generated code in the host evaluator process.
- A local subprocess **alone is not a sufficient security boundary** for hostile code; use a restricted container/sandbox for real model trials. If a secure environment is unavailable, implement only mock/oracle runs and mark real execution blocked pending sandbox setup.
- No network in candidate execution; no cloud credentials; mount task inputs read-only and outputs writable only inside an ephemeral sandbox; separate graders/oracles entirely.
- No personal or production data. Use fake names, IDs, financial numbers and tenant IDs.
- Rate-limit retries for transient API errors; log attempts. Fail closed for parser/execution errors and do not automatically turn an unsuccessful run into a pass.
- Never leak oracle/hidden fixtures into prompt, container, logs provided to agent or API request. Repository can store grader files for judges, but candidate runtime cannot see them.
- Protect `.env` and SDK logs; ensure ZIP secret scan.
- Distinguish **model failed task**, **API unavailable**, **execution infrastructure failed** and **invalid task/grader**; exclude infrastructure failures from measured model accuracy until rerun.

### Grading policy

- Primary metric: **task pass** (all mandatory correctness assertions met), independently tested with oracle and negative controls.
- Score actual output/end state, not exact code approach or formatting where alternatives are valid.
- JSON output can be canonicalized (order of unordered records, consistent numeric/UTC handling) but **never** canonicalize away meaningful distinctions (duplicates, tenant leakage, deleted records).
- Use semantic row-keyed comparison and set/multiset checks as appropriate; do not use Python `set` on data where multiplicity matters.
- Use numeric tolerance only where the task contract permits; exact decimal for financial calculations.
- Partial credit may be used as secondary diagnostics, but define components and weights before model comparisons.
- Unit test graders with oracle passes, several wrong variants fail, boundaries and intentionally equivalent correct representations pass.
- If a grader labels a defensibly correct response as wrong, fix the grader, version the change and rerun all compared models.

### Metrics

**Required:** raw pass rate = passes / valid trials, per-task success rates, per-model aggregates, count of timeouts/parser errors, total cost and runtime, versions/settings/date, transcript references.

**Consistency:** `pass^k` for a task/model indicates every one of k independent trials passes. Also optionally `pass@k` indicates at least one passes, clearly distinguishing these metrics from raw pass rate. Report k, denominator and uncertainty. Do **not** claim robustness from one pass.

**Interpretation:** compare across same frozen tasks/graders. Differences may depend on prompting, sample size and model configuration; do not claim statistical significance without supporting analysis. Read failure transcripts manually and classify errors (e.g., wrong CDC precedence, missed boundary, tenant leakage, incorrect rounding).

## 6. Milestone plan and acceptance gates

### M0 — Environment, rules, and repo bootstrap (Oct 30)

**Implement:**
- [ ] Initialize Git repo `pipeline-integrity-bench`; add this `MILESTONES.md` at root.
- [ ] Set up Python project, reproducible environment, basic pytest and linter, `.gitignore`, `.env.example` (no credentials).
- [ ] Copy precise guide requirements into `docs/methodology.md`; mark final event Instructions tab verification pending.
- [ ] Start `docs/decision-log.md`, `docs/task-review-checklist.md`, and a plan for versioned tasks.
- [ ] Create a tiny smoke test that runs without any API keys.

**Exit criteria:** New machine can clone, install pinned dependencies and run basic tests using documented commands. Secrets are absent. Git shows clean logical commit.

### M1 — Scientific design and first vertical slice (Oct 30–31)

**Implement:**
- [ ] Write the testable hypothesis and benchmark capability boundaries in `docs/methodology.md`.
- [ ] Choose candidate programming artifact interface (Python vs SQL/PySpark) with owner; record rationale.
- [ ] Develop **T01 only** end-to-end: explicit prompt, synthetic fixtures, reference oracle, execution contract, deterministic grader, positive/negative tests.
- [ ] Test with a **mock model adapter** producing (a) correct candidate, (b) wrong candidate, (c) syntax error, (d) timeout.
- [ ] Prove model-visible materials do not include oracle/grader secrets.
- [ ] Review actual output diffs with owner.

**Exit criteria:** T01's reference passes 100% of tests; flawed candidate variants fail; equivalent correct output is accepted; infrastructure failures are classified. Owner agrees interface is meaningful and feasible. **HUMAN DECISION: artifact language/interface.**

### M2 — Task portfolio and reference truths (Nov 1–2)

**Implement:**
- [ ] Author T02–T08 from realistic expert scenarios, each independently reviewable.
- [ ] For every task, include clear rules, fixtures, oracle, positive/negative/boundary tests and short domain rationale.
- [ ] Where possible, implement metamorphic checks: duplicating a retried event must not change final output; permuting delivery order should not change output **only when the contract defines order independence**; renaming tenant IDs consistently must preserve isolation.
- [ ] Review tasks for ambiguity, under-specification, unrealistic assumptions, reference leakage and accidental ability to hardcode sample results.
- [ ] Perform human spot checks of expected results on small hand-computable cases.
- [ ] Reject tasks that depend on subjective interpretations or hidden unstated requirements.

**Exit criteria:** Every included task has an unambiguous acceptance contract and a hand-reviewed oracle; no task has unresolved semantic conventions; graders are not contaminated by prompt-visible hidden answers. **HUMAN REVIEW: approve each task before model testing.**

### M3 — Reliable and safe full runner (Nov 3–4)

**Implement:**
- [ ] Build typed task manifest validation and loader.
- [ ] Implement provider abstraction and mock provider with deterministic fixtures for CI.
- [ ] Add model-response parsing, trial isolation, safe code sandbox, resource/time limits and structured execution outcome categories.
- [ ] Implement per-task grading and all positive/negative grader tests.
- [ ] Save trial JSONL, raw prompt/response, run manifest, expected-vs-actual diffs and aggregate CSV.
- [ ] Add CLI help, dry run, graceful interruption and resumability without double-counting trials.
- [ ] Add run reproducibility metadata (Git SHA, task version/hash, prompt hash, Python/dependency versions, OS/container digest where available).
- [ ] Add packaging and secret-leak tests.

**Exit criteria:** Entire suite executes with reference/oracle and mock candidates from a clean environment; unit tests and integration tests pass; a reviewer can inspect why a mock wrong response failed. No untrusted model code executes on host.

### M4 — Pre-registered experimental protocol and costed pilot (Nov 4–5)

**Implement:**
- [ ] Lock initial model roster with **exact available API model identifiers**; at least one frontier model, ideally two different model families.
- [ ] Fix generation settings, maximum output tokens, timeouts, number of trials and common prompts.
- [ ] Check that API adapters capture raw generations and distinguish transport errors from task errors.
- [ ] Calculate projected token usage/cost using a tiny 1-task dry/pilot run; record estimates and hard stop spending limit.
- [ ] Pilot a small balanced sample across intended models and inspect transcripts for parser/grader ambiguity.
- [ ] Document all task refinements arising from pilots; finalize **benchmark v1 freeze** before main comparison.

**Exit criteria:** Model/provider setup proven with authorized budget; all models receive equivalent instructions; no unaccounted grader ambiguity; frozen prompt/task/grader hashes recorded. **HUMAN DECISION: models, budget, 3 vs 5 trials.**

### M5 — Official benchmark experiments (Nov 5–6)

**Implement:**
- [ ] Run each frozen task on each approved model for ≥3 independent trials.
- [ ] Use fresh isolated context and execution state for every trial; preserve outputs and settings.
- [ ] Collect all outcomes, exceptions, timestamps, usage and run artifacts.
- [ ] Inspect failing transcripts manually; label failure modes without modifying results retroactively.
- [ ] Where an apparent failure may be grader error, separately investigate, resolve, version and **rerun all models consistently** if benchmark changes.
- [ ] Add targeted follow-up experiments only if clearly labeled as **exploratory**, separate from primary pre-specified results.

**Exit criteria:** Complete nonfabricated result table, evidence for every claimed weakness, and stable rerun protocol. At least one representative failure per task **where an actual failure occurred**; if none occurred, disclose it and follow the guide's evidence expectations without inventing one. If required guide expects one failure per task, reconsider including any tasks without limitations but never distort data.

### M6 — Analysis, reliability audit and README (Nov 7)

**Implement:**
- [ ] Compute scores and `pass^k` with exact definitions/denominators; optional `pass@k`.
- [ ] Classify failures as semantic logic errors, boundary errors, implementation errors, formatting errors, or infrastructure errors.
- [ ] Identify meaningful differences among models, near-misses and unexpectedly successful cases.
- [ ] Use grounded transcript excerpts as evidence, with paths to complete transcripts.
- [ ] Report cost, wall time, trial count and any censored runs/errors.
- [ ] Re-run all oracle and negative-control tests; inspect grader false-pass and false-fail risk.
- [ ] Write README sections: problem, domain importance, task summaries, exact setup and run commands, methodology, grading, grader validation, model settings, full result summary and spread, error analysis, provenance, limitations, cost/time and AI-use disclosure.
- [ ] Owner manually audits every task/answer/rule and signs off in `docs/task-review-checklist.md`.

**Exit criteria:** Every headline claim is traceable to an included run, transcript or checked oracle; a skeptical judge can understand failures without trusting the author.

### M7 — Packaging, demo and submission (Nov 8; buffer before deadline)

**Implement:**
- [ ] Confirm HackerRank Instructions tab format, eligibility and participant agreement.
- [ ] Reproduce a clean install/test/run with new virtualenv or container; document all commands.
- [ ] Produce self-contained ZIP **< 50 MB**, with code, small fixtures, reference solutions, graders, README, representative transcripts and final results; exclude video/binaries/cache/secrets.
- [ ] Secret-scan and list archive contents; verify ZIP extracts successfully.
- [ ] Record ≤5-minute demo: ~1 min problem/importance; ~1.5 min task and grader; ~2 min genuine results and failure transcripts; ~0.5 min takeaway.
- [ ] Host video so it opens without login or permission request; test incognito and audio.
- [ ] Write brief project description: domain, actual tested limitation, task count, models tested and headline supported result.
- [ ] Submit ZIP, link and description via HackerRank before the stated deadline; save submission confirmation separately.

**Exit criteria:** Final automated ZIP checks pass; owner confirms successful event submission. **HUMAN ACTION: actual HackerRank submission and access testing.**

## 7. Day-by-day working rhythm

Each Codex session should: (1) read this file and decision log; (2) state the current milestone; (3) implement the smallest verifiable batch; (4) run tests and display actual outcomes; (5) update `docs/progress.md` with done/blocked/next; (6) commit only if approved by owner or repository workflow; (7) stop at an explicit human checkpoint. Do not silently skip validation to meet the date.

At the end of each milestone report:
- **Files changed** and why.
- **Commands run** and real exit status.
- **Tests passed/failed/skipped** (including sandbox constraints).
- **Evidence** (paths to fixtures, oracle, trial records, diffs).
- **Unresolved decisions or risks**, with recommended default.
- **Next small task**.

## 8. Quality assurance checklist and threat model

- [ ] Task instructions specify **every graded behavior**.
- [ ] Two competent domain engineers could independently reach the same expected outcome.
- [ ] All reference implementations pass their graders.
- [ ] Intentionally buggy variants fail their relevant tests; verify no trivial output can accidentally pass.
- [ ] Equivalent correct approaches are not unfairly penalized.
- [ ] Models see neither grader code nor reference answers.
- [ ] Candidate execution has no access to host secrets, network or shared mutable state.
- [ ] Every trial starts clean; no caches/history carry over.
- [ ] Outputs are evaluated for final state rather than particular algorithm choices.
- [ ] Trial config, versions, task hashes and error types are recorded.
- [ ] README commands actually reproduce local mock/oracle checks; real API trials list keys/cost requirement.
- [ ] All datasets are synthetic or licensed and documented.
- [ ] No fabricated model failures, results, transcripts or confidence intervals.
- [ ] Benchmark changes after frozen tests trigger consistent reruns.
- [ ] Human expert review of all task semantics and grader contracts is explicitly logged.
- [ ] ZIP meets event limits and contains the agreed-required deliverables.

**Likely project risks & mitigation:**
1. **Models pass everything:** Add expert-motivated, preregistered realistic interaction cases rather than contrived tricks; report honest successful findings if no limitation remains.
2. **Models fail everything:** Check interface clarity, environment, parsing and oracle validity before treating as capability limitation.
3. **Grader false negatives:** Verify equivalent outputs, precision and record ordering; repair and uniformly rerun.
4. **Grader false positives:** Add adversarial wrong cases and mutation-style tests; ensure checks cover all meaningful constraints.
5. **Unbounded costs:** Pilot first, cap trials/tokens, log usage, stop before budget is exceeded.
6. **Sandbox unavailable:** Block real generated-code execution until isolated sandbox is configured; do not run untrusted code on host.
7. **Not enough time:** Deliver 5 excellent, fully validated tasks instead of 8 incomplete ones; preserve reproducibility/README and demo buffer.
8. **Provider drift:** Record exact model IDs and timestamps; note that provider-side model updates may affect future reproduction.
9. **Data leaks / answer leakage:** Synthetic-only fixtures, strict task/grader separation, secret scan, no hidden labels in prompts.
10. **Misleading comparison:** Same tasks, prompt template, resources, tests and trial counts across compared models; label differences in provider behavior.

## 9. Definition of done

Project is done **only when**:

1. 5–10 independent, original, expert-reviewed realistic tasks exist (8 target).
2. Every task has a validated positive oracle and adversarial negative grader checks.
3. Models are genuinely run through equivalent, documented protocols, including a frontier model and multiple trials/task.
4. Genuine results, model output transcripts and task-level explanations support all claims.
5. A clean-environment reviewer can execute the documented steps and verify main observations, acknowledging that API reruns may incur cost.
6. README documents the full methodological and experimental story, provenance, human review and AI-assistance disclosure.
7. A tested sub-50 MB ZIP, public accessible ≤5-minute video and accurate description are ready for the official submission.
8. Owner has accepted the event terms and actually submitted.

## 10. Initial instruction to Codex — start here, do not implement whole project

1. Read `MILESTONES.md` fully.
2. Summarize the project objective, locked decisions and unresolved human decisions in at most one page.
3. Propose **two clear T01 execution interface alternatives**: (A) pure Python `transform()` and (B) DuckDB SQL. Compare grading reliability, simplicity, model fairness and implementation risk. Recommend one.
4. Create only M0 repository/bootstrap scaffolding, tests and decision/progress documents; do not generate all eight tasks.
5. Run baseline tests; show the real results and the project tree.
6. Stop and ask the owner to select the T01 graded interface before beginning M1. Do not claim an external model is tested at this stage.

---

### Supporting sources

- User-provided *Find What AI Can't Do Yet: A Participant's Guide to the micro1 Eval Hackathon* (2026), notably pages 2–4 (goal and core terms), 9–12 (eval design), 16–17 (rubric), 18–19 (submission materials), 20 (ground rules), and 22 (checklist).
- Official event Instructions tab on HackerRank must be checked at submission time; do not treat this document as a substitute for later official changes.
