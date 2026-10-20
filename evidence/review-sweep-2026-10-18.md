<!-- Raw report from the read-only cloud session "sbt upstream review mining (read-only)", 2026-10-18. Model output, not verified line by line; claims are tagged OBSERVED/INFERRED by that session. Kept for traceability of checklist.md and reviewers.md. -->

# sbt/sbt contribution research: PR review patterns (read-only, as of 2026-10-18)

**Sources.** Five read-only subagent sweeps, assembled by me. Nothing was written to GitHub or to files. Unless a claim is marked INFERRED, it was OBSERVED directly in PR, review or issue data.

**Caveats that affect every number below:**
- The search endpoint was rate-limited (403) for several agents, so they paged `list_pull_requests` instead.
- Maintainer-authored PRs, jozanek's own PRs and PRs by bots are mostly excluded from the samples.
- "Review rounds" are partly INFERRED from review timing.
- I paraphrased throughout.

## 1. Merged sample: 48 PRs into develop

Coverage is Mar–Jun (25 PRs) and Jul–Oct (23 PRs). That is 44 non-maintainer and 4 maintainer PRs, and #9337 is one day outside the window. Some PRs the agents did not open (#9911, #9811, #9809, #9806, #9804, #9790, #9789, #9788, #9785, #9783, #9771, #9765) were not analysed.

Merger: eed3si9n merged nearly all of them. anatoliykmetyuk merged #8880, #9448 and #9669 (INFERRED from the Jul–Oct agent's notes).

### Mar–Jun merged PRs

