# <issue#>-<slug>

kind: bug-fix | test | docs | triage | private-review | retro-learn
area: <autonomy-map row>   level at start: L?
issue: https://github.com/sbt/sbt/issues/<n>   PR: <n or none>
started: YYYY-MM-DD   closed: YYYY-MM-DD   outcome: merged | closed | parked | report-only

## S0 Selection (why this one)
- still valid on develop @ <sha>: <evidence>
- claimed or covered? <search: open PRs mentioning #n; assignees; recent "I'll take this">
- blast radius: <who is affected if I get it wrong>
- risk area? <yes/no, which>
- maintainer responsiveness for similar work: <PR numbers>
- teaches me: <slice>

## S1 Understand and reproduce
- my one-sentence statement of the problem:
- repro: `local-temp/issues/<n>-<slug>/reproduce.sh`  (sandbox? yes/no)
- verdicts: direct <ver>: yes|no / bare develop@<sha>: yes|no

## S2 Explore and explain back
- **prediction before reading** (copy to learning/predictions.md): <where and why I think it breaks>
- reading map: <link or paste anchors from sbt-explainer>
- my explanation (own words, 5-10 sentences):
- agent check of my explanation: correct / wrong at <anchor>, because <evidence>
- prediction hit? yes / partly / no

## S3 Maintainer decision?
- decision vs information: <which list item from AGENT.md, or "none">
- wanted signal: <link to maintainer comment / label / none>
- message sent (by me): <link>, date; answer: <link>, date

## S4 Work under gates
- failing test first: <name>, failure output on develop@<sha> (3-10 lines)
- gates: compile [ ] Test/compile [ ] scalafmtCheckRepo [ ] mima [ ] testOnly [ ] scripted [ ] contraband [ ] headers [ ] JDK17 [ ] size-check <result>
- real-session smoke test (C15), if launcher/client/clean/boot: <what I ran>
- who wrote the core hunk: me / agent (L0-L1 areas: me)
- hunk purposes (C03): one line per non-test hunk

## S5 Self-review ledger
| Round | SHA reviewed | ID | Sev | file:line | Finding | My verdict (fixed/wrong/intentional/doesn't matter) |
|---|---|---|---|---|---|---|

- explain-back: <explained>/<total> non-test hunks. Unexplained hunks: <list> (they block sending)

## S6 Submission
- fork CI run (same SHA as PR head): <link> green?
- PR text: `PR.md` here; disclosure present [ ]; Generated-by in part 1 [ ]

## S7 Feedback
<table from templates/feedback-reply.md>

## S8 Close-out
- notes updated: <files>
- rules added or changed: <IDs>
- metrics row added [ ]
- quiz questions for +3 days: 1) 2) 3)
