# Fresh-context reviewer: calibration, 2026-10-20

Setup: the `sbt-fresh-reviewer` prompt (model opus), round 1, on 5 commits from local history. Each case was
checked out detached at its own commit, so later history (the reverts) was not visible from HEAD. The commit
message stood in for the PR draft.

## Run 1 (contaminated; not scored)
The reviewer read `checklist.md`, which names #8464, #8730 and #9060 in C12 and C15. All three revert reviews
quoted those notes, so the answer leaked. **Lesson:** run evals against a checklist copy with the eval cases
removed. (Now in OPERATING-MODEL.md S5.)

## Run 2 (blind checklist: revert references removed, generic rules kept)

| Case | Ground truth | Reviewer's top finding | Verdict | Score |
|---|---|---|---|---|
| #9060 cleanFull deletes boot dir (reverted, about 5 months later) | running session breaks: later update/reload use deleted boot jars | Important: deletes the running session's own sbt/Scala jars, then continues; `update` substitutes deleted Scala jars; reuse `reboot full` | no | **hit, exact mechanism** |
| #8464 musl/NIO sockets for sbtn (reverted, about 2 days later) | sbtn could not connect to the server on JDK 17 (maintainer's suspected cause: the JDK 17 SocketChannel path; unconfirmed) | Important: on JDK 17/18 the NIO stream adapters share `blockingLock()`, so full-duplex traffic deadlocks; also an NPE on server shutdown, a 50 ms accept polling loop, and a silent default switch for every server | no | **hit, same class** |
| #8730 quote-aware dot-file parsing (reverted, about 9 days later) | Git Bash on Windows: "Invalid maximum heap size: -Xmx2G" (root cause unconfirmed upstream) | Important: multi-option `-J` lines regress; quote characters stay in values; `.jvmopts` no longer suppresses the default opts; tests pass on the old code | no | **blocked with real regressions; reported failure not identified** |
| #9250 dependencyMode internal deps (merged, bare approval) | no known problem | 3 Important: user additions to `dependencyClasspath` dropped in Direct/PlusOne (plausible, unverified); a pre-existing self-classpath gap mislabelled Important; commit-message process (artifact) | no | **false block** |
| #9271 missing-file error message (merged, bare approval) | no known problem | 1 Important: unit tests build the exception chain by hand and don't drive the real path (fair, but beyond the maintainer's bar) | no | **false block** |

Contaminated run 1 on the clean cases is the same as above (clean cases were not named in the checklist).

## What it means
- **Recall on real problems is good:** 2 of 3 reverts were caught at the mechanism level, blind, and the third
  was blocked with genuine regressions.
- **The merge verdict doesn't discriminate:** it said "would not merge" on all 5. Severity is calibrated above
  eed3si9n's bar. An agent author that "fixes" every Important will grow PRs, and C03/C04 (scope, size) are your
  top repeated corrections.
- **Findings do discriminate by type.** Revert cases had Important findings of *concrete breakage in default
  or documented configurations*. Clean cases had edge cases, test strength, and a misfiled pre-existing problem.
  The rubric change below encodes that difference.
- **Eval artifacts:** commit messages aren't PR descriptions. Process findings (disclosure, Problem/Solution) on
  #9250 were wrong: its PR body had a disclosure, a scripted test and a MiMa note.
- **Cost:** about 115-160k tokens per review on opus, about 1.06M across 8 runs. Three opus rounds per PR would
  be about 350k tokens. The account's 7-day usage limit showed a warning during this run.

## Changes made (not yet re-validated; re-run when the weekly limit resets)
1. Severity rubric in `install/agents/sbt-fresh-reviewer.md`. Important only for (a) concrete breakage in a
   default, common or documented configuration, with the scenario; (b) a policy MUST (no test at all, bincompat
   break, missing disclosure in the PR draft); or (c) a C01-C04 concern. Everything else is Nit or "Above the bar".
2. "Pre-existing" means present in the parent commit, and is never Important.
3. Process findings are judged on the PR draft (PR.md) only.
4. "Would merge" is replaced by a three-way verdict: ready / ready after Important fixes / reconsider.
5. Cost: opus for round 1; rounds 2-3 (diff-only) on sonnet.

Expected on re-run: the 3 reverts keep their breakage findings as Important; the 2 clean cases come back with no
Important findings. If not, iterate on the rubric, not the cases.
