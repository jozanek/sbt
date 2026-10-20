# Handoff: sbt contributor operating model

Planning session, 2026-10-18 to 2026-10-20: https://claude.ai/code/session_01RaX7mTThdSAJFhcysP5sX9
Owner: Jozef Koval (`jozanek`). Read this first, then `README.md`, then `OPERATING-MODEL.md`.

## What was asked
An operating model for contributing to sbt/sbt as an outside contributor, with agents doing most of the
reading and checking locally and Jozef "on the loop". Maintainer attention is spent only on decisions only
maintainers can make, and every work item must leave Jozef understanding the codebase better. The brief used
the Claude Code team's review article as inspiration, adapted to an outsider with a limited token budget.

## What exists (this branch)
This branch has no shared history with sbt's `develop` and is not meant to be merged anywhere.

| Path | What |
|---|---|
| `OPERATING-MODEL.md` | Step 0 report, flow map, stage specs (S0-S9), work shortlist, escalation, autonomy, knowledge system, rollout, metrics, assumptions, self-check questions |
| `install/` | `AGENT.md` (standing instructions), `settings.local.json` and `tools/guard-outbound.py` (no-publish guard), `tools/size-check.sh`, `tools/check-anchors.py`, `tools/mine-reviews.sh`, `agents/` (fresh reviewer, explainer, log triage) |
| `templates/` | PR description (follows the 10-item commit guideline), escalation, wanted-check, feedback reply |
| `notes-skeleton/` | seed for `~/oss/sbt-notes/`: checklist C01-C23, reviewers, decisions, conventions, mistakes, metrics baseline, autonomy map, glossary, item template, learning logs |
| `evidence/` | raw review sweep (2026-10-18) and reviewer calibration (2026-10-20) |

## Decisions Jozef made (2026-10-20)
1. No WIP cap. New work doesn't pause. Ordering rule: red CI or unanswered feedback on an open PR comes first.
2. Jozef writes the core change himself in L0-L1 areas ("I want to learn").
3. #9799 waits.
4. Merged PRs stay as they are. The AI disclosure is added to the open #9744 only.

## Facts established (as of 2026-10-20)
- Policy: upstream #9807 (2026-09-22) added `LLM_POLICY.md`: disclose all AI use, small PRs in scope and lines,
  confirm "wanted" with a maintainer first, stricter enforcement for AI-assisted PRs. The commit guideline
  changed 2026-10-04 (1d53696): a fix's subject names the problem fixed; short Problem/Solution; plain prose
  without backticks; details in the PR description; Generated-by.
- Reviewer concerns, ranked: reuse don't add (~14), scope/split (~12), correctness (~9), tests (~9). Jozef's own
  repeated corrections: C02 reuse (x4), C03 scope (x3).
- Open PRs (no activity on any since 9/22):
  - **#9744**: red job 1 = `scalafmtCheckAll` on `main/src/main/scala/sbt/internal/Load.scala` in the upstream
    merge run (fork CI ran the unmerged branch and passed). No review, no AI disclosure.
  - **#9619**: eed3si9n's changes-requested review (8/17) is still the latest.
  - **#9799**: green, waiting.
- Shortlist caveats: #9033 had a maintainer PR (#9034) that was closed, so read why first. #9042 may be intended
  behaviour (the reporter said so), so ask before coding.
- The fork's `develop` is at 2026-09-17 and behind upstream.

## Reviewer calibration (evidence/reviewer-calibration-2026-10-20.md)
Blind, the fresh-context reviewer caught 2 of 3 reverted PRs at the mechanism level (#9060 exactly, #8464 the
JDK 17 socket path). It blocked #8730 for real regressions but missed the reported Git Bash failure. It also
blocked both clean PRs (#9250, #9271), so its severity was set too strictly. The rubric was tightened ("Above
the bar" bucket; Important = concrete breakage, a policy MUST, or C01-C04) but **not re-validated**. Lesson: eval
against a checklist that doesn't name the eval cases. Cost: about 115-160k tokens per opus review.

## Next actions (in order)
1. **Install** per `README.md` (Phase 0). Includes a read-only GH token for agent sessions and the Docker sandbox.
2. **#9744**: explain-back on the `Load.scala` change; then `git fetch upstream && git checkout
   sbt-1224-initial-project && git merge upstream/develop`, `scalafmtAll`, job 1's check commands from the merged
   ci.yml, push, and add the AI-disclosure line to the PR description.
3. **#9619**: explain-back on the remaining `AccessDeniedException` fallback; re-request review.
4. **Retro-learning**: #9722 and #9442 first (prediction, reading map, own explanation, quiz at +3 days).
5. **Re-validate the reviewer** on the same 5 cases once usage allows. Expected: reverts keep Important breakage
   findings; clean cases show no Important findings.
6. **Phase 2 items**: #9189 escalation practice (no code until answered); the doc-lie fix in
   contributing-docs/06_manual_tests.md, or #9162 after retro-learning #9728.

## Not verified
- On Jozef's machine: install steps, Docker sandbox, `mine-reviews.sh` (syntax-checked only).
- Whether a squash merge uses the PR body or the commit messages.
- #9744 formatter cause beyond the log: that upstream's scalafmt setup changed (#9737) is inferred.
- The PR samples were a paged walk under rate limits, not random. The closed-PR sample covers Jul to Oct only;
  Discussions were unreadable.

## Constraints for whoever picks this up
- Hard rules in `install/AGENT.md`: the agent never posts, comments, pushes or opens PRs. It drafts; Jozef sends.
  No tracked files are added to sbt PR branches. Untrusted builds run in the sandbox. Disclose AI use.
- The push of *this notes branch* to the fork was an explicit one-off request (2026-10-20). It doesn't change the rule.
- Budget: Claude Code subscription; the 7-day usage limit showed a warning on 2026-10-20. Use haiku/sonnet for bulk
  reading; opus only for round-1 review of risky diffs.

## Environment notes
- That cloud session's GitHub access covered only `jozanek/sbt`. Upstream couldn't be attached because of a
  same-name collision. Upstream reads went through three read-only cloud sessions sourced from sbt/sbt ("review
  mining", "work discovery", "status check"; about $3.70, $1.20 and $0.64 on their meters). They can be archived.
- Locally, run Claude Code in the clone. `gh` with Jozef's auth replaces those sessions.
