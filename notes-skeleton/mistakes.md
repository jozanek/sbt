# My mistakes, and what changed so they don't recur

Format: date, what happened (evidence), root cause in my process, the system fix (rule, gate or template), and whether it has recurred since.
Blameless: the question is which check should have caught it.

| Date | What happened | Process root cause | System fix | Recurred? |
|---|---|---|---|---|
| 2026-09-30 | #9720 closed by me after 23 days: maintainer said non-snapshot plugin updating is by design | Built before asking whether it was wanted; a 2014-era issue was not current consent | C01; Stage 3 gate; `templates/wanted-check.md` | |
| 2026-08 to 09 | Asked to shrink or split on #9347, #9434 and #9799 | No size or scope gate before submitting | C03, C04; `tools/size-check.sh` in S4; hunk-purpose list in S5 | C03 repeated 3 times |
| 2026-07 to 09 | New surface rejected or replaced on #9442 (key), #9434 (option), #9619 (hand-written install), #9720 (command) | Didn't search for an existing mechanism; no "what did you reuse?" step | C02; reviewer asks it; any Keys.scala addition triggers Stage 3 | C02 repeated 4 times |
| 2026-07 to 09 | AI disclosure missing on #9434, #9728, #9744 | Disclosure was manual and easy to forget | C18; disclosure in template part 1; reviewer checks it | |
| 2026-09-11 onward | #9744 has sat 37+ days with a red job 1 (scalafmt on Load.scala in the merge run) and no review | Trusted fork CI on the unmerged branch; treated "submitted" as "waiting on maintainers" without checking upstream CI | C17; sync with upstream and `scalafmtAll` before the fork-CI run that counts; session-start check of my open PRs' CI | |
| 2026-10-18 | Can defend "few" of my merged PRs line by line | Agent did the understanding; no explain-back gate | Explain-back gate (S4/S5); retro-learning in rollout | |
