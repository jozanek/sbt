# Maintainer decisions (and why)

Never pruned; mark superseded entries. Each needs a link. Paraphrased; check the link before relying on one.
These are seeded from the 2026-10-18 sweep; verify each when you first rely on it.

| Date | Decision | Rationale given | Link | Status |
|---|---|---|---|---|
| 2026-09 | sbt should not support remote SNAPSHOT plugin auto-update; no special `updateGlobalPlugins` command | non-snapshot plugins not auto-updating is by design | sbt/sbt#9720 | current |
| 2026-08 | `-java-home` single-dash form not supported in sbtw; keep #963 work to bug fixes | minimize to bug fixes | sbt/sbt#9434 | current |
| 2026-07 | forked `run` inherits sbt's cwd; test cwd stays the subproject; no new key | test cwd has been the subproject for so long that changing it could break builds | sbt/sbt#9442 | current |
| 2026-08 | `richTaskSeq` is public API; can't remove implicits; use an extension method instead | binary/source compatibility | sbt/sbt#9347 | current |
| 2026 | develop targets 2.1.x; 2.0.x backports are slowing after regressions; performance work lands on develop only | regressions in backports | sbt/sbt#9515, #9623, #9448 | current |
| 2026-10 | no more 1.12.x releases | n/a | sbt/sbt#9903 | current |
| 2026-09 | removing the launcher boot dir in `cleanFull` was "probably too much"; reverted | breaks running session | sbt/sbt#9747 | current |
| 2026-09-22 | LLM policy split into LLM_POLICY.md: disclose all AI use; stricter enforcement for AI-assisted PRs; small PRs in scope and lines; confirm wanted first | maintainer bandwidth | sbt/sbt#9807 | current |
