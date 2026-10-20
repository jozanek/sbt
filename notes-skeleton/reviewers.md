# Reviewers

last-verified: 2026-10-18 (sweep of 48 merged and 19 closed PRs, Mar to Oct 2026; re-mine quarterly)
These are patterns, not predictions about people. Each line has evidence. Update only from what they actually said.

## eed3si9n (Eugene Yokota), lead; reviews and merges nearly everything
- Reuse over new surface: existing helpers (`IO.copyFile`, #9689 and my #9619), existing parsers (#9051), no new keys or commands (my #9442, #9720).
- Scope: "minimize the change to just bug fixes" (my #9434); split unrelated work (my #9799, #9515).
- Compatibility and placement: `private[sbt]`, helpers out of `Defaults.scala` (#9293, #9793); existing implicits are API (my #9347).
- Evidence: "were you able to reproduce?", "how would we know it is fixed?" (#9147); reproduces perf claims himself before approving (#9253).
- Cites the docs rather than restating rules (CONTRIBUTING on #9147, 03_coding_style on #9293).
- Small, well-described PRs often get a bare approval ("Thanks!") within about a day (about 15 of 48 sampled).
- Branch policy: develop is 2.1.x; 2.0.x backports slowing (#9515, #9448).
- Reverts fast when something breaks (#8557: about 25 min from issue to revert).
- Nudges: stuck PRs moved after polite nudges around day 16-22 (#9253, #9337; my #9434, #9347).

## anatoliykmetyuk (Anatolii Kmetiuk)
- The deepest correctness reviews: side effects, hard-reset safety (#8880); Windows paths with spaces (#9448); last-wins duplicates, ambiguous separators, secrets in diagnostics (#9685).
- Wants end-to-end or integration tests over narrow unit tests, and a reproduction (#9448, #9725).
- Pushes back on reversing earlier deliberate performance decisions without data (#9725).

## xuwei-k (kenji yoshida)
- Mostly an author in the sample; found the #8730 regression via sbt/zinc CI. No reviewing profile yet (fewer than 3 sampled reviews).

## Peers whose reviews have caught real bugs (not maintainers; weigh, don't obey)
- stasimus: found the empty-match bug in my #9722; public API and test-strength points on #9655 and #9904.
