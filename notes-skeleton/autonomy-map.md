# Autonomy map (per area)

last-verified: 2026-10-18

Levels (how much I decide without a maintainer, beyond the policy's "is this wanted?", which is always settled first):
- **L0 Ask first.** Open question on the issue before any design or code ("is this wanted, and what approach would you accept?").
- **L1 Propose.** I bring a design with a recommendation (`templates/escalation.md`) and wait for an OK before coding.
- **L2 Decide and explain.** I make the design choices and list them in the PR under "Decisions I made, and alternatives".
- **L3 Decide and defend.** As L2, and I hold a position under review with evidence. I may review others' PRs in this area publicly.

Ceilings regardless of evidence (these are maintainers' decisions by nature, as with the article's sensitive paths):
new or changed public API (Keys.scala, anything outside `sbt.internal`) and default or user-visible behaviour
changes: max **L1**. CI workflows, the build (`build.sbt`, `project/`), release, packaging, signing: max **L0**.

## Promotion (all of these, within the area)
- L0 to L1: 1 merged PR or accepted triage/repro in the area, plus explain-back at 100% on it, plus an `architecture/<area>.md` I wrote and that has been verified.
- L1 to L2: 2 merged PRs where the design I proposed was accepted with at most 1 maintainer round each; no repeated correction in the area; I pass a cold quiz (3 questions, no notes) on the area.
- L2 to L3: 3+ merged in the area, at least one design choice I made accepted after discussion; 2 private reviews of others' PRs in the area whose findings a maintainer later confirmed; no revert attributable to me in the last 6 months.

## Demotion (any one)
- A revert or regression traced to my change in the area: drop to L0 for that area until the post-mortem is in `mistakes.md`, then L1.
- The same checklist rule corrected twice in the area: drop one level.
- A maintainer says "please discuss first", or closes as not wanted: L0 for that area.
- 6 months without work in the area, or a major upstream rewrite of it: drop one level and re-verify notes.

## Map

Evidence is from my 11 sbt PRs (to 2026-10-18). Self-assessment, 2026-10-18: "few" of my merged PRs could I defend line by line today. So no area starts above L1: merged code is not evidence of understanding until explain-back passes.

| Area (paths) | Risk | Level | Evidence so far | Next promotion needs |
|---|---|---|---|---|
| Docs: contributing-docs/, notes/ | low | L1 | notes entries in #9344, #9442 | 1 docs PR verified by following it |
| Scripted test infra: scripted-sbt/, sbt-app/src/sbt-test | med | L0 | #9799 open, asked to split | #9799 resolved plus explain-back |
| util-cache, ActionCache | high | L0 | #9619 open, asked to use `IO.copyFile` | #9619 resolved plus explain-back |
| Settings/task DSL and macros: main-settings/, core-macros/, TaskMacro | high | L0 | #9347 (bincompat correction), #9728 merged | retro-learn #9347 and #9728 (explain-back 100%) |
| Project load and state: main/internal/Load, Extracted | high | L0 | #9722 merged (semantics caution), #9744 open, unreviewed | retro-learn #9722 |
| Defaults/Keys (public surface) | high, ceiling L1 | L0 | #9442 (new key dropped), #9744 adds key | retro-learn #9442 |
| Launchers: sbtw/, launcher-package/ | high (reverts #8730, #8464) | L0 | #9434 (trimmed, design correction) | retro-learn #9434 |
| Library management: lm-core/, ivyless publish | high | L0 | #9344, #9814 merged; #9720 closed by design | retro-learn #9344 and #9814 |
| lm-coursier resolution | high | L0 | none | first item |
| Client/server/BSP: main-command/, protocol/, client/, server | high | L0 | none (BSP touched in #9442) | first item |
| Remote cache | high | L0 | none | first item |
| CI/build: .github/, build.sbt, project/ | ceiling L0 | L0 | #9799 touches ci.yml and build | n/a |
