# How things are usually done in sbt/sbt

last-verified: 2026-10-18
Rule for adding an entry: 2+ examples in code or review, with anchors or links. Otherwise it goes to open-questions.md.

## Branches and PRs
- Fix bugs against `develop` (2.x; currently the 2.1.x line). Backports target `1.<minor>.x` or `2.0.x` only when asked. Source: CONTRIBUTING.md; #9515, #9903.
- Commit subject: `[2.x] <type>: <Imperative>`, with type one of fix, feat, refactor, test, ci, deps (also perf and docs in practice: 21 perf commits since 2025-10). Body: **Problem** / **Solution**. `Generated-by:` trailer. Source: CONTRIBUTING.md; git log (602 of 610 recent tagged subjects use `[2.x]`).
- Maintainers merge with merge commits and squash merges both (563 merges and 1,463 non-merge commits since 2024-06 on develop). Keep a reviewable commit history during review.
- User-visible behaviour or default changes ship a `notes/<version>/<topic>.md` entry (e.g. `notes/2.0.0/fork-working-directory.md`, `patterns-maven-compatible-default.md`) and, for migrations, `notes/2.0.0/migration.md`.

## Tests
- Unit: HedgeHog preferred, Verify acceptable, not ScalaTest for new tests. Source: 04_unit_tests.md; #9226.
- Scripted: `sbt-app/src/sbt-test/<group>/<name>/{build.sbt,test,changes/}`. Issue regressions are named `i<issue>-<slug>` (e.g. `project/i1210-run-aggregated`, `actions/i1095-dynamic-reference`). In scripted builds, test keys are `@transient lazy val check = taskKey[Unit]("")`. Source: 05_scripted_tests.md, 03_coding_style.md.
- 33 scripted tests carry a `pending` marker (2026-09-17). They are skipped; see open-questions.md.
- CI jobs (ci.yml): job 1 runs MiMa, javafmt, scalafmtCheckRepo, Test/compile, doc, publishLocal, test, serverTestProj/test; jobs 2-5, 7 and 12 run scripted groups; 10 is lm-coursier (Linux and Windows); 11 contraband; 13 community build. 25-minute timeout per job.

## Repro conventions
- The project ships `.agents/skills/sbt-issue-fixing/SKILL.md`: one folder per issue under `local-temp/issues/<id>-<slug>/` with README.md, reproduce.sh (bare and `--direct` modes, isolated caches, `REPRODUCED: yes|no`), build.sbt. `local-temp` is git-ignored upstream.

## Code
- Public surface minimal: internals in `sbt.internal.*`, helpers `private[sbt]`, keep helpers out of Defaults.scala. Source: 03_coding_style.md; #9293, #9793.
- Keys via the `settingKey[A]`/`taskKey[A]` macros, with `.withRank(...)`. Source: Keys.scala; 03_coding_style.md.
