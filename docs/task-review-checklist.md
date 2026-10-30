# Task review checklist

No tasks authored or expert-approved at M0. Copy this checklist per versioned task
and record reviewer, date, version/hashes, hand-computed examples and evidence paths.

- [ ] Real business context, engineering difficulty and consequences documented.
- [ ] Every graded behavior stated; two experts can agree on expected results.
- [ ] Schema, keys/tenant scope, ordering/ties, timezone, duplicates, deletes,
      late data, missing/null/invalid behavior and precision explicit as applicable.
- [ ] Normal and nontrivial edge examples manually checked by owner.
- [ ] Independent reference passes grader; expected outputs reproducible.
- [ ] Deliberately wrong candidates rejected for intended reasons.
- [ ] Boundary/metamorphic tests and equivalent correct representations checked.
- [ ] Multiplicity and exact decimals preserved where meaningful.
- [ ] Prompt/runtime cannot access reference, hidden expected outputs or grader.
- [ ] Candidate isolation blocks host secrets/network and cross-trial state.
- [ ] Data provenance/license and original-work disclosure reviewed.
- [ ] Version/hash freeze logged; changes after trials trigger consistent reruns.
- [ ] Actual transcripts inspected; infrastructure failures kept out of accuracy.
- [ ] Owner sign-off recorded (never self-certified by AI).
