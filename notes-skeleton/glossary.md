# Glossary (in my own words)

Rule: I write the definition. The agent may only check it against code and mark it right, or wrong with
an anchor. Delete anything I can no longer explain at a monthly review.

Format:
**Term**: my definition (2-3 sentences). Anchor: `path:line@sha`. Verified: YYYY-MM-DD. Confused with: <term>.

## To define first (they appear in my merged PRs, so I already shipped code that depends on them)
- Setting vs Task vs InputTask
- `Def.Initialize[A]` and `Def.Initialize[Task[A]]`
- Scope and its axes; `Zero`, `This`, `ThisBuild`; delegation
- `Extracted`, `State`, `BuildStructure`
- `.value` macro expansion (TaskMacro); "task-local" / illegal dynamic reference
- `Def.taskDyn`
- `Project` vs `ProjectRef` vs `ProjectReference`; aggregation
- fork, `baseDirectory`, working directory
- Patterns / Ivy resolver patterns, `[organisation]` vs `[orgPath]`
- action cache, dirzip, CAS
