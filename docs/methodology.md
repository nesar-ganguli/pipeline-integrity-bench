# Methodology and event requirements

Status: M0, 2026-10-30. Read all 22 pages of the supplied
`Eval_Hackathon_Participant_Guide.pdf` and all three supplied screenshots.
The live HackerRank Instructions tab is authoritative; independent verification
of its current fields and any changes is **pending**. Screenshots lack a complete
participant agreement and do not resolve that action.

## Objective and locked design

Measure preservation of explicit data-pipeline semantics, not syntax alone.
Target eight original tasks, allowing 5–10 high-quality tasks. Use Python 3.11,
small synthetic UTF-8 CSV/JSON/JSONL, explicit time zones and exact financial
arithmetic. Owner selected DuckDB SQL as the T01 graded artifact on 2026-10-30, replacing
the provisional Python function contract. Python remains the harness language.
The pinned SQL engine and table/result contract will be defined in M1.
Use deterministic outcome grading, independent references and negative controls.
Keep prompts/fixtures separate from graders/oracles. A local subprocess alone
is insufficient for hostile generated code: real trials require restricted
sandbox/container execution with no secrets/network and ephemeral state.
Use a Python CLI later, independent trials, JSONL raw records, CSV summaries and
saved transcripts. No frontend and no LLM grader for primary correctness.
These are project choices, not mandated event execution formats.

## Guide requirements and recommendations (page references)

- Pages 2–4, 9: individual original eval grounded in expertise, a real limitation,
  unambiguous success criteria; approximately 5–10 tasks is a recommendation.
- Pages 9–12, 22: a reference solution for every task must pass its grader;
  deliberately wrong answers must fail. Every graded condition must be in the
  prompt. Accept equivalent correct outcomes and keep reference answers hidden.
- Pages 10–11: prefer code grading. LLM judges, if ever added, need specific
  rubrics, a different model family, expert calibration and repeatability checks.
  Partial credit is optional. No required target pass rate; investigate universal
  failure and recognize limited headroom when strongest models approach 100%.
- Pages 11, 17, 22: test at least one frontier model with multiple independent
  trials per task; 3–5 is recommended. Record exact model versions, settings,
  dates, spread, approximate cost and runtime; keep every trial state clean.
  Distinguish at-least-one success (`pass@k`) from all-trial success (`pass^k`).
- Pages 12, 18–19: read failing transcripts, explain actual errors, include
  representative transcripts for each reported model. Page 18 explicitly asks
  for at least one failure per task; page 19 asks for at least one near-miss task.
  If no genuine failures occur, report success honestly and seek clarification
  or reconsider task inclusion; never fabricate or cherry-pick claimed evidence.
- Pages 12, 17, 20, 22: owner must review every task, reference and grading rule;
  disclose AI contributions and how they were reviewed. Use original work,
  disclose prior work/adaptations, respect tool/data licenses and terms.
- Pages 3, 18–20, 22: submit through HackerRank: ZIP code and small support files,
  maximum 50 MB (project gate: strictly under 50 MB), root README, video link
  at most 5 minutes, and short written description. No video inside ZIP.
  Exclude credentials, confidential/client/employer data and private information.
  Provide dependencies and `.env.example` variable names without credentials.
- Pages 18–19 and screenshots: README needs short description, public video link,
  domain/expertise, capability and importance, task overview, scoring and grader
  validation, clean setup/run instructions and key supply, runtime/cost, exact
  models/settings/dates/trial counts/scores/spread, failure analysis, provenance,
  limitations, AI disclosure and links to transcripts. Include tasks, expected
  answers/criteria, scoring logic, actual raw outputs and scores in the ZIP.
- Pages 19, 22 and screenshots: video must open without requesting access and
  play with audio. No face required; AI voice permitted. Description appears in
  submission fields and README. Latest complete upload counts; one submission
  per participant. Owner must personally accept the participant agreement.
- Pages 6–8, 18: Harbor and its illustrated layout are optional; follow the final
  event format, not an assumed mandatory sample structure.
- Page 3: deadline November 9, 2026 at 05:15 GMT = November 9, 12:15 AM
  America/Indianapolis (November 8, 9:15 PM Pacific). Winners: November 23, 2026.

## Judging priorities (pages 16–17)

Eligibility, completeness, integrity and reproducibility checks precede scoring.
Task design 20; grader reliability 20; real-world relevance 15; evidence of
limitations 15; reproducibility 15; human expertise/review 10; insight 5.
No empirical claim is made in M0. Full protocol, task semantics and results
will be developed only at their prescribed gates.