| PR | Author | +/−/files | Days | Rounds | 1st maint. | Substantive maintainer feedback (maintainer) → category |
|---|---|---|---|---|---|---|
| 8866 | fury0928 | 121/33/5 | 1.1 | 0 | 27h | None pre-merge. Post-merge a non-maintainer (SethTisue) said "refactor" in the title is misleading, and eed3si9n said it might be noted as ivyless publishing → release notes / PR title |
| 8880 | seroperson | 826/69/43 | 5.6 | 1 | 4.6d (anatoliykmetyuk) | Abort instead of hard reset if local edits exist; consistent "changed" semantics → correctness. `exists` with a side effect; extract the long predicate → style. Dedup test unclear; reflection vs import; add the `Every` strategy case → tests. Document the feature → release notes. Warning instead of auto-update → design. (eed3si9n) Scala 3 enum? → design/style. Develop is the 2.1.x line → branch |
| 8887 | binaryworldtl | 44/3/3 | 1.8 | 0 | 44h | None |
| 8903 | majk-p | 51/6/2 | 0.9 | 0 | 21h | None |
| 9011 | corevibe555 | 5/1/1 | 0.8 | 0 | 20h | None. Split out of #8921 earlier at a reviewer's request → scope. AI tag present |
| 9041 | tanishiking | 37/2/3 | 0.6 | 1 | 1.1h | (eed3si9n) Add a comment explaining why plain inline failed → style/comments |
| 9047 | bitloi | 70/8/2 | 4.0 | 0 | 20h | (eed3si9n) Copy-then-move may be slower on Windows; use `Retry` and copy once → performance/platform. Author kept the design and it was approved anyway |
| 9050 | Crystora | 29/29/1 | 0.4 | 0 | 9h | None |
| 9051 | jonathanchang31 | 43/14/4 | 5.2 | 1 | 35h | (eed3si9n) Don't add a second command and parser; make the existing parser accept both names → design. Changes requested |
| 9098 | mkurz | 7/3/4 | 6.1 | 1 | 10h | (eed3si9n) Don't require an extra env var; keep laptop builds easy → design/dev experience |
| 9102 | zainab-ali | 211/144/8 | 7.7 | 3 | 19h | (eed3si9n) History of `evictionWarningOptions`, unsure about `default`→`full` → design. Asked for before/after eviction output → repro evidence. Coursier treats Compile and Test as separate graphs, so deduping loses information; test on the reported kafka build; prefer the `evicted: true` revision deterministically; distinguish Compile from Test in output → correctness. Backport labels added |
| 9110 | mrdziuban | 45/8/2 | 0.7 | 0 | 17h | None |
| 9131 | arashi01 | 420/72/9 | 1.1 | 0 | 10h | (eed3si9n) "Generally supportive"; merged without blocking review → design |
| 9147 | jimcody1995 | 69/17/3 | 0.55 | 1 | 3.5h | (eed3si9n) Cited CONTRIBUTING: reproduce manually, include tests, disclose AI use, sign the Scala CLA, get CI green on a fork. Asked whether the Wayland error was reproduced and how we would know it is fixed → repro evidence / tests / AI disclosure / CLA. Merged anyway |
| 9226 | BrianHotopp | 364/35/14 | 3.0 | 1 | 18h | (eed3si9n) New tests should use HedgeHog or Verify, not ScalaTest → tests (wrong kind). AI disclosure and release note were in the body |
| 9250 | BrianHotopp | 162/11/8 | 2.2 | 0 | 54h | None. Body had an AI disclosure, a scripted test and a MiMa note |
| 9253 | mrdziuban | 416/32/2 | 38.2 | 0 | 22.4d | (eed3si9n) Wants to reproduce the perf issue and understand why it is faster; is sorting plus combining sets really 25s? → repro evidence/performance. A third-party user confirmed 163s→105s. Approved after a second pass; author nudged on day 22 |
| 9260 | BrianHotopp | 44/5/4 | 1.2 | 0 | 28.5h | None. "AI-assisted" in the body |
| 9271 | BrianHotopp | 60/4/4 | 2.1 | 0 | 51h | None |
| 9293 | arashi01 | 121/9/11 | 2.1 | 1 | 19h | (eed3si9n) `addPlatformSuffix` should be `private[sbt]` → public API. Accepted a duplicate in lmcoursier with cross-referencing comments; move the package in a separate PR → scope. Avoid infix `a.orElse(b)`; use braceless match, citing 03_coding_style.md → style |
| 9295 | BrianHotopp | 254/1/7 | 8.0 | 1 | 7.4d | (eed3si9n) All-lowercase progress text, verb "downloading" → naming. Said it "looks very cool" |
| 9337 | BrianHotopp | 161/12/5 | 16.9 | 1 | 16.8d (after a nudge) | (eed3si9n) Remove the `println`; users can't act on it → design/UX |
| 9353 | merlinorg | 14/9/3 | 9.2 | 2 | 5.3h | (eed3si9n) Use `Long` for the job id since `JobHandle#id` is Long → correctness. Remove the CONTRIBUTING.md additions because they duplicate contributing-docs/06_manual_tests.md → scope/docs |
| 9364 | yhefamly | 57/26/1 | 7.2 | 0 | 3.5h | (eed3si9n) Sign the Scala CLA → other. AI disclosure and a reproducer (600s→1.2s) in the body |

Maintainer-authored PRs seen in this window: #9244 (xuwei-k, 63 days to a single approval), #9255 (anatoliykmetyuk, 5 days to approval).

### Jul–Oct merged PRs

