<!--
"Is a contribution wanted?" comment on an issue. LLM_POLICY.md requires
confirming with a maintainer before working on a PR, unless the issue already
carries that confirmation (see OPERATING-MODEL.md Stage 3 for what counts).

Send this only AFTER you have reproduced on develop. A confirmed repro is
the most useful thing in the comment, and is useful even if the answer is no.
-->

I can reproduce this on develop (<sha>) and on sbt <latest 2.x release>:

```
<the 3-10 decisive lines of output, not the whole log>
```

Minimal repro: <inline build.sbt + command, or gist of reproduce.sh>.

<One of:>
- I think the cause is in `<File.scala>` (<function>): <one sentence>. I'd like to fix it with a <unit|scripted> test, around <N> lines. Would a PR be welcome?
- I have not found the cause yet. Before I dig further: is this still behaviour you want changed in 2.x?

Disclosure: I'm using <tool/model> to help investigate.

<!-- If it does NOT reproduce, say so instead, with the version and repro you
used, and ask whether it can be closed. That is a complete, useful
contribution with no PR. -->
