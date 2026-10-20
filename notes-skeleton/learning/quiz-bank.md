# Quiz bank (spaced recall)

Asked 3 days and 3 weeks after an item closes, with no notes and no agent. The agent grades against code.
A question I fail twice becomes an explainer task in open-questions.md.

## Retro-learning set (my merged PRs; answer without looking first)
- #9722: Before the fix, what did `Extracted.runAggregated` fill in when the key named no project, and why did that differ from `runInputTask`? What edge case did a peer reviewer find?
- #9442: Why does forked `run` now inherit sbt's working directory but `test` doesn't? Who could the other choice break?
- #9347: Why did removing the implicit conversion break bincompat, and why does an extension method win member resolution?
- #9728: What makes a reference "task-local" in `sources.all(filter).value`, and at which macro phase is it detected?
- #9344: What does `isMavenCompatible = true` make Ivy do to `[organisation]`, and who is affected by flipping the default?
- #9434: In what order does sbtw resolve the JDK now, and why was single-dash `-java-home` rejected?
- #9814: Why should `publishLocal` overwrite but remote publish not, and what does the HEAD probe "fail open" mean?

| Date asked | Question | Answer quality (0-2) | Note |
|---|---|---|---|