| PR | Author | +/−/files | Days | Rounds | 1st maint. | Feedback → category |
|---|---|---|---|---|---|---|
| 9907 | eugkhp | 68/8/2 | 0.4 | 0 | ~10h (merge) | None |
| 9904 | eugkhp | 81/12/3 | 1.0 | 1 | 25h | None from maintainers. A non-maintainer (stasimus) found that the in-memory store's `syncBlobs` returns Nil so the check always misses, and the class is public → correctness/public API. Author reworked |
| 9901 | mkurz | 192/6/5 | 0.7 | 1 | 9h | (eed3si9n) Rename unused `newState` and `terminationState` → naming |
| 9896 | jleider | 146/26/21 | 3.9 | 0 | none visible | None. Repro, scripted tests and AI disclosure were in the PR |
| 9885 | retronym | 2/2/1 | 0.04 | 0 | <1h | None |
| 9873 | seveneves | 88/32/2 | 0.1 | 0 | 2h | None |
| 9870 | PhoenixmitX | 334/20/15 | 1.7 | 2 | 29h | (eed3si9n) Shorten a long Scaladoc → comments. A `Files.walk` over the class dir on every edit is costly and pointless on APFS → performance/correctness. Author dropped the walk |
| 9864 | kitbellew | 1/1/1 | 0.5 | 0 | 3h | (eed3si9n) CI crossed the 25-minute timeout and failed 3 times → CI. The change was qualified-private→public → public API |
| 9860 | eugkhp | 34/3/4 | 2.1 | 0 | 26h | None. Repro, scripted test, MiMa and AI disclosure were in the PR |
| 9848 | pierscin | 115/7/2 | 1.3 | 0 | 3h | (eed3si9n) Approved, then noted `put` vs `add` is subtle and JDK-dependent and asked about logging → design |
| 9839 | mkurz | 116/10/5 | 0.4 | 0 | 2h | (eed3si9n) Filed an unrelated failing-test issue; approved → CI |
| 9793 | PhoenixmitX | 99/4/10 | 3.3 | 1 | ~2.6d | (eed3si9n) Move helpers out of `Defaults.scala` into `sbt.internal.Compiler` and scope them `private[sbt]` → public API/placement. The author said it was their first contribution |
| 9766 | stasimus | 69/25/2 | 0.1 | 1 | 0.8h | (eed3si9n) Can the Windows `isWindows` guard in the BSP test be removed? He wanted the test to exercise the route → tests/platform |
| 9753 | alexasl | 2/2/1 | 0.5 | 0 | none visible | None |
| 9689 | kitbellew | 90/68/4 | 5.4 | 0 | 4h | (eed3si9n) Use `IO.copyFile`, which already writes atomically → design. Part split to #9694 (depends on sbt/io 552) → scope. anatoliykmetyuk approved 4.3 days later |
| 9685 | stasimus | 820/25/10 | 11.7 | 2+ | 11.6h | (eed3si9n) Use a list type in `portfile.contra` → naming/design. (anatoliykmetyuk) -D props from `.sbtopts`/`.jvmopts`/`SBT_OPTS` not seen; disabled autorestart should warn; duplicate keys must use the last; newline separator is ambiguous → correctness ×4. Diagnostics may expose secrets in -D values → security. Approved "LGTM" 3 days after the last response |
| 9669 | azdrojowa123 | 130/3/7 | 0.2 | 1 | 1.4h | (eed3si9n) Scripted tests run in batch so reload semantics are messy; suggested a separate scripted group. Cleaning the global dir was accepted instead → tests/CI |
| 9655 | unkarjedy | 199/28/9 | 3.3 | 1–2 | 6.6h | (eed3si9n) Created issue #9658 retroactively after the author declined to add an Empty case → scope. Peer stasimus: public `SuiteResult` exposes throwables, value equality, weak scripted test, `SuiteResult.+` lacks Empty → public API/tests/correctness |
| 9623 | hoangmaihuy | 18/4/3 | 8.7 | 1–2 | 3.4d | (eed3si9n) Prefer fixing out-of-the-box APFS behaviour over a config flag; hard links rejected because they write through to the shared CAS → design. Won't backport; performance work lands on develop → branch. Cleanup: only `cleanFull`, suggested a Bazel remote cache → other |
| 9563 | takayahilton | 259/48/52 | 0.7 | 1 | 11h | (eed3si9n) Suggestions to simplify the buffer-length check and use `Files.isRegularFile` → style/correctness. 52 files, mostly generated (INFERRED) |
| 9515 | hoangmaihuy | 830/56/11 | 36 | ~1 | 10h | (eed3si9n) Split into independently applicable fixes (author made four PRs) → scope. Develop targets 2.1.0; 2.0.x backports are slowing after regressions → branch |
| 9448 | BrianHotopp | 143/30/3 | 2.6 | 1 | ~1.5d (anatoliykmetyuk) | Do Windows paths with spaces still work? → platform/correctness. Integration test proving the flag reaches the new server → tests (wrong kind). Author fixed the tokenizer and added a unit assertion instead of a scripted round trip. Post-merge, eed3si9n explained why it missed 2.0.3 (CVE fixes) → branch |

Also read: #9500 (eed3si9n, maintainer).

### Review-round and size observations

