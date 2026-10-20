# Metrics

One row per work item (PR, triage report, or private review). Trends are what matter.
Guardrail (as in the article): if maintainer round trips or regressions go up while autonomy goes up,
autonomy came too early. Tighten.

Definitions:
- **MRT**: maintainer round trips. Maintainer reviews or comments that required a change from me.
- **Corr**: checklist rule IDs maintainers corrected. A rule appearing in two items is a **repeat** (target: 0).
- **1st resp / merge**: days from open to first maintainer response / to merge or close.
- **Up-CI**: red upstream CI runs before green (target: 0; fork CI should catch them first).
- **SR**: self-review rounds; findings by verdict fixed/wrong/intentional/don't-matter (reviewer precision = fixed / all).
- **EB**: explain-back score, non-test hunks I explained unaided / total (target: 100% before sending).
- **Pred**: prediction hit rate in this item (where I guessed the cause or mechanism before reading).
- **New concepts**: glossary/architecture entries added *and verified*.
- **Usage**: rough Claude usage for the item (from `/usage`), so the cost per item is visible.
- **Regress**: a regression or revert within 60 days (guardrail).

## Baseline: my 11 sbt PRs before this model (from the 2026-10-18 sweep)

| PR | Area | Non-test / test lines | Outcome | Days | MRT | Corr | AI disclosed |
|---|---|---|---|---|---|---|---|
| 9344 | lm-core | 52 / 144 | merged | 1 | 0 | none | yes |
| 9347 | main-settings | 17 / 30 | merged | 67 | 1-2 | C09, C03 | yes |
| 9434 | sbtw | 304 / 241 | merged | 33 | 1-2 | C02, C03 | **no** |
| 9442 | Defaults/BSP | 81 / 77 | merged | 14 | 1 | C10, C02 | yes |
| 9619 | util-cache | 47 / 50 | open, 62d | n/a | 1 | C02 | yes |
| 9720 | commands | ~190 total | closed (by design) | 23 | 1 | C01 | yes |
| 9722 | Extracted | 24 / 145 | merged | 3 | 0 maint (1 peer) | C10 (caution), C11 (peer) | yes |
| 9728 | TaskMacro | 66 / 274 | merged | ~2 | 0 | none | **no** |
| 9744 | Load/Keys | 45 / 140 | open, 37d+, red job 1 (scalafmt in merge run), unreviewed | n/a | 0 | n/a | **no** |
| 9799 | scripted/CI | 123 / 144 | open, 28d, green | n/a | 1 | C03 | yes |
| 9814 | lm-core publish | 139 / 460 | merged | 0 | 0 | none | yes |

Baseline signals: **repeats already present** (C02 four times, C03 three times, C10 twice). Disclosure was missing on 3 of 11.
No EB, Pred or Usage data (not measured before). Self-assessed explainability: "few".
Project context: median first maintainer response ~13h, p90 ~5-7d; one maintainer (eed3si9n) reviews almost everything.

## Items

| Date | Item | Kind | Area | Lvl | Non-test/test | Outcome | 1st resp | Days | MRT | Corr (repeat?) | Up-CI | SR rounds / precision | EB | Pred | New concepts | Usage | Regress |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
