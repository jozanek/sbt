# sbt/sbt review checklist (project-specific)

last-verified: 2026-10-18
Sources: CONTRIBUTING.md and LLM_POLICY.md (upstream #9807, 2026-09-22); AGENTS.md;
contributing-docs/03-05; a read-only review sweep of 48 merged and 19 closed-unmerged PRs (Mar to Oct 2026)
plus all 11 of my PRs; 3 reverts (#8464, #8730, #9060). Counts are approximate (the sample is a paged walk,
not random). Re-mine quarterly with `tools/mine-reviews.sh`.

How to use: the fresh-context reviewer cites these IDs. Each rule says what failure looks like, which
local check catches it, and what that check misses. "Mine" counts maintainer corrections on my own PRs.
A rule that fires on me twice is a repeated correction, and the metric for that should be zero.

Order is by how often maintainers raise it, not by how easy it is to check.

## A. Should this exist (decide before code)

**C01 Wanted first.** Failure: weeks of work closed as "by design" or "is there an open problem?".
Evidence: LLM_POLICY requires maintainer confirmation before a PR; #9720 (mine, 23 days, closed: by design);
#9541, #9627. Mine: 1.
Check: Stage 3 gate. Link the confirming comment in the PR's reviewer notes.
Misses: priorities change. A 2014 or 2017 maintainer comment is not a current "yes" (#1361, #1224).

**C02 Reuse before adding.** Failure: a new key, command, flag, option, parser or println where an existing
one could be extended. This is the most common maintainer concern (about 14 PRs: #9051, #9689, #9623, #9337).
Mine: 4 (#9442 new key dropped; #9434 single-dash option rejected; #9619 use `IO.copyFile`; #9720 command
not wanted).
Check: the PR text names the existing mechanism considered and why it is insufficient. Any added line in
`Keys.scala`, a new `Command`, or a new launcher option means Stage 3 (maintainer decision).
Misses: an existing helper you don't know about. Run `git grep` for the verb (copy, parse, resolve) before writing one.

**C03 One concern; "bug fixes only".** Failure: asked to split, or to drop unrelated changes (about 12 PRs:
#9515, #9353, #9627). Mine: 3 (#9799 split into #9814; #9434 trimmed from +595/-152; #9347 unrelated change).
Check: for every hunk, one line on which part of the Problem it serves. Any hunk that serves none gets split
out. `tools/size-check.sh`.
Misses: refactors that feel necessary. Ask first, or land them as a separate PR first.

**C04 Size.** LLM_POLICY: "small (both scope and lines of change)". Merged outside PRs since 2026-01:
non-test lines p50 19, p75 62, p90 137; test lines p50 28, p75 76. Above p75, the PR says why. Above p90,
split, or get an explicit OK. Test volume costs review time too, so prefer one decisive test over five.
Mine: non-test 17-304, test 30-460; #9814 had 139 non-test and 460 test lines.

## B. Evidence

**C05 Reproduction evidence.** "How would we know it's fixed?" (about 7 PRs: #9147, #9102, #9725, #9720).
Check: `reproduce.sh` verdicts before and after, in the PR. For performance claims, give numbers and a method a
maintainer can rerun (#9253 waited 22 days for a maintainer reproduction).
Misses: a repro that matches a different failure. Match the issue-specific output fragment, not the exit code.

**C06 Right kind of test.** New unit tests use HedgeHog (preferred) or Verify, not ScalaTest (#9226). Use a
scripted or end-to-end test when behaviour crosses tasks, files or processes (#9448, #9725). Don't guard away
the route the test should exercise, e.g. an `isWindows` skip (#9766).
Check: reviewer. `git diff` for `extends AnyFunSuite|FlatSpec` in new test files.
Misses: tests that pass for the wrong reason. Hence C07.

**C07 The test fails first, for the same reason.** Show its failure output on `develop @ <sha>`.
Check: S4 gate. Misses: flaky failures that look like the bug. Run the failing case 3 times.

## C. Compatibility and surface

**C08 Minimal public surface.** New helpers are `private[sbt]` or under `sbt.internal`. Not in `Defaults.scala`
(#9293, #9793; #9864 qualified-private to public). Don't expose external-library types (03_coding_style).
Check: reviewer greps the diff for new `def`/`val`/`class` without `private`.
Misses: package-private visibility leaking through public signatures.

**C09 Binary compatibility.** Existing public implicits and methods can't be removed (#9347: `richTaskSeq`,
mine). Check: `mimaReportBinaryIssues`.
Misses: MiMa checks JVM signatures only. It does not catch behaviour, default values, source compatibility,
or semantic changes to existing keys.

**C10 Behaviour change, even when fixing an old bug.** Long-standing behaviour has users. Examples: #9722
(mine; a bug from about 2013, and "the fix could change build semantics"), #9442 (mine; test cwd kept, change
scoped to `run`), #9344 (mine; default flip, documented in notes). Check: the PR says who might depend on the
old behaviour, with a `notes/<next>/*.md` entry (and `migration.md` if applicable), and the change is raised in
Stage 3. Misses: plugin authors. Only the community build (CI job 13) samples them.

## D. Correctness patterns reviewers found

**C11 Edge cases sbt reviewers ask about.** Empty match still running tasks (#9722); dedupe across
Compile/Test losing information (#9102); duplicate keys (last wins) and ambiguous separators (#9685);
side effects inside predicates like `exists` (#8880); types that match existing APIs (#9353 Long job id).
Check: the test matrix in the item file lists empty, duplicate, multi-config, aggregate and cross-build cases,
or says why each is not applicable. Misses: interactions with plugins and custom configurations.

**C12 Platform.** Windows paths with spaces, file locking, Git Bash, CRLF, APFS (#9047, #9448, #9623,
#9434; revert #8730). Check: fork CI includes Windows jobs 10 and 12.
Misses: the matrix runs pwsh and Linux shells. Git Bash, macOS APFS and JDK-specific client paths are not
exercised (see C15).

**C13 Performance.** No unbounded filesystem walks on hot paths (#9870). Don't reverse a deliberate
performance decision without data (#9725). Claims need reproducible numbers (#9253). Misses: everything
without a benchmark. Say so in the PR instead of claiming.

**C14 Security.** Diagnostics and logs must not print secrets, e.g. `-D` values or credentials (#9685).

## E. Process

**C15 Real-session smoke test for launcher, client/server, clean or boot changes.** All three recent
reverts had fully green CI: #8464 (sbtn on JDK 17), #8730 (Git Bash `.jvmopts`), #9060 (same-session
`cleanFull`). Check: run the changed path in a real interactive session through `sbt`/sbtn with
`publishLocalBin`, on JDK 17, and record it in the PR. Misses: platforms you don't have.

**C16 Branch.** develop is 2.1.x. Backports to 2.0.x are slowing after regressions, and 1.12.x has no more
releases (#9903, #9515, #9623). Don't open backports unless a maintainer asks.

**C17 CI green before review, on the merge with current develop.** Diagnose every red job before asking for
review, or before waiting. #9744 (mine) sat 37+ days unreviewed with job 1 red: `scalafmtCheckAll` failed on
`Load.scala` in the upstream merge run, while fork CI on the unmerged branch was green. Before the fork-CI run
that counts, merge upstream/develop and run `scalafmtAll`. Jobs time out at 25 minutes, so a slow new scripted test can
push a job over (#9864). Infra failures (e.g. HTTP 403 from Maven Central before tests ran) justify one re-run.
"Flake" is not a diagnosis.

**C18 Disclosure.** AI disclosure in the PR body, plus `Generated-by:` at the end of part 1 so it survives a
squash merge (LLM_POLICY; AGENTS.md). Mine: missing on #9744, #9728, #9434. No maintainer objected to
disclosed AI use in any sampled thread.

**C19 CLA signed** (#9364, #9147). Done for me; keep it in the checklist for other repos.

## F. Code conventions (enforced partly by tools, rarely raised in review)

**C20 Style.** Fewer-braces syntax for new code, end markers, no `return` (scalafix DisableSyntax), `Using`
over try-finally, no infix for non-symbolic methods (#9293), Option over null, Scala collections over Java
ones. Check: `scalafmtCheckRepo` (scalafmt applies some Scala 3 rewrites; see `.scalafmt.conf`), scalafix,
reviewer. Note: the sweep found no maintainer comments on braces, end markers, `return` or `Using`, likely
because tools and authors already handle them (inferred).

**C21 Comments.** No inline comments (AGENTS.md). Add a short "why" only when the code would otherwise
mislead (#9041). Keep Scaladoc short (#9870).

**C22 Names and user-facing text.** Match existing output style (lowercase, verb form; #9295). Drop output
users can't act on (#9337). Remove unused vals (#9901). PR title type must be accurate; "refactor" for a
behaviour change misleads (#8866).

**C23 Generated and boilerplate files.** Contraband: run `generateContrabands` (CI job 11 diffs it). New
files: Apache header via `headerCreate` (CI does not check it). Hermetic tasks: no absolute paths or
timestamps in outputs (03_coding_style). Don't duplicate content that already lives in contributing-docs
(#9353).

---

## Rule log (append; never delete, mark retired)

| Date | Rule | Change | Source (PR/comment) | Precision note |
|---|---|---|---|---|
| 2026-10-18 | C01-C23 | created | sweep above | baseline |
