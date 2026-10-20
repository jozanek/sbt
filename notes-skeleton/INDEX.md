# sbt notes: index

last-verified: 2026-10-18
Location: `~/oss/sbt-notes/` (its own private git repo; never inside the sbt clone).
Clone: `~/src/sbt` with remotes `origin` = jozanek/sbt (fork), `upstream` = sbt/sbt.

## Read at the start of every work item (in this order, and only these)
1. `items/<active>.md`: where we left off, the findings ledger, open decisions
2. `checklist.md`: review rules C01-C23 (skim the IDs; read rules for the areas touched)
3. `autonomy-map.md`: rows for the areas this item touches
4. `mistakes.md`: the last 5 entries
5. `architecture/<area>.md` for the touched area, only if `last-verified` is under 90 days, otherwise re-verify

## Update at the end of every work item
- [ ] `items/<id>.md`: outcome, explain-back score, ledger closed
- [ ] `metrics.md`: one row
- [ ] `checklist.md`: a new or edited rule for every maintainer correction, logged in the rule log
- [ ] `mistakes.md`: anything I got wrong, plus the rule or gate that now prevents it
- [ ] `architecture/`, `glossary.md`, `conventions.md`: only what I can state in my own words, with anchors
- [ ] `decisions.md`: any maintainer decision, with link
- [ ] `autonomy-map.md`: evidence added; promote or demote per the rules there
- [ ] run `tools/check-anchors.py`; fix or delete CHANGED and GONE anchors

## Files
| File | Holds | Pruning rule |
|---|---|---|
| architecture/map.md | module map, where things live | re-verify yearly or when anchors go stale |
| architecture/<area>.md | my explainers per slice | 90-day `last-verified`; stale anchors fixed or the section deleted |
| glossary.md | sbt terms in my words | merge duplicates; delete anything I can no longer explain |
| conventions.md | "how it's usually done here" | an entry needs 2+ examples in code or review, otherwise it moves to open-questions |
| decisions.md | maintainer decisions and rationale | never pruned; mark superseded |
| reviewers.md | per-maintainer preferences, with evidence | refresh after each quarterly re-mine |
| checklist.md | review rules | rules with poor precision get rewritten or retired (rule log) |
| mistakes.md | my errors and the fix to the system | never pruned |
| open-questions.md | unknowns and harvested pre-existing findings | close or move monthly |
| autonomy-map.md | level per area, with evidence | updated every item |
| metrics.md | one row per item | never pruned |
| items/ | one file per work item | archive to `items/done/` |
| learning/ | predictions, quiz bank | review monthly |

Monthly (15 min): prune per the table, re-run anchors, look at the trends in metrics.md.
