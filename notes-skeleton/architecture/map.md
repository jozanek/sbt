# Module map (where things live)

last-verified: 2026-10-18 (develop @ 2ef94e08, 2026-09-17)
Lines of Scala are non-test, non-scripted. Modules are listed by size. Project ids (for `<id>/testOnly`) come from build.sbt.

| Dir | Project id | Main / test LOC | What lives here (verify in my own words when first touched) |
|---|---|---|---|
| main/ | mainProj | 40,272 / 5,196 | Defaults, Keys, Load, Extracted, commands, server/BSP. The heart, and the highest risk |
| protocol/ | protocolProj | 12,273 / 230 | client/server/BSP protocol types (largely Contraband-generated) |
| internal/util-* | utilCore, utilLogging, ... | 10,341 / 2,092 | logging, completion, control, relation, position |
| lm-core/ | lmCore | 10,003 / 2,850 | library-management API, resolvers, Patterns, ivyless publish |
| main-command/ | commandProj | 5,480 / 1,524 | command engine, State, the shell |
| main-settings/ | mainSettingsProj | 4,926 / 1,857 | the settings/task DSL (Def, Scope, Init) |
| lm-coursier/ | lmCoursier | 4,615 / 1,725 | Coursier-based resolution (CI job 10) |
| util-cache/ | utilCache | 3,175 / 1,438 | action cache, hashing, dirzip |
| main-actions/ | actionsProj | 2,963 / 848 | compile, test, package actions; workers |
| buildfile/ | buildFileProj | 1,563 / 745 | build.sbt parsing and evaluation |
| core-macros/ | coreMacrosProj | 968 / 147 | macro infrastructure |
| tasks/, tasks-standard/ | taskProj, stdTaskProj | 1,093 / 0; 741 / 597 | task engine and standard tasks |
| sbtw/ | sbtwProj | 664 / 240 | Windows launcher (Scala) |
| launcher-package/ | launcherPackage | scripts | sbt / sbt.bat runner scripts, packaging |
| client/ | sbtClientProj | n/a | sbtn thin client |
| scripted-sbt/ | scriptedSbtProj | 1,151 / 0 | scripted test framework |
| sbt-app/src/sbt-test/ | (scripted) | 676 tests in 25 groups | integration tests; 33 marked pending |

Other repos that are part of sbt: sbt/io (`sbt.io`), sbt/zinc (incremental compiler). CI checks both out at develop.
