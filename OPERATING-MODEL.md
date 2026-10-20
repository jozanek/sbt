# Operating model: contributing to sbt/sbt from outside, agents on the loop

For: Jozef Koval (`jozanek`). Prepared 2026-10-18.
Evidence base: the local clone (develop @ 2ef94e08, 2026-09-17), your fork's branches and CI runs, upstream's
new CONTRIBUTING.md and LLM_POLICY.md (from #9807, visible on your `fix/9813-publish-overwrite` branch), a
read-only sweep of 48 merged and 19 closed sbt PRs plus all 11 of yours, a work-discovery sweep of the issue
tracker (section "Step 2"), and the Claude Code team's review article. Each claim is observed unless marked
*inferred*.

How to read: section 0 is the Step 0 report. 1 is the one-page flow, 2 the per-stage spec. Then Steps 2 and 4-7.
Then rollout (4) and assumptions (5). Section 6 has questions to check your own understanding before you adopt
this. The files you install are under `install/`, `templates/` and `notes-skeleton/`; see README.md.

---

## 0. Step 0 report

### 0.1 What sbt is, structurally
- Scala 3 (2,131 .scala files; 823 .sbt), plus small amounts of Java and shell. About 109k lines of main
  Scala and about 27k of unit tests, plus 676 scripted integration tests in 25 groups (33 marked `pending`).
- The core is `main/` (40k lines: Defaults, Keys, Load, Extracted, server/BSP). Then come `protocol/`
  (largely generated), `internal/util-*`, `lm-core/` (library management), `main-command/`, `main-settings/`
  (the settings/task DSL), `lm-coursier/`, and `util-cache/` (action cache). sbt/io and sbt/zinc are separate repos.
- Branches: `develop` is 2.x (the 2.1.x line now). `1.<minor>.x` is stable 1.x. 2.0.x backports are slowing
  after regressions, and there are no more 1.12.x releases.
- CI (`.github/workflows/ci.yml`): 11 jobs, a 25-minute timeout each. Job 1 runs MiMa, javafmt,
  scalafmtCheckRepo, Test/compile, doc, publishLocal, test and server tests. Jobs 2-5, 7 and 12 run
  scripted groups; 10 is lm-coursier on Linux and Windows; 11 regenerates Contraband and diffs it; 13 is a
  community build. Header checks are commented out, so CI does not enforce file headers.
- No CODEOWNERS, no PR template, and no CODE_OF_CONDUCT in the repo. Maintainers squash-merge or
  merge-commit. Contributors sign the Scala CLA.
- The project ships agent tooling. `AGENTS.md` (to which `CLAUDE.md` is symlinked) has the agent
  rules. `.agents/skills/sbt-issue-fixing/SKILL.md` fixes the shape of a reproduction: `local-temp/issues/<id>-<slug>/`, two
  modes, isolated caches, a `REPRODUCED: yes|no` verdict. Upstream's `.gitignore` already ignores `.claude/` and
  `local-temp`. Maintainers expect contributors to run agents locally.

### 0.2 Rules that bind you (current as of upstream #9807, 2026-09-22)
- **Start with a conversation.** "Before creating a pull request to sbt, start a conversation", and
  confirm with a maintainer that a contribution is wanted. The new CONTRIBUTING moved this to the top.
- **LLM_POLICY.md** (new file): human-in-the-loop verification ("actually run sbt"); disclose all AI use in
  the PR description; "we will likely enforce the contribution guidelines more strictly for AI-assisted
  contributions"; small PRs "both scope and lines of change"; you must understand all generated code.
  Untested, unexplainable, copy-pasted AI PRs get closed and the user blocked.
- AGENTS.md: put `Generated-by:` in the commit message; always add tests (HedgeHog preferred; scripted for
  file/task coordination); fewer-braces syntax; prefer `Using`; no inline comments; never break binary
  compatibility (MiMa).
- Reproduce before you fix; show that the fix works (tests, or screenshots/screencast of a manual run).
- What changed since your local copy: the "Gittensor bounties" paragraph is gone, replaced by a general
  bandwidth statement; the AI section moved to LLM_POLICY.md and got stricter on size and enforcement.
  Your fork's develop (2026-09-17) predates this. Sync it before relying on any local copy of the docs.

### 0.3 What reviewers actually care about (sweep, Mar to Oct 2026)
Ranked by how often a maintainer raised it (approximate counts, paged sample):
1. **Reuse, don't add** (about 14): extend the existing parser, setting or helper; no new key, command or flag.
2. **Scope** (about 12): "minimize the change to just bug fixes", split unrelated work.
3. **Correctness found in review** (about 9): empty cases, Compile/Test conflation, duplicates, side effects.
4. **Tests** (about 9): missing, weak, or wrong kind (ScalaTest instead of HedgeHog/Verify; unit where end-to-end was needed).
5. **"Is there an issue or open problem?" / superseded** (about 7).
6. **Reproduction evidence** (about 7): "how would we know it is fixed?"
7. Public surface (`private[sbt]`) (6), branch/backport (6), platform (5), performance (5), naming/UI (4),
   style (4), compatibility (3-4), release notes (3-4), CI/CLA (3).

What they did **not** raise in the sample: braces, end markers, `return`, `Using`, commit-message format,
AI use when it was disclosed. Tools and diligent authors cover those (*inferred*). So the checklist ranks
judgement concerns first and style last, the opposite of how easy each is to check.

All three recent reverts (#8464 sbtn on JDK 17, #8730 Git Bash `.jvmopts`, #9060 same-session `cleanFull`)
had fully green CI. Each broke a path the CI matrix doesn't exercise. That is the main limit of
"CI green": it says nothing about launcher, client/server or session behaviour on real machines.

### 0.4 How responsive maintainers are
- One lead (eed3si9n) reviews and merges nearly everything. anatoliykmetyuk does the deepest correctness
  reviews on some PRs. Their attention is a single queue, and your PRs compete in it.
- Time from open to first maintainer response for outside PRs: median about 13 hours, p90 about 5-7 days
  (small n, *inferred* from pooled samples). Small, well-described PRs often get a bare "Thanks!" approval
  within a day (about 15 of 48).
- Stuck PRs moved after a polite nudge around day 16-22 (#9253, #9337, and your #9434 and #9347).
- Closed-unmerged PRs were mostly superseded, often by a maintainer's own alternative that kept the contributor's
  test. None in the sample was closed for "AI" or "CI failing". The policy text threatens both.

### 0.5 Your position today, plainly
- 11 PRs: 7 merged, 3 open, 1 closed by you as "by design" (#9720, 23 days of work).
- **Open:** #9799 (scripted publishing isolation; green upstream; waiting 26 days after you split #9814 out at
  the maintainer's request). #9744 (`initialProject`; 37 days, no review, **upstream job 1 red** although your
  fork CI on the same SHA was green; adds a public key; no AI disclosure). #9619 (Windows dirzip;
  changes-requested 8/17; you switched to `IO.copyFile` and replied 9/1; no response for 47 days).
- **Repeated corrections already present:** "reuse, don't add" four times (#9442, #9434, #9619, #9720) and
  "scope/split" three times (#9347, #9434, #9799). These are the project's top two concerns, so the checklist
  puts them first.
- **Disclosure gaps:** #9434, #9728 and #9744 have no AI disclosure in the description. None of your 6 squashed
  commits carries a `Generated-by:` trailer. LLM_POLICY says "all AI usage in any form must be disclosed".
- **Size:** your non-test lines (17-304) mostly sit at or above the outside-contributor p75 (62). #9434
  (304) and #9814 (139) exceed p90 (137). Your tests are large too (30-460 lines; others' p75 is 76).
- **Understanding:** by your own assessment you could defend "few" of your merged PRs line by line. Under the
  current LLM_POLICY, that is the biggest risk to your reputation goal. It also means "you land it,
  you own it" would be hard today if one of them regressed.
- **Fork state:** your fork's develop is a month behind upstream. Fork CI (96 runs) works, and a recent red
  run on `fix/1361` was infrastructure (Maven Central HTTP 403 while downloading a jar, before any test ran).

### 0.6 Where I adapted the article, and why

| The article's reasoning | Your situation | What this model does |
|---|---|---|
| Humans stay in the loop for "should we build this?". Even a team that removed review kept it for changes from outside the team | You are always the outside team. sbt's policy makes "wanted?" a precondition | Stage 3 is mandatory before code for every PR, and is the earliest maintainer touchpoint, not a surprise on a finished PR |
| Closing a PR "doesn't feel like a loss" because the code was cheap | For you, a closed PR still costs a maintainer's reading time and some reputation, and the policy threatens blocking | Make exploration cheap before the PR (private repro, private prototype, a closed question on the issue). The PR comes last |
| The change sets the risk tier; trusted authors get lighter paths | You have no trusted path; every PR gets eed3si9n's eyes | Autonomy is per area and earned by evidence (Step 5). Ceilings for public API, defaults, CI and launchers mirror the article's "sensitive paths always need a person" |
| AI review and required CI run on every PR in the team's infra | You can't add bots or gates to sbt | Your required CI is local gates plus **fork CI on the same SHA, after syncing upstream develop** (the article's merge-queue point: your fork's push run on #9744 was green while the upstream PR run was red) |
| `REVIEW.md` is written by code owners | You aren't an owner, and must not add files | `checklist.md`, mined from their comments, lives outside the repo; the fresh-context reviewer cites it |
| Noise is measured by how authors respond; incidents become an eval set | Same problem at small scale | You record a verdict on every self-review finding (reviewer precision). The eval set is the 3 reverts, 5 clean merged PRs, and your corrected PRs (Stage 5) |
| Convergence: a round cap of 3, diff-only re-review, bug classes, no repeats | Same (your principle 8) | Same, plus a cap on maintainer rounds: at 3, stop and ask whether the approach is wanted |
| Learning: ask for an explainer of the slice; nobody holds the whole model | You need the model, and your explainability is low today | The agent gives a map, not the answer. You predict, read, explain back, and write the core hunk yourself at L0-L1. Human time is deliberately spent here; the article minimises it |
| Flags, staged release, fast rollback | Not yours | Small reversible PRs, a notes entry for behaviour changes, and a 60-day post-merge watch (S9): offer the revert yourself |
| Company token budget | Subscription limits | Model routing, a log-triage subagent, notes as cache, fork CI for compute |

---

## 1. One-page flow map

```
            AUTOMATED                    AGENT-ASSISTED                     ME                              MAINTAINER
S0 Select   CI/feedback on my PRs      validity on develop, claim search  pick one; S0 fields               -
S1 Repro    reproduce.sh (sandbox)     build minimal repro per SKILL.md   state problem in my words;        -
                                                                          read the verdict output
S2 Explore  -                          reading map (sbt-explainer);       PREDICT, read, explain back       -
                                       grade my explanation
S3 Decide   -                          decision-or-information; ladder;   send or not (I post)              "wanted?" and direction
                                       draft message                                                        (ONLY pre-code touchpoint)
S4 Build    gates: compile, fmt, MiMa, failing test first; scaffolding    write the core hunk (L0-L1);      -
            tests, scripted, contraband, (L0-L1) or implementation (L2+)  real-session smoke test (C15)
            size
S5 Review   -                          fresh-context reviewer, max 3      verdict per finding;              -
                                       rounds, diff-only after round 1    explain-back gate (100%)
S6 Submit   fork CI full matrix after  PR text draft; push commands       sync, push to fork, read          reads the PR
            syncing upstream                                              evidence, open the PR             (the one big spend)
S7 Feedback -                          classify comments; draft replies   decide each; post replies         decides
                                       and fixes
S8 Close    anchor check; metrics row  draft note updates                 write the notes in my words; quiz -
S9 Watch    weekly issue search on     triage reports touching my change  own any regression; offer revert  decides revert
(60 days)   my area's keywords
```

Maintainer attention is spent at three points only: S3 (a closed question, before code), S6 (reading a small,
evidenced PR), and S7 (deciding on my replies). Everything else is resolved locally.

---

## 2. Per-stage spec

Each stage: goal, what is automated, what the agent hands me, what I decide, the exit criterion, failure modes,
and what the checks miss.

### S0 Select
- **Goal:** pick one item that is valid, unclaimed, small, in an area I'm allowed to work in at my current
  autonomy, and that teaches me a slice.
- **Automated:** at session start, `gh pr list -R sbt/sbt --author @me --json number,state,statusCheckRollup`
  (I run it and paste the output). No WIP cap (decided 2026-10-20), but an open PR with red CI or unanswered
  maintainer feedback comes first.
- **Agent hands me:** for each candidate, the S0 fields of `items/_template.md`. Still valid on develop
  (code path exists, behaviour plausibly unchanged)? Claimed or covered (open PRs mentioning the number,
  assignees, recent "I'll take this")? Blast radius, risk area, how maintainers responded to similar work,
  and the slice it teaches.
- **I decide:** which one, or "none, do learning or triage this week".
- **Exit:** one item file created.
- **Failure modes:** picking by age alone (old issues are often by design or 1.x-only); picking big
  semantic changes because they're interesting; starting new work while an open PR is red or has unanswered
  feedback. Without a WIP cap, watch the queue: several of your PRs waiting on the same reviewer at once
  raises time-to-merge for all of them.
- **What the checks miss:** a maintainer's private plans (e.g. a rewrite in progress). Only S3 reveals that.

### S1 Understand and reproduce
- **Goal:** a reproduction that fails for the reported reason, on both the affected release and develop.
- **Automated:** `reproduce.sh` in `local-temp/issues/<id>-<slug>/`, exactly per the project's SKILL.md
  (bare mode with the local snapshot via `publishLocalBin`; `--direct` with the affected version; isolated
  caches; `REPRODUCED: yes|no` matched on an issue-specific output fragment, not the exit code).
  **Builds from issues run in the Docker sandbox** (no host `~/.sbt`, `~/.ivy2`, coursier cache or credentials
  mounted), or in a cloud session.
- **Agent hands me:** the repro folder, the decisive 3-10 lines of output, and a one-line verdict per mode.
- **I decide:** whether this really is the reported problem. I restate it in one sentence, in my own
  words, in the item file.
- **Exit:** verdicts recorded; or "does not reproduce", which goes straight to a triage report (a complete
  contribution, no PR).
- **Failure modes:** a repro that fails for a different reason; leaking state between runs (the sbt 2
  action cache is OS-level, which is why the skill isolates caches); running untrusted build code on the host.
- **What the checks miss:** environment-specific bugs (Windows, Git Bash, JDK vendor). Say so in the
  report rather than claiming non-reproduction.

### S2 Explore the slice, then explain it back
- **Goal:** I understand the code path well enough to predict the fix. The agent does not understand it for me.
- **Automated:** nothing.
- **Agent hands me:** first a request for my **prediction** (where it breaks and why, with a confidence of 1-5),
  logged. Then a **reading map** (`sbt-explainer`): entry points, a numbered path of `path:line@sha` anchors,
  new vocabulary, 3-5 questions, and 1-2 experiments to watch it run (a scripted test with `> debug`,
  `inspect`, a breakpoint). No root cause stated.
- **I decide/do:** read the anchors, run an experiment, and write a 5-10 sentence explanation. The agent
  grades it against the code (right, or wrong at an anchor, with evidence). Only then does it show its own reading.
- **Exit:** my explanation is marked correct; prediction hit/partly/miss logged; new glossary entries in my words.
- **Failure modes:** skimming the map and accepting the agent's framing; the agent confidently wrong about
  sbt semantics (macros, scope delegation). Experiments exist to check behaviour, not just code.
- **What the checks miss:** the agent can grade my explanation only against code it read. A wrong shared
  assumption survives. The cold quiz three days later (S8) is the backstop.

### S3 Does a maintainer need to decide?
- **Goal:** spend maintainer attention once, early, on a closed question, and only when it is a real decision.
- **Automated:** nothing. The rules are in Step 4.
- **Agent hands me:** a classification (decision or information, citing the list in AGENT.md); the ladder
  results (what it found by code search, blame, docs, past PRs, similar changes); and either "no decision needed,
  and wanted is already confirmed by <link>" or a draft from `templates/wanted-check.md` or `templates/escalation.md`.
- **I decide:** send it (I post), rework it, or drop the item. What counts as "wanted" already: a
  maintainer comment in the last ~12 months inviting a fix, or a maintainer applying "help wanted" or
  "good first issue" (*assumption*; see 5). An old comment (2014, 2017) does not count.
- **Exit:** a maintainer answer in hand. While waiting, the item is parked and I work on something else.
- **Failure modes:** asking open questions ("thoughts?"); asking for information I could find; asking
  after the code exists; defaulting maintainers ("I'll proceed unless you object").
- **What the checks miss:** maintainers sometimes say yes to the problem and still reject the shape of the
  solution (C02). The escalation template forces options so the shape is agreed too.

### S4 Do the work under local gates
- **Goal:** the smallest change that fixes the root cause, proven by a test that failed first.
- **Automated (in order):** failing test on develop (output shown); compile and Test/compile;
  `scalafmtCheckRepo`; javafmt if Java changed; `mimaReportBinaryIssues`; targeted `testOnly`; the new scripted
  test plus the scripted group(s) for the subsystem; contraband regeneration and diff if `.contra` changed;
  headers for new files; one run on JDK 17; `tools/size-check.sh`. Logs are summarised by `sbt-log-triage`,
  never pasted.
- **Agent hands me:** the test harness and scaffolding. In L2+ areas it also writes the implementation. In
  L0-L1 areas, **I write the core hunk** (typically 5-30 lines) and the agent reviews it.
- **I decide/do:** for launcher, client/server, clean or boot changes, a **real-session smoke test** via
  `publishLocalBin` and an interactive sbt/sbtn session on JDK 17 (C15, from the reverts).
- **Exit:** all gates green; a one-line purpose for every non-test hunk (C03).
- **Failure modes:** the test passes for the wrong reason; fixing a symptom; "while I'm here" changes; new
  surface (C02); long scripted tests that push a CI job past 25 minutes.
- **What the checks miss:** MiMa catches signatures, not behaviour, defaults or source compatibility (your
  #9344 default flip passed MiMa and was still a behaviour change). Scalafmt doesn't catch design. Local runs
  miss Windows. Nothing catches plugin-ecosystem breakage except the community build (job 13), and that only
  samples it.

### S5 Fresh-context self-review (converging)
- **Goal:** find what a maintainer would find, before they spend time on it, without looping.
- **Automated:** none (the reviewer is an agent).
- **Agent hands me:** `sbt-fresh-reviewer` output. It runs with no conversation context, gets only the
  branch, issue, checklist and PR draft, and cites rule IDs. Findings are Important, Nit (max 5) or Pre-existing,
  with file:line. Round 1 covers the full diff; rounds 2-3 cover the new diff only, plus a check that earlier
  findings are resolved. No repeats (the ledger lives in the item file). Classes of bug, not single lines. Max 3 rounds.
  If Important findings remain after round 3: "STOP: reconsider the approach".
- **I decide:** a verdict on every finding (fixed / wrong / intentional / doesn't matter). Pre-existing ones go to
  open-questions.md as candidate work, never into this PR. Then the **explain-back gate**: the agent walks
  every non-test hunk, I explain each, and any unexplained hunk blocks sending.
- **Exit:** no open Important findings; explain-back at 100%.
- **Failure modes:** the reviewer is noisy, so an agent "fixes" nits into more churn; or it's too lenient
  because it shares the author's blind spots. Measure precision (fixed / all findings) per rule. Every
  quarter, re-run the reviewer on the eval set: the 3 reverted PRs' original diffs (it should flag the
  class: platform/session paths), 5 merged PRs that got a bare approval (it should say "nothing to fix"), and
  your PRs with known corrections (it should catch C02/C03). Run the eval against a copy of the checklist
  with the eval cases' PR numbers and specifics removed, and with each case checked out detached at its own
  commit so later history (the revert) isn't visible. The first calibration on 2026-10-20 showed why: the
  reviewer "caught" #9060 by quoting rule C15, which names #9060.
- **Calibration (2026-10-20, `evidence/reviewer-calibration-2026-10-20.md`):** blind, it caught 2 of 3 reverted
  PRs at the mechanism level (#9060 exactly, #8464 the JDK 17 socket path). It blocked the third (#8730)
  with real regressions, but missed the reported Git Bash failure. It also "blocked" both clean PRs, so its
  severity was set above the maintainer's bar. The rubric is now tightened (Important = concrete breakage, a
  policy MUST, or C01-C04; new "Above the bar" bucket), but not yet re-validated. Re-run the 5 cases when usage
  allows; until then, treat its Important findings as candidates and give each a verdict.
- **What the checks miss:** anything outside the diff, such as a plugin depending on old behaviour, or
  maintainers' intent. This is why S3 exists.

### S6 Submit
- **Goal:** a PR a maintainer can approve in minutes.
- **Automated:** **sync with upstream develop first** (`git fetch upstream && git merge upstream/develop`, or
  rebase before review starts). Then I push to the fork, and the full CI matrix runs there. The PR head SHA must
  equal the green fork-CI SHA.
- **Agent hands me:** PR text from `templates/pr-description.md` (part 1 reads as the squash commit, with
  `Generated-by:` and `Fixes #N`; part 2, collapsed, holds repro verdicts, test proof, checks run, where to
  look, risk and revert, and AI disclosure); the exact push and PR commands for me to run.
- **I decide/do:** read the evidence, not the summary; run the commands; open the PR. If I can't say
  what the checks would miss, I'm not ready (from the article).
- **Exit:** PR open, upstream CI green. If upstream CI goes red, diagnose it (`sbt-log-triage`) before anything
  else. A red PR is mine to fix, not "waiting on review".
- **Failure modes:** fork CI tested the branch while upstream tests the merge; a long description nobody
  reads; missing disclosure.
- **What the checks miss:** upstream-only secrets or permissions in CI, and timing flakes.

### S7 Handle feedback
- **Goal:** each comment answered once, and each correction converted into a rule so it never costs them twice.
- **Agent hands me:** the `templates/feedback-reply.md` table, with every maintainer comment classified FIX,
  DISAGREE (with evidence a maintainer can check in under a minute), QUESTION, or FOLLOW-UP (valid but out of
  scope). Draft replies and fixes, as separate commits. A "what changed since your review" note after each push.
- **I decide/do:** each class, then post the replies. Re-request review once the replies are up.
- **Exit:** all threads answered. Every FIX or DISAGREE that taught something becomes a checklist rule (with PR
  link and date). If the same rule fires again, it's a repeat, and mistakes.md gets an entry on why the gate missed it.
- **Failure modes:** the agent "fixes" everything, including things I disagree with; force-pushing over
  reviewed commits; long defensive replies; widening the PR. At **3 maintainer rounds**, stop and ask on the
  PR whether the approach is still wanted.
- **What the checks miss:** tone. Read every reply aloud before posting.

### S8 Close out and learn
- **Automated:** `tools/check-anchors.py`; a metrics row.
- **Agent hands me:** draft note updates; 3 quiz questions for +3 days and +3 weeks.
- **I do:** write architecture and glossary entries in my own words (the agent may only grade them); answer
  the quiz cold.
- **Exit:** INDEX.md checklist ticked.
- **Failure modes:** notes the agent wrote and I never internalised; notes that rot. The anchor checker and
  90-day `last-verified` catch rot; the quiz catches the first.

### S9 Watch after merge (60 days)
- **Automated (optional):** a weekly `gh search issues -R sbt/sbt "<area keyword>" --created ">=<merge date>"`.
- **I do:** if something regresses, I'm first to say "this is from my #N; here's a revert or fix",
  with a repro. The maintainer decides. Any regression is a demotion in that area (Step 5) and a mistakes.md entry.
- **What it misses:** silent regressions nobody reports. The 4-month gap on #9060 shows they happen.

---

## Step 2: Work discovery and ranked shortlist

### Where work comes from (beyond open issues, oldest first)

| Source | Value to maintainers | Value to my learning | Maintainer cost | Verdict |
|---|---|---|---|---|
| **My in-flight PRs** (#9744 red, #9619 waiting, #9799 waiting) | high: they're already in the queue | medium | low if I fix red CI and nudge once | **first, always** |
| **Retro-learning my 7 merged PRs** | indirect: I can own regressions | very high: code I shipped and can't defend | zero | **first, alongside** |
| **Reproducing and triaging stale bugs** on 2.x (repro or "no longer reproduces") | high: the contributing guide lists "garden the issue tracker" | high | low (one comment) | **main source in weeks 1-6** |
| **`pending` scripted tests** (33) | medium: each is a dormant test of a real feature | high (self-contained slice) | medium (needs "is this pending on purpose?") | good, after `git log` on each `pending` file |
| **Doc lies** (06_manual_tests shows 1.x versions and paths) | medium | medium (the dev loop) | low | good first PR |
| **Private review of open PRs** (not posted) | none until posted | high: how others approach a slice | zero | weekly, as learning |
| **Posted reviews** of others' PRs | medium-high if right; noise if not | high | real (they read it) | only at L3 in that area |
| **Missing tests** (e.g. `tasks/` has 1,093 main lines and 0 unit tests) | medium | high | medium (test-only PRs still need "wanted?") | later |
| **TODO/FIXME** (96 in main code) | unknown: many are intentional | medium | medium | only with blame context |
| **Flaky tests** | high | medium | low | needs upstream CI history. I can't see it from the fork; revisit with `gh run list -R sbt/sbt` |
| **Pre-existing self-review findings** | varies | medium | varies | harvest into open-questions.md |

Your default (old issues, oldest first, small) is sound **as a triage source**: reproducing an old bug
costs maintainers one comment and teaches a slice. It is weaker **as a PR source**: the oldest issues
are disproportionately by-design or 1.x-only. Of the 120 oldest open issues (#887 to about #3258, all
pre-2018), 72 have no maintainer comment at all. None has an open PR, and the last maintainer comment is almost
always from 2014-2020. Your own last three started this way: #9720 from #1084 (closed, by design), #9799 from
#1361 and #9744 from #1224. The latter two had only 2014 and 2017 maintainer comments, which aren't current consent.
So: oldest first for *triage*, wanted-signal first for *PRs*.

What counts as a wanted signal in 2026 (observed): eed3si9n answers "can I work on this?" with a median of
about 4.8 hours, with a standard checklist (reproduce manually, tests, disclose AI, green CI on a fork, CLA)
and phrases like "ready for contribution", "up for grabs if it still reproduces", "Yes, please", "happy
to get a PR". He avoids assigning new contributors, and parallel contributors are allowed, so a claim is not
exclusive. "good first issue" has 0 open issues and "help wanted" has 6.

### Ranked shortlist (2026-10-18)

Filters applied: valid on develop (2.x), not covered by an open PR, small-to-medium blast radius, fits current
autonomy, maintainers respond to similar work, teaches a new slice. "Validity" is from report and triage state
unless I say I checked the code. Nothing below has been reproduced yet. That is S1's job.

**Tier 0: in flight (do these first; they are already in the maintainer's queue)**

| # | Item | Next action (mine, local unless noted) | Needs maintainer decision? |
|---|---|---|---|
| 1 | **#9744** `initialProject` (#1224) | **Cause found (2026-10-20):** upstream job 1 fails `scalafmtCheckAll` on `main/src/main/scala/sbt/internal/Load.scala`, a file the PR edits. Fork CI ran the unmerged branch; upstream ran the merge with develop, whose formatter setup had changed (*inferred*: #9737). Fix: merge upstream/develop, `scalafmtAll`, run job 1's commands locally, push. Add the AI disclosure to the description (decided). Prepare, don't post, the C02 answer: which existing mechanism (`onLoad`, `project` command, shell startup) you considered and why it's insufficient | **Yes**: a new public key (ceiling L1). Once CI is green, one closed question on the PR is fair. Recommend waiting until day ~45, then ask |
| 2 | **#9619** Windows dirzip lock (your issue #9618) | Explain-back on the remaining `AccessDeniedException` fallback first. Then re-request review (lighter than a comment); a one-line nudge if it's still quiet after a week | No new decision; the maintainer's review is pending |
| 3 | **#9799** scripted publishing isolation (#1361) | **Decided 2026-10-20: wait.** Explain-back meanwhile (it touches `ci.yml`, `build.sbt` and `project/`, ceiling L0; 123 non-test lines, above p75). One nudge at most | Revisit only if a maintainer responds, or after about day 60 |

**Tier 1: learning, zero maintainer cost (in parallel with Tier 0)**

| # | Item | Why now |
|---|---|---|
| 4 | Retro-learn #9722 + #9744's slice (Extracted, Load) | You'll be asked about #9744. You can't defend it today |
| 5 | Retro-learn #9728 + #9347 (TaskMacro, Def) | Prerequisite for #9162 below |
| 6 | Private review of **#9815** (run/server-test, +50/-5, 24 days, no reviews) and **#9632** (plugin classpath in the action-cache key, +256/-18, matches #9631) | Learn how others approach run/server and cache. Don't post at your current level |

**Tier 2: new items, triage-first (no WIP cap; can start now, in parallel with Tier 0)**

| Rank | Issue | Area | Evidence still valid | Covered? | Blast radius | High risk? | Responsiveness | Teaches | Maintainer decision? |
|---|---|---|---|---|---|---|---|---|---|
| 7 | **#9162** `@cacheLevel`/`@transient` ignored on a local val | core-macros, main-settings (TaskMacro, Def) | filed on 2.x, 2026-04; macros present in develop (sweep checked) | no PR found; a third party asked 04-30, so check before starting | medium | yes (cache semantics) | "ready for contribution" the next day | sbt 2 caching macro, builds on your #9728 | Wanted: **already yes**. Approach: propose first (L0 area) |
| 8 | **#9033** duplicate jars on forked-console classpath | console/run | 33-entry classpath repro on 2.0.0-RC10 | **a maintainer PR (#9034, xuwei-k) was closed**; read why before anything else | small | no | no maintainer comment yet | classpath construction | Wanted-check needed; the closed #9034 may mean "not wanted" or "harder than it looks" |
| 9 | **#9042** `disablePlugin(IvyPlugin)` no longer works | main/ plugins, Load | regression; maintainer traced it to #8459 the same day | no | medium | yes (Load) | analysed same day | auto-plugin loading | **Yes**: the reporter said it can be closed if the change was intentional. Ask whether it's intended before any code |
| 10 | **#9109** `sourcesInBase` duplicates beyond the root project | main/ Defaults | filed 2026-04 by xuwei-k (a maintainer) | no | small-medium | medium | quiet | source discovery settings | A maintainer-filed bug is a strong signal; still confirm |
| 11 | **#9189** `timingFormat` key unused since 2.0.0-RC4 | Keys, Defaults | key defined, never read (sweep grep) | no | small | public API | filed by xuwei-k | key wiring, MiMa | **Yes**: rewire vs deprecate. Your **first escalation-template practice**: a closed question, cheap to answer |
| 12 | **Doc lie**: 06_manual_tests.md shows 1.x versions and paths | contributing-docs | lines 13, 57-65 @ 2ef94e08 | no | tiny | no | n/a | dev loop (`publishLocalBin`, boot cache, `sbtOn`) | Start a conversation (short issue), then PR. Verify by following the doc |
| 13 | **Pending scripted tests audit** (33) | sbt-app/src/sbt-test | `pending` markers present | n/a | none (report) | no | n/a | scripted infra, related to #9799 | Report-only: a table of "passes now / still fails / pending on purpose (blame)". The maintainer decides |
| 14 | **#9693** JEP 500 warning with forked tests | worker (multi-release JAR) | filed 2026-08-29; maintainer sketched an approach | no | small-medium | no | sketched approach | MRJARs, JDK 17+ | Confirm timing; the approach exists |
| 15 | **Old-bug triage batch**: #1993, #2203 (DSL/parser), #2454 (tab completion), #1485, #2506, #1583 (forked-test output) | various | titles suggest possibly still valid on 2.x (*inferred*) | no | none (report) | no | 2.x-moot issues get closed (#7334) | breadth | Report-only: "reproduces on 2.x with this minimal build" or "doesn't; suggest closing". At most one comment per issue, and only when the result is decisive |

**Deliberately excluded:** #9642 (overlaps the +4,824-line #9556), #9653 (wait for #9619, Windows-only),
#9122 (library-management resolution, sensitive), #9840 (protocol design still moving),
issues with open PRs (#9631, #9891, #9410, #9908, #1469).

---

## Step 4: Escalation ladder

Before anything reaches a maintainer, climb these rungs in order. Each one has a timebox and a log line in the item file.

| Rung | Tool | Answers | Timebox |
|---|---|---|---|
| 1 Code search | `git grep`, symbol references, `inspect`/`show` in a running sbt | what and where | 15 min |
| 2 Blame and history | `git log -S`, `git log -L`, `git blame` to commit to PR to its review thread | why it is this way | 20 min |
| 3 Docs | contributing-docs, `notes/`, Scaladoc, sbt website docs | intended behaviour | 10 min |
| 4 Past decisions | `decisions.md`, `gh search issues/prs -R sbt/sbt "<terms>"` | has it been decided | 15 min |
| 5 Similar changes | how sibling bugs were fixed (`git log -- <neighbour files>`) | how it's usually done | 15 min |
| 6 Fresh-context agent | a new subagent with only the question and anchors (no conversation history) | is my reasoning sound | 1 run |
| 7 Ask once | `templates/escalation.md` or `wanted-check.md`, on the issue | a decision only maintainers can make | n/a |

**Information** (never ask): how code works; why it's this way; conventions; how to test; whether it reproduces; how 1.x behaved; which file to change.

**Decision** (ask, once, early):
- Is the change wanted?
- Does user-visible behaviour or a default change?
- Does public API change (Keys.scala, anything outside `sbt.internal`)?
- Is a bincompat trade-off involved?
- Does it touch CI workflows, the build, release or launchers?
- Is it a deprecation, or a choice of backport target?
- Is it a choice between viable designs whose trade-offs depend on what maintainers want?

The test: *could a careful reader of the code and history answer it with certainty?* If yes, it's
information. *Does the answer depend on what maintainers want for users or the project's future?* If yes, it's a
decision. *Would guessing wrong be costly to undo?* (public API, defaults): treat it as a decision even if you're
fairly sure.

**The message:** a closed question; 2-3 options with the cost of each; your recommendation; what you already checked;
the size of the PR it would lead to; no "I'll proceed unless you object". On the issue, not in DMs. One message.

**If there's no answer:** park the item and work on another. Bump once on the same thread after about 14 days
(p90 first response is about 5-7 days; stuck PRs moved after 16-22-day nudges). After a second silence, drop
it and note it in decisions.md as "no decision".

---

## Step 5: Autonomy levels per area

Full map and rules: `notes-skeleton/autonomy-map.md`. Summary:
- **L0 ask first**: an open question before design. **L1 propose**: a design plus recommendation; wait for OK.
  **L2 decide and explain** in the PR. **L3 decide and defend**, and review others' PRs in the area publicly.
- **The "wanted?" question is always settled first** (policy). Autonomy governs *how* decisions, not *whether*.
- **Ceilings**: public API and defaults max L1; CI, build, release and launcher packaging max L0. These mirror the
  article's "sensitive paths always need a person".
- **Promotion** requires merged work *and* passed explain-back *and* a cold quiz in that area. Merged code alone is not
  evidence of understanding, so every area starts at L0-L1 for you today.
- **Demotion**: a revert or regression traced to you (to L0); the same rule corrected twice (down one level); "please discuss
  first" (to L0); 6 months idle (down one level).
- The agent's own autonomy is fixed: draft, run read-only and local commands, never publish. It does not grow.

---

## Step 6: Knowledge system

Location: `~/oss/sbt-notes/` as its own private git repo, outside the clone. Seeded in `notes-skeleton/`:
INDEX, architecture/map, glossary, conventions, decisions, reviewers, checklist, mistakes, open-questions,
autonomy-map, metrics, items/, learning/.

- **Read** at item start: INDEX's five files only (item, checklist, autonomy rows, last 5 mistakes, the area
  note if fresh). That costs fewer tokens than re-reading code.
- **Write** at item end, in *your* words. The agent drafts structure and grades; it doesn't author your explanations.
- **Linked to code** with `path:line@sha` anchors. `tools/check-anchors.py` flags CHANGED and GONE anchors and
  `last-verified` older than 90 days.
- **Dated and pruned** monthly (15 min), with a per-file pruning rule in INDEX.md. Delete what you can no longer explain.
- **Learning check**: predict, then verify (`learning/predictions.md`, with confidence 1-5 for calibration); a cold
  quiz at +3 days and +3 weeks (`learning/quiz-bank.md`, seeded with 7 questions on your merged PRs).

---

## 4. Rollout plan and metrics

**Phase 0, week 1 (about 6h, zero maintainer cost):** install (README.md). Create a **read-only** GitHub token for
agent sessions. Build the Docker sandbox image. Time the gates on develop once, so you know your machine's costs
(compile, Test/compile, one scripted group, MiMa). Sync your fork's develop (you, in your terminal).

**Phase 1, weeks 1-3: in flight and retro-learning (strict gates; measure only).**
- Tier 0: #9744 (diagnose red CI against current upstream, add disclosure), #9619 (explain-back, then re-request
  review), #9799 (explain-back; nudge at most once).
- Tier 1: retro-learn 2 merged PRs per week (#9722 and #9442 first, then #9728 and #9347). Each gets: prediction, reading
  map, your explanation, explain-back on every hunk, a glossary entry, a quiz at +3 days.
- One private review (#9815).
- Exit: all three open PRs green upstream, disclosure fixed, explain-back at 100% on each.

**Phase 2, from week 1, alongside Phase 1 (no WIP cap): the first 2-3 new items (strict gates; you write the core hunk).**
1. **#9189 escalation** (decision practice, no code until answered).
2. **Doc-lie fix** (06_manual_tests), verified by following it, or the **#9033 repro and wanted-check** if you'd rather have a code item.
3. **#9162** after the #9728 retro-learn, if a maintainer OKs your approach. Otherwise #9042 or #9109.
- Triage reports (#15 batch, pending-tests audit) fill the waits.

**Phase 3, week 8 onward: loosen on evidence only.** After 3 completed items, review metrics.md:
- *Loosen* (one step at a time) if all hold: EB 100% on every item; MRT ≤ 1 per PR; zero repeated corrections;
  upstream CI first-time green; reviewer precision ≥ 60%. Possible steps: promote areas per the map; fewer
  self-review rounds on small diffs. You keep writing the core hunk at L0-L1 (your choice, 2026-10-20).
- *Tighten* if any of: a repeat correction, an unexplained hunk caught late, a revert, red upstream CI twice.

**Metrics** (definitions in `notes-skeleton/metrics.md`, with a baseline from your 11 PRs):

| Metric | Baseline | Target |
|---|---|---|
| Maintainer round trips per PR (MRT) | 0-2 | ≤ 1 |
| Repeated corrections | **present** (C02 ×4, C03 ×3) | 0 |
| Time to first maintainer response | project median ~13h | track only; it's theirs |
| Time to merge | 0-67 days for your PRs | trend down; mainly via size |
| Upstream CI red before green | ≥1 (#9744) | 0 |
| Non-test size | 17-304 lines | ≤ 62 typical, ≤ 137 max without explicit OK |
| AI disclosure present | 8/11 | 11/11 |
| Explain-back (EB) | "few" (self-assessed) | 100% before sending |
| Prediction hit rate | none | rising per area |
| Concepts learned (verified glossary/architecture entries) | 0 | about 3-5 per item |
| Reviewer precision (fixed / all findings) | none | ≥ 60%; drop or rewrite rules below it |
| Usage per item (from `/usage`) | none | visible; trend down as notes accumulate |
| Regressions within 60 days (guardrail) | 0 known | 0 |

---

## 5. Assumptions and open questions for you

1. **Paths**: `~/oss/sbt-notes/` for notes and `~/src/sbt` for the clone, with `upstream` = sbt/sbt. Adjust paths in AGENT.md and settings.
2. **"Wanted" signals**: I treat a maintainer comment from the last ~12 months inviting a fix, a maintainer-applied "help wanted", or a maintainer-filed bug as "wanted". The policy text doesn't define it. If you know eed3si9n's expectation better, override.
3. **Decided 2026-10-20: no WIP cap.** New work doesn't pause. Ordering rule: red CI or unanswered feedback on an open PR comes first.
4. **Decided 2026-10-20: #9799 waits.**
5. **Decided 2026-10-20: leave merged PRs as they are; add the disclosure to open #9744.**
6. **Decided 2026-10-20: you write the core hunk at L0-L1** ("I want to learn").
7. **Resolved 2026-10-20:** the 10-item commit-message guideline was read verbatim from upstream develop and is summarised in `templates/pr-description.md` and AGENT.md rule 7.
8. **Squash body source**: still unverified. The guideline's "details belong in the PR description" means commit body and PR description are separate. The template keeps part 1 commit-compliant in case it's used either way.
9. **Local models**: you chose not to use the GPU server for now. The model is designed for a Claude Code subscription only. A local model could later take log triage and comment classification (the haiku subagents' jobs) if usage limits bite.
10. **Sandbox**: Docker for untrusted builds, cloud sessions as a fallback. The image recipe is in README.md and is untested on your machine.
11. **Sweep limits**: rate limits meant the PR sample was a paged walk (Mar to Oct merged; Jul to Oct closed), not random; Discussions were unreadable. Re-run `tools/mine-reviews.sh` locally with your `gh` to refresh the checklist quarterly.

---

## 6. Check your understanding before adopting this

Answer cold, then check against the sections cited. If you miss two or more, re-read section 0.

1. Your #9344 passed MiMa. Why was it still a compatibility-relevant change, and where in this model would that be caught? (C09, C10, S4 "misses")
2. Fork CI was green on #9744's exact SHA but upstream job 1 was red. Give the most likely structural reason, and the gate that closes the gap. (S6)
3. You find a bug in an untouched function while fixing #9033. What do you do with it, and why not fix it in the PR? (S5, open-questions)
4. Classify each as decision or information: (a) why `Extracted.runAggregated` used the global scope; (b) whether `timingFormat` should be rewired or deprecated; (c) whether a scripted test or a HedgeHog test fits #9033. (Step 4)
5. Which two checklist rules are already repeated corrections for you, and which local check now targets each? (C02, C03; metrics baseline)
6. All three recent reverts had green CI. What do they have in common, and which rule responds to it? (C15)

