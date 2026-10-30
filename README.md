# PipelineIntegrityBench

A planned benchmark of whether AI-generated data transformations preserve explicit
integrity rules under CDC, late events, duplicates, schema changes, replay and tenant
boundaries. These failures could silently corrupt downstream operational decisions.
The hypothesis is untested: no benchmark tasks, model runs or findings exist yet.

Current stage: M0 bootstrap. [MILESTONES.md](MILESTONES.md) is the specification.
T01 artifact selected by owner: DuckDB SQL; Python 3.11 remains the harness
language. M0 review is pending before M1 implementation.

## Setup and local verification

Install CPython **3.11.11** (see `.python-version`), Git and pip. From a clean clone:

```bash
python3.11 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.lock
python -m pip install --no-build-isolation --no-deps -e .
python -m pytest -q
python -m ruff check .
python -m ruff format --check .
python -m pip check
```

On Windows, activate with `.venv\Scripts\activate`. Initial installation needs
network access; tests and lint run locally without API credentials. M0 has no
runtime dependencies. Tooling and its transitive dependencies are pinned in
`requirements.lock`; the build backend is pinned in `pyproject.toml`.
The smoke test checks the installed package in a fresh isolated interpreter.
M0 tests take seconds and incur no model API costs. Full-evaluation runtime and
cost are unknown until an authorized pilot. No CLI commands are implemented yet.

## Method and review status

See [methodology](docs/methodology.md), [decisions](docs/decision-log.md),
[task review checklist](docs/task-review-checklist.md),
[task versioning](docs/task-versioning.md), and [progress](docs/progress.md).
No generated candidate code may run until a restricted sandbox exists.

## Submission status and provenance

Video walkthrough: pending (publicly accessible, with audio, at most 5 minutes).
Domain: data engineering; owner expertise and review statement pending.
Models tested, exact settings, results and failure analysis: not available; no
model has been tested. Task/grader validation begins in M1.

The supplied project charter and participant guide are source materials present
before this implementation. Existing benchmark tasks/data have not been copied.
Future fixtures must be synthetic or properly licensed. Public benchmark examples
in the guide inform methodology only. Third-party tools retain their own licenses;
project license remains an owner decision before distribution. The supplied PDF's
redistribution permission is unverified; exclude it from the submission unless cleared.

AI assistance: Codex drafted the M0 packaging, smoke test and documentation.
Owner review is pending; no human task or grader sign-off is claimed.
The owner must accept the participant agreement and verify the live HackerRank
Instructions tab. Final delivery requires a ZIP under 50 MB, real run artifacts,
a public video link and short description. This repository is not submission-ready.
