<!--
Escalation message: one per real decision, posted by you, on the issue (or
the PR if one already exists), BEFORE writing more code. Not Discord DMs:
the decision should live next to the issue so it is findable later.

Gate before sending (all must be true; see OPERATING-MODEL.md, Step 4):
[ ] It is a decision, not information (it depends on maintainers' intent,
    priorities, compatibility policy or future plans).
[ ] I ran the ladder: code search, blame/log, docs, past PRs, similar change,
    fresh-context agent. Nothing settles it.
[ ] I can name 2-3 concrete options and the cost of each.
[ ] I have a recommendation and can defend it.
[ ] The question can be answered with a letter or a word.
-->

**Question for maintainers:** <one sentence, closed: "Should X do A or B?">

Context: <1-2 sentences. Link the repro or the failing test, not a wall of logs.>

Options:
- **A (recommended).** <what it means for users>. Cost: <lines, compat, risk>.
- **B.** <...>. Cost: <...>.
- **C. Leave as is.** <why this might be right too>.

What I already checked: <blame/PR that introduced the behaviour (#NNNN),
related decision or discussion, how sbt 1.x behaves, MiMa result if relevant>.

If A is fine, the PR would be about <N> lines plus a <unit|scripted> test.
I won't open it until one of you confirms.

<!-- Do not add "I'll proceed unless you object". An outside contributor
does not get to set a default for maintainers. -->
