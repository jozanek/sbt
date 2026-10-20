<!--
PR description template for sbt/sbt. sbt has no PR template in the repo
(checked .github/ and the repo root on develop, 2026-09-17 and 2026-09-22),
so this follows CONTRIBUTING.md's commit-message guideline and LLM_POLICY.md.

Why two parts: maintainers often squash-merge. Your merged commits' bodies
look like PR descriptions. So part 1 must read well as a commit message on
its own, and part 2 is reviewer-only material a maintainer can drop at merge.

Commit-message guideline (CONTRIBUTING.md on develop, read 2026-10-20; 10 items,
changed 2026-10-04 in 1d53696). Part 1 below, and every commit on the branch, must:
  - subject: optional [2.x]; type fix|feat|refactor|test|ci|deps; imperative mood
  - for a fix, name the problem fixed, not how ("Fix task output lost by the thin
    client", not "Subscribe the channel before reading")
  - body: Problem and Solution sections, a few lines each; details go in the PR
    description (part 2), not the commit
  - plain prose, NO backticks; no @-mentions; end with Generated-by: <tool (model)>

Delete these comments before sending. You, not the agent, send it.
-->

**Problem**
<!-- 2-4 sentences: observable behaviour, who hits it, on which sbt version.
Facts vs opinion kept apart (CONTRIBUTING "Reporting Issues"). -->

**Solution**
<!-- 2-4 sentences: what changes, and why this is the smallest change that
fixes it. Name anything you deliberately did NOT do and why. -->

Fixes #NNNN

Generated-by: <tool and model, e.g. Claude Code (Claude Sonnet 5.5)>

---

<details>
<summary>Reviewer notes (not for the commit message)</summary>

**Was this wanted?** <!-- link to the maintainer comment that confirmed it, or the label -->

**Reproduction.** `local-temp/issues/NNNN-slug/reproduce.sh`, run before and after:

```
before (sbt <affected version>, --direct):  REPRODUCED: yes
before (develop @ <sha>, bare):             REPRODUCED: yes
after  (this branch @ <sha>, bare):          REPRODUCED: no
```

**Test that proves it.** `<test name>` fails on `develop @ <sha>` with
`<one-line failure>`; it passes on this branch.

**Local checks run** (JDK <17|21|25>, <OS>):
`compile`, `Test/compile`, `scalafmtCheckRepo`, `mimaReportBinaryIssues`,
`<module>/testOnly <...>`, `scripted <group/test ...>`, plus `<anything else>`.
Fork CI: <link to green run on the same head SHA>.

**Where to look.** <!-- the 1-3 hunks that carry the change, in reading order;
everything else is tests/plumbing -->

**Risk and how to undo.** <!-- blast radius (which users/builds), behaviour or
default changes, bincompat (MiMa clean? new public API?), and "revert this
commit" or anything more. If it changes a default or user-visible behaviour,
link the notes/2.x/*.md entry. -->

**AI disclosure.** I used <tool/model> to <what: reproduce, explore, draft
tests, draft code, draft this text>. I ran every check above myself and can
explain each change.

</details>
