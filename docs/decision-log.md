# Decision log

No owner approvals are inferred from defaults. Dates use America/Indianapolis.

| Date | Choice/status | Reason and alternatives | Impact on prior runs |
| --- | --- | --- | --- |
| 2026-10-30 | M0 only; existing Git repo retained | User authorization and charter; no need to reinitialize | None; no model runs |
| 2026-10-30 | CPython 3.11.11; setuptools src layout; no runtime deps | Charter locks Python 3.11; pin patch for repeatability; Python 3.14 host not used for acceptance | None |
| 2026-10-30 | pytest 8.3.5 and Ruff 0.11.13 pinned | Small auditable toolchain; Ruff covers formatting and lint instead of separate Black | None |
| 2026-10-30 | No commit made | Charter section 7 requires owner approval or repository workflow; no such approval found | M0 diff awaits review; clean-commit criterion pending |
| 2026-10-30 | PDF excluded from eventual ZIP unless permission cleared | Supplied guide is evidence, redistribution rights unknown | None |

## Approved T01 artifact decision

Owner selected **DuckDB SQL** explicitly in chat on 2026-10-30, replacing the
charter's provisional Python function artifact. Python 3.11 remains the harness
language. T01 will grade DuckDB SQL results under a pinned engine and explicit
input-table/output-schema contract. Engine version, SQL statement restrictions,
ordering/NULL/type conventions and isolation details will be defined in M1.
The owner's selection is the rationale; no additional motivation is inferred.
Alternative considered: Python `transform(inputs)` (simpler invocation).
Impact on prior runs: none; no tasks or model runs exist. Keep subsequent
comparisons on the same approved artifact contract; do not mix languages.

## Pending owner gates

- M1: artifact choice resolved as DuckDB SQL; first-slice semantics/output
  review remains pending. Custom CLI default; Harbor optional.
- M2/M3: hidden fixture policy, optional explanation, partial credit, secure runtime.
- M4: exact model IDs/families, budget and runtime caps, trial settings/count.
- M5: task count, freeze and any additional trials/difficulty revisions.
- M7: license/public release, video host, agreement and actual submission.
- Now: owner review of M0 and authorization for logical bootstrap commit.
- Event: verify live Instructions tab; clarify failure-per-task expectation if
  actual trials all pass. No paid trial or sandbox execution authorized by M0.

## T01 alternatives for M1 review

| Criterion | A: Python `transform(inputs)` | B: DuckDB SQL |
| --- | --- | --- |
| Grading | JSON records permit semantic/schema/multiset checks | Query rows permit the same checks; explicit NULL/type/order rules needed |
| Simplicity | Standard library, no engine dependency | Pin DuckDB, define tables and SQL submission contract |
| Model fairness | Same Python interface for all; measures transformation logic | Same SQL dialect for all; more directly measures SQL generation |
| Risk | Function extraction and safe code execution required | SQL parsing, engine conventions and file/extension access restrictions required |

The initial recommendation was A for simplicity; the owner selected B.
Neither option is implemented. SQL needs a restricted execution boundary.
