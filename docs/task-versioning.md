# Task versioning plan

M0 plan only: no task schema, loader, grader or hash implementation yet.
Use stable IDs t01–t08 and explicit task versions once tasks are authored.
Version the complete acceptance contract: prompt, metadata, visible and hidden
fixtures, oracle and grader. Record Git SHA and stable content hashes of those
components, plus rendered prompt hash, in every future run manifest.

Keep model-visible files under tasks/ and reference and grader implementations
under separate reference/ and graders/ directories. Only explicitly allowlisted
visible files enter prompts or candidate runtime; directory proximity is no access
boundary. Hidden fixtures and expected answers stay evaluator-side.

Log changes with date, rationale, reviewer, old/new versions and affected runs.
Never overwrite historical trial artifacts. Mark development/pilot/exploratory
runs separately. Freeze v1 before primary comparisons. Any graded semantic,
fixture, prompt or grader change requires a new version and rerunning all
compared models consistently; retain superseded runs as historical evidence.