- 15 of the 48 got only a bare approval ("Thanks!") with no inline comments: #8887, #8903, #9011, #9050, #9110, #9250, #9260, #9271, #9907, #9896, #9885, #9873, #9860, #9753, and #9839 apart from an unrelated issue.
- Every PR that drew multi-round design discussion was large or touched shared semantics: #8880 (826 lines), #9102 (8 files), #9685 (820 lines), #9515 (830 lines).
- The one PR with a long open time and no maintainer objection was #9253, at 38 days. It was waiting on a maintainer reproduction of the perf claim.
- A small group of contributors (stasimus, kitbellew, BrianHotopp, mkurz) account for many of the merged non-maintainer PRs.

## 2. Closed-unmerged sample: 19 PRs

**Coverage limit.** Only about Jul 13–Oct 18 was paged, and Jan–Jul 2026 was not sampled. The task asked for Jan 1 onward, so this is a gap. CI state is "not retrieved" for most rows, and the closer is INFERRED where no closing comment was visible.

| PR | Author | Size | Days | Closer | Reason | AI disclosed? | Prior issue? | CI at close | 1st maint. response |
|---|---|---|---|---|---|---|---|---|---|
| 9910 | cpitclaudel | 26/10/2 | 1.9 | eed3si9n | Superseded by his #9911, which kept the contributor's test (stated) | No | Yes (#9850) | n/r | ~12h |
| 9912 | stasimus (draft) | 54/2/3 | ~0 | author (INF) | Unstated; follow-up to #9911 | No | Refs #9911 | n/a | none |
| 9844 | hoangmaihuy | 10/4/1 | 12 | author | Superseded by maintainer perf PR #9888 (stated) | Yes (Claude Code) | Yes (#9843) | n/r | none |
| 9903 | mkurz | 203/7/5 | 0.5 | eed3si9n | 1.12.x backport; review the develop PR first; no more 1.12.x releases (stated) | Yes (Codex) | Yes (#9900) | Windows client job failing (author says stock server smoke test) | ~13h |
| 9754 | mmustafasenoglu | 135/?/5 | 0.35 | unknown | Unstated; first draft had not been compiled against the pinned coursier (INF) | Disclosed only after a contributor remarked on AI-sounding replies | "Fixes #9732" | pending | none |
| 9580 | ecat3 | 548/37/15 | 31 | author (INF) | Stale after the author found clients depend on `buildClock` | Yes | No | author says fork CI green | none visible |
| 9699 | msosnicki | 36/3/4 | 10 | unknown | Unstated | No | Yes (#9698) | CLA only | none |
| 9568 | warcholjakub | n/a | ~0 | author (INF) | "CLA migration test" throwaway | No | No | n/a | none |
| 9627 | ColOfAbRiX (draft) | 56/65/5 | 26 | author (INF) | Superseded by #9731; maintainer had asked for 3 issues and 3 PRs | Yes, prominent | None initially; asked "Is there a GitHub issue?" | n/r | ~22h |
| 9518 | ColOfAbRiX | 10/2/1 | 0.2 | author (INF) | Unstated; likely mixed scope with #9482 | Yes | No | pending | none |
| 9541 | BrianHotopp | 47/22/8 | 1 | author | Maintainer asked "is there an open problem?" pointing to merged #9469 and #9538; author agreed it was too broad (stated) | Yes (Claude Code) | Branch name refs #9468 | n/r | ~13h |
| 9510 | BrianHotopp | 35/12/2 | 1 | author | Superseded by his own #9521 (stated) | Yes | Refs #9507 | n/r | none |
| 9725 | stasimus | 146/6/7 | 6 | author | anatoliykmetyuk: reverses a deliberate perf decision (#9462, #9473); no repro on #9607; test not end-to-end. Author found the bad bytecode was already in the cached blob and withdrew (stated) | No | Refs #9607, no repro | n/r | ~5.4d |
| 9634 | stasimus | 121/10/6 | 23 | author (INF) | Unstated. Maintainer agreed on a shutdown-hook approach, then it was closed (reason unknown). Related to the #9060 revert | No | Yes (#9633) | n/r | ~15.7d |
| 9654 | stasimus (draft) | 1208/22/33 | 3 | author (INF) | Unstated; rebase of eed3si9n's #8584 with known perf/classloader issues. Maintainer noted JDK 8 compile isn't possible unless Zinc is built for JDK 8 | No | refs #8584 | n/r | ~10h |
| 9787 | kitbellew | 59/44/2 | 15 | author | Nudged "not much traction in 2 weeks" then closed (stated) | No | No | n/r | none |
| 9536 | eed3si9n (draft) | 235/198/6 | 15 | maintainer (INF) | WIP stacked on #9533; unstated | n/a | n/a | n/a | n/a |
| 9772 | mkurz | 97/7/2 | 0.6 | author | Maintainer built alternative #9775 (Gigahorse should honour `Realm.usePreemptiveAuth`); author closed in its favour (stated) | Yes (Codex) | Yes (#9774) | n/r | ~7h |

**Reasons tally (19 PRs):**
- Superseded by a maintainer or own alternative: 7 stated (#9910, #9844, #9627, #9541, #9510, #9772, and #9903 partly).
- Author withdrew after a maintainer objection: 1 (#9725).
- Stale, no traction: 2 (#9787, #9699).
- Unstated, abandoned or reworked: 5.
- Throwaway: 1. Maintainer WIP: 1. Backport with no future release line: 1.
- No maintainer closed a PR for "AI use", "CI failing" or "too large" in this sample. Those reasons are at most INFERRED.
- Authors closed their own PR in at least 7 of 19 (OBSERVED). Maintainers closed 2 (#9910, #9903).

## 3. jozanek's PRs (11 PRs; exhaustive search)

All maintainer review in these threads came from eed3si9n. xuwei-k and anatoliykmetyuk do not appear. Non-maintainer stasimus also reviewed #9720 and #9722.

| PR | Title | State | +/−/files | Days open | Outcome |
|---|---|---|---|---|---|
| 9814 | publishLocal overwrites, remote publish does not | MERGED 9/22 | 573/26/11 | 0 (same day) | Approved ("Thanks!"). Split out of #9799 at his request |
| 9799 | Publishing isolation for scripted | **OPEN** | 204/10/12 (8 commits) | 28 | He asked for the publishLocal bug to be a separate issue/PR (scope). Author did so (#9813, #9814). No response since |
| 9744 | initialProject setting | **OPEN** | 236/1/16 | 37 | No reviews or comments |
| 9728 | Diagnostics for task-local refs | MERGED 9/11 | 340/?/7 | ~2 | Approval only |
| 9722 | runAggregated resolves project axis | MERGED 9/10 | 161/8/7 | 3 | stasimus found a correctness issue (empty-match case still ran tasks); author fixed. eed3si9n approved with a caution that the bug dates from about 2013, so the fix could change build semantics |
| 9720 | updateGlobalPlugins command | CLOSED by author 9/30 | 192/8/14 | 23 | Peer fixes done. eed3si9n said non-snapshot plugins not auto-updating is by design; asked to retest with SNAPSHOT. Author found it reproduces only for a SNAPSHOT over HTTP. He replied sbt should not support remote SNAPSHOT and he would sooner close #1084 than add a special command. Author agreed and closed (design/not wanted) |
| 9619 | Locked dirzip on Windows | **OPEN** | 61/36/2 | 62 | Changes requested 8/17: use `IO.copyFile` rather than a hand-written install. Author switched (758c31e) and kept a narrow `AccessDeniedException` fallback; replied 9/1. No maintainer response since |
| 9442 | Forked run inherits cwd | MERGED 7/26 | 150/45/11 | 14 | Test cwd has been the subproject for so long that changing it could break builds → scoped to `run` only, new key dropped (naming/design). Post-approval he suggested a `Compile / run / baseDirectory` approach and linked #9530 |
| 9434 | -java-home in Windows launchers | MERGED 8/13 | 446/99/9 | 33 | Single-dash `-java-home` shouldn't be supported (design). "Minimize the change to just bug fixes" (scope). Author trimmed from +595/−152 and removed `ArgParser` and package-private leftovers. Author pinged 7/25 and 8/11 |
| 9347 | Seq[Initialize[Task]].join | MERGED 8/21 | 42/5/4 | 67 | `richTaskSeq` is existing API so removing implicits isn't safe (bincompat/public API) → author used an extension method. Separate an unrelated change → scope. Author pinged 7/25 |
| 9344 | Patterns.isMavenCompatible default | MERGED 6/16 | 225/7/8 | 1 | Approved same day; documents the compat impact in a notes file |

**AI disclosure.** 8 of the 11 descriptions disclose AI use, and #9744, #9728 and #9434 do not. No maintainer objected to AI in any thread read. Earlier I counted 9 of 11, but the agent's own list of non-disclosing PRs has three, so 8 is the consistent figure.

**Prior maintainer confirmation.** I did not verify this for most linked issues. The agent checked #1224 (a 2017 comment from dwijnand saying to track "a more formal way" to define the initial project) and #1361 (eed3si9n comments from 2014). Neither is a recent "please send a PR". I found nothing for the others.

### Open PRs: current state

| PR | CI on head | Mergeable | Last activity | Waiting on |
|---|---|---|---|---|
| 9799 | 15/15 green (240e627) | unknown | 9/22 (26 days ago) | INFERRED: eed3si9n review of the split |
| 9744 | 14/15; `test (ubuntu-22.04, 21, temurin, 1)` failed, cause not determined, possibly flaky (INFERRED) | unknown | 9/11 (37 days ago), no replies | INFERRED: first maintainer review |
| 9619 | 15/15 green (758c31e) | unknown | 9/1 (47 days ago) | eed3si9n; his changes-requested review is still the latest maintainer state and the author replied 9/1 |

### Recommended next steps for these (INFERRED)

- #9744 adds a new public setting, which this maintainer tends to question. It also has a failed check and no response, so a short note on why the setting is needed, plus a re-run of the one failing job, is the lowest-friction next step.
- #9619 and #9799 appear to be waiting on the maintainer, not on you. A polite nudge is consistent with what other contributors did, such as #9253 and #9337, which moved after day 16–22 nudges.

## 4. Reverts

Pairing (OBSERVED from revert PR text and linked issues): #8464→#8557, #8730→#8797, #9060→#9747. #8919 has no revert that I found. The revert search was rate-limited, so I cannot fully rule one out.

| | #8464→#8557 | #8730→#8797 | #9060→#9747 | #8919 |
|---|---|---|---|---|
| Original | mkdev5 (external): sbtn uses JDK17+ NIO Unix sockets via a reflection factory (musl static link) | Eruis2579 (external): quote-aware parsing of .sbtopts/.jvmopts in the bash launcher | xuwei-k (maintainer): `cleanFull` also deletes the launcher bootDirectory | bitloi (external): skip coursier Conflict on relocation cycles |
| Size | 284/11, 8 files | 84/5, 2 files | 7/0, 1 file | 112/1, 4 files |
| Days open | ~3 | ~3 | <1 | ~1.5 |
| Review before merge | 4 comment reviews, then eed3si9n approval | 1 changes-requested, then approval | 1 approval | ~6 comment reviews, then approval |
| CI at merge | 14/14 green incl. Windows and macOS | 15/15 green incl. Windows and macOS | 15/15 green | 15/15 green |
| Merge→revert | ~2 days | ~9 days | ~153 days | n/a |

**What broke and how it was found:**
- **#8464.** sbtn could not connect to the server on JDK 17. eed3si9n found it by using sbt himself, filed #8555 on Jan 16, and merged the revert about 25 minutes later. The root cause was "likely" the JDK-17-only SocketChannel path and was not confirmed.
- **#8730.** On Windows Git Bash, `.jvmopts` containing `-Xmx2G` failed with "Invalid maximum heap size". xuwei-k found it in sbt/zinc CI (which runs the launcher under `shell: bash`) and filed #8767. It was bisected to the parsing rewrite and eed3si9n reverted after confirming on a zinc PR. His CRLF-vs-LF guess was unconfirmed.
- **#9060.** After `cleanFull`, the running session breaks because in-use boot jars are deleted, for example `NoSuchFileException` on scala-library.jar. A user reported it in May and eed3si9n first answered that wiping boot was consistent with cleaning caches. A second report in #9633 (Aug 19) led to a proposed patch (#9634, later closed without merge), and on Sep 11 he said removing the boot dir was probably too much and reverted. Discovery was by user report, and the original sat for about 4 months.
- **#8919.** Not reverted. It carries a stated trade-off (a warning and less eviction detail for cyclic configurations).

**Which local check could have caught each (INFERRED):**
- **#8464.** A manual smoke test running `sbt` on JDK 17 so the shell connects via sbtn, or a scripted test that starts the server and connects on JDK 17. The PR's test plan only said it "compiles and passes the existing test suite" (OBSERVED). Compile, scalafmt and MiMa would not catch it.
- **#8730.** A `RunnerScriptTest`-style case running the bash script under Git Bash with CRLF files and a plain `-Xmx2G` line, plus a Windows CI job using `shell: bash`. The Windows CI that ran was green.
- **#9060.** A scripted test running `cleanFull` then `compile` or `reload` in the same session, ideally via the sbt client so the server stays up. No unit test, compile, scalafmt or MiMa check would cover it.
- **Common thread.** All three originals had fully green CI. Each regression was in a path the matrix did not exercise: JDK 17 sbtn, Git Bash, same-session `cleanFull`.

## 5. Maintainer response patterns (non-maintainer PRs)

All figures are time from PR open to first maintainer comment, review or merge, taken from the agent reports and combined. The combined n is roughly 50 measurable values, so the medians are INFERRED.

| Sample | n | Median | Notes |
|---|---|---|---|
| Mar–Jun merged | 24 | ~20h | Range 1h–22d; #9253 22.4d, #9337 16.8d (nudge), #9295 7.4d, #8880 4.6d |
| Jul–Oct merged | ~20 | ~9h | Range <1h–3.4d; #9623 3.4d, #9793 ~2.6d |
| Closed-unmerged | 8 with a response | ~12h | Range 7h–15.7d; 9 of 17 had none |
| Combined | ~52 | **~13h** | **p90 ≈ 5–7 days** |

- Of the closed-unmerged PRs, those that got no response at all were mostly small, bare or not linked to an issue. Every one that drew a reply got it within a day, apart from #9725 (5.4d) and #9634 (15.7d).
- Merge times for non-maintainer PRs range from under 1 hour to 36 days, with a median near 1.3 days (Jul–Oct sample).
- **Typical change-request phrasing (paraphrased):**
  - "Can this reuse X?" or "Could we minimize the change to just bug fixes?"
  - "Don't add a new key/command; extend the existing one."
  - "Is there an open issue / problem for this?"
  - "Split this into separate issues and PRs."
  - "How would we know it is fixed?" and "Were you able to reproduce it?"
  - "Make it `private[sbt]`" and "use HedgeHog or Verify".
  - Suggestions are often offered as concrete code suggestions.
- **Phrases that precede a close:**
  - "Superseded by #N" or "closing in favour of #N" (most common, from authors and maintainers alike).
  - "Review the develop PR first" for backports.
  - "No reproducible example."
  - Reversing a performance decision without data.
  - The author's own "not much traction, closing".
- **AI.** AI disclosure is common (about 8 of 11 jozanek PRs and roughly 15 of the merged and closed samples) and drew no maintainer pushback. The one explicit AI reminder was eed3si9n's CONTRIBUTING citation on #9147.
- **CI failing.** Not seen as a close reason. The only CI complaint was the 25-minute timeout on #9864.

## Cross-cutting patterns: top 15 recurring reviewer concerns

Counts are approximate tallies of PRs in the samples where a maintainer raised the concern. Peer reviewers (such as stasimus) are excluded unless noted.

| # | Concern | ≈Count | Example PRs |
|---|---|---|---|
| 1 | Design/direction: reuse existing parser, API or setting instead of adding a new one; don't add a flag | 14 | #9051, #9689, #9623, #9619, #9442 |
| 2 | Scope/size: split, drop unrelated changes, "bug fixes only" | 12 | #9515, #9799, #9434, #9353, #9627 |
| 3 | Correctness bug found in review | 9 | #8880, #9102, #9685, #9353, #9448 |
| 4 | Tests: missing, weak or wrong kind | 9 | #9226, #8880, #9448, #9766, #9725 |
| 5 | Superseded or "is there an issue/open problem?" | 7 | #9627, #9541, #9910, #9772 |
| 6 | Reproduction evidence ("how would we know it is fixed?") | 7 | #9147, #9253, #9102, #9725, #9720 |
| 7 | Public API surface (`private[sbt]` vs public) | 6 | #9293, #9793, #9347, #9864 |
| 8 | Branch targeting / backport policy | 6 | #9623, #9515, #9448, #9903, #8880 |
| 9 | Platform (Windows, APFS, Git Bash) | 5 | #9047, #9448, #9766, #9623, #9434 |
| 10 | Performance trade-offs | 5 | #9870, #9047, #9253, #9725, #9623 |
| 11 | Naming / UI text | 4 | #9901, #9685, #9295, #9442 |
| 12 | Scala style and comments | 4 | #9293, #8880, #9041, #9563 |
| 13 | Binary/behavioural compatibility | 3–4 | #9347, #9442, #9722 |
| 14 | Release notes / docs | 3–4 | #8880, #8866, #9442 |
| 15 | CI/flaky and CLA | 3 | #9864, #9669; CLA on #9364, #9147 |

**Not seen from maintainers in these samples:** fewer-braces, end-marker, `return` and `Using` style objections, commit message format, and an AI-disclosure objection beyond the single reminder on #9147. These items appear in CLAUDE.md but are not what reviewers raised. Authors often include MiMa results and AI disclosure unprompted, which may be why nobody had to ask (INFERRED).

## Reviewer profiles

- **eed3si9n.** Reviewed nearly every sampled PR and merged almost all of them. Focus:
  - Reuse and minimal surface: use existing helpers such as `IO.copyFile` or existing parsers; avoid new keys or commands.
  - Scope discipline: unrelated changes get split out, and he asks for "bug fixes only".
  - Compatibility and API surface: bincompat, `private[sbt]`, and the placement of helpers.
  - Evidence and rule citation: reproductions, test kind (HedgeHog/Verify), and citing contributing-docs rather than restating rules.
  - Quick bare approvals ("Thanks!") on small, well-described PRs.
  - Policy remarks: develop is 2.1.x; backports to 2.0.x are being slowed after regressions.
  - Reverts quickly (about 25 minutes from issue to revert PR) when something breaks.
- **anatoliykmetyuk.** Reviewed ≥3 sampled PRs (#8880, #9685, #9448, #9725, #9689, #9669). Focus on the deepest correctness review: side-effecting code, hard-reset safety, Windows paths with spaces, secrets exposure in diagnostics, ambiguous separators, and performance trade-offs that reverse earlier deliberate decisions. He asks for an end-to-end or integration test over a narrow unit test, and for a reproduction.
- **xuwei-k.** Appeared in the sample mainly as an author or as the finder of the #8730 regression and the author of #9060. He did not review three or more sampled PRs in the data, so no profile.

## Data gaps

- **Closed-unmerged sample.** Jan–Jul 2026 was not sampled, so it covers roughly Jul 13–Oct 18 (19 PRs, not 20). Closers are INFERRED for most, because the payload has no `closed_by`. CI at close was retrieved for few. The "prior issue" column only records whether the body links an issue, which is not proof of maintainer approval.
- **Merged sample.** Both agents lacked commit lists, so review-round counts are approximate. The list endpoint returned no sizes in the Mar–Jun pass, and sizes came from per-PR reads. #9102 had 10 review threads of which only 8 were visible. About a dozen Sept PRs listed above were not opened. Search was rate-limited, so the sample is a paged walk, not a random draw, and may be biased toward recent PRs.
- **Maintainer list.** mkurz is a GitHub MEMBER but not on your maintainer list, so I treated mkurz and SethTisue as non-maintainers. Their comments are therefore not counted as maintainer feedback.
- **jozanek.** I did not check the linked issues for #9728, #9722 and most others for prior maintainer sign-off. The #9744 CI failure reason was not retrievable from the job-log tail.
- **Reverts.** The agent did not read review threads or diffs, so "review rounds" there count review events only. Whether #8730's fix also needed a 1.x launcher change is INFERRED.
- **Time to first response.** The p90 of 5–7 days and the 13h median are my estimates from pooled agent lists. The underlying n is small and mixes merge times with comment times in places.