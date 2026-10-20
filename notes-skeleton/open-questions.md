# Open questions and harvested candidates

Close or move monthly. Pre-existing findings from self-review land here as candidate work, never in the current PR.

## Questions about the project
- [ ] When maintainers squash-merge, does the commit body come from the PR description or the commits? (Affects where Generated-by must live; the template covers both.)
- [ ] Does a "help wanted" or "good first issue" label count as "a maintainer confirmed the contribution is wanted" for LLM_POLICY? Or is an explicit comment expected? Watch how maintainers respond (see the work-discovery sweep, section 6).
- [ ] Why are 33 scripted tests `pending`? (`ls -d sbt-app/src/sbt-test/*/*/ | while read d; do [ -f "$d/pending" ] && echo $d; done`). For each, check `git log --follow -- <dir>/pending` for the reason before running it.
- [x] #9744 job 1 red: `scalafmtCheckAll` on `main/src/main/scala/sbt/internal/Load.scala` in the upstream merge run (answered 2026-10-20).
- [ ] Why was xuwei-k's #9034 (for #9033) closed? Read before picking #9033.

## Harvested candidates (pre-existing findings, TODOs, doc lies)
- [ ] contributing-docs/06_manual_tests.md: 2.x doc shows a `1.1.2-SNAPSHOT` example and an sbt 1.2/Scala 2.12 `sbtOn` transcript (lines 13, 57-65 @ 2ef94e08). Verify by following the doc on develop.
- [ ] 96 TODO/FIXME in main code (40 in main/). Triage only with blame context; many are intentional.

## My knowledge gaps (turn into Stage 2 explainers)
- [ ] Settings vs tasks vs input tasks; `Def.Initialize`; how `.value` is rewritten by TaskMacro
- [ ] Scope axes (project, config, task) and delegation; what `Extracted` resolves
- [ ] Load phases: from build.sbt to `BuildStructure`
- [ ] sbt 2 action cache and remote cache; what is hashed
- [ ] sbtn / client-server handshake; BSP
- [ ] ivyless publishing path (GenericPublisher) vs Coursier resolution
