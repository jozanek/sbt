# sbt contributor operating model: files and install

Start with `OPERATING-MODEL.md` (Step 0 report, flow map, stage specs, shortlist, rollout).
Nothing here goes into the sbt repo as a tracked file.

## What's here

| Path | Install to | Purpose |
|---|---|---|
| OPERATING-MODEL.md | `~/oss/sbt-notes/OPERATING-MODEL.md` | the model |
| install/AGENT.md | `~/oss/sbt-notes/AGENT.md` | standing instructions every session loads |
| install/settings.local.json | `~/src/sbt/.claude/settings.local.json` | deny rules and the guard hook (fix the path inside) |
| install/tools/guard-outbound.py | `~/oss/sbt-notes/tools/` | blocks publish and write commands (tested: 10 block cases, 7 allow cases) |
| install/tools/size-check.sh | `~/oss/sbt-notes/tools/` | non-test size vs. merged outside PRs (tested on your branches) |
| install/tools/check-anchors.py | `~/oss/sbt-notes/tools/` | finds stale `path:line@sha` anchors (tested) |
| install/tools/mine-reviews.sh | `~/oss/sbt-notes/tools/` | quarterly re-mine of review comments with your `gh` (syntax-checked, not run) |
| install/agents/*.md | `~/.claude/agents/` | sbt-fresh-reviewer (opus), sbt-explainer (sonnet), sbt-log-triage (haiku) |
| templates/*.md | `~/oss/sbt-notes/templates/` | PR description, escalation, wanted-check, feedback reply |
| notes-skeleton/ | `~/oss/sbt-notes/` | notes folder, seeded with the checklist, reviewers, decisions, metrics baseline, autonomy map |

## Install (about 30 minutes; you run all of it)

```bash
# 1. Notes repo, outside the clone, versioned privately
mkdir -p ~/oss/sbt-notes && cp -r notes-skeleton/. ~/oss/sbt-notes/
cp OPERATING-MODEL.md install/AGENT.md ~/oss/sbt-notes/
cp -r templates install/tools ~/oss/sbt-notes/ && chmod +x ~/oss/sbt-notes/tools/*
git -C ~/oss/sbt-notes init && git -C ~/oss/sbt-notes add -A && git -C ~/oss/sbt-notes commit -m "seed"

# 2. Clone hygiene (your clone: ~/src/sbt)
cd ~/src/sbt
git remote add upstream https://github.com/sbt/sbt.git 2>/dev/null; git fetch upstream
git config remote.origin.pushurl DISABLED-use-explicit-url    # agent can't push by accident;
git config remote.upstream.pushurl DISABLED                     # you push: git push git@github.com:jozanek/sbt.git HEAD
printf 'CLAUDE.local.md\n.claude/\nlocal-temp/\n' >> .git/info/exclude
echo '@~/oss/sbt-notes/AGENT.md' > CLAUDE.local.md              # approve the external import once

# 3. Guard rails
mkdir -p .claude && sed "s#/home/REPLACE_ME#$HOME#" /path/to/install/settings.local.json > .claude/settings.local.json
mkdir -p ~/.claude/agents && cp /path/to/install/agents/*.md ~/.claude/agents/

# 4. Verify (inside claude): /context lists CLAUDE.local.md and AGENT.md; /hooks lists the guard;
#    ask the agent to run `git push` and confirm it's blocked; `git status --porcelain` is empty.
```

**The only hard boundary is credentials.** Deny rules and the hook are guard rails (the docs note
`git -C . push` slips past deny rules; the hook catches it, but no regex is complete). For agent sessions, export a
fine-grained GitHub token with read-only access to public repos as `GH_TOKEN`. Push from your own terminal.
For a true boundary, run agent sessions as a separate OS user, or in a container without your SSH key.

## Sandbox for untrusted builds (untested on your machine)

Issue repro builds and other people's PR branches are code that sbt runs on load.

```dockerfile
# ~/oss/sbt-notes/sandbox/Dockerfile
FROM eclipse-temurin:17-jdk
RUN apt-get update && apt-get install -y --no-install-recommends curl git ca-certificates \
 && rm -rf /var/lib/apt/lists/*
ARG SBT_RUNNER_VERSION   # pick the current runner from https://github.com/sbt/sbt/releases
RUN curl -fsSL "https://github.com/sbt/sbt/releases/download/v${SBT_RUNNER_VERSION}/sbt-${SBT_RUNNER_VERSION}.tgz" \
  | tar xz -C /opt && ln -s /opt/sbt/bin/sbt /usr/local/bin/sbt
RUN useradd -m runner
USER runner
```

```bash
docker build --build-arg SBT_RUNNER_VERSION=<x.y.z> -t sbt-sandbox ~/oss/sbt-notes/sandbox
# --direct mode (affected release): only the repro folder is mounted; caches are inside it (per SKILL.md)
docker run --rm -it --cap-drop ALL --security-opt no-new-privileges --memory 6g \
  -v "$PWD/local-temp/issues/<id>-<slug>:/work" -w /work sbt-sandbox ./reproduce.sh --direct
# bare mode: run publishLocalBin on the host (trusted sbt code), then mount the published snapshot read-only:
#   -v "$HOME/.ivy2/local:/home/runner/.ivy2/local:ro"   (adjust if publishLocalBin writes elsewhere)
```

Fallback: a Claude Code cloud session as the sandbox. That's convenient but costs subscription usage.

## Running a work item (prompts you can paste)

- "Session start per AGENT.md. Here is `gh pr list -R sbt/sbt --author @me --json number,state,statusCheckRollup`: <paste>"
- "S0 for #9033: fill the S0 fields in a new item file."
- "S1: build the repro per SKILL.md; run --direct in the sandbox."
- "S2: ask me for a prediction first, then run sbt-explainer on <symbol>."
- "S4: write the failing test and show its failure on develop. I'll write the fix in <file>."
- "S5: run sbt-fresh-reviewer round 1 on this branch for #9033."
- "Explain-back: walk me through each non-test hunk."
- "S8: draft the close-out; I'll write the explanations."

## Research sessions used for Step 0

Two read-only cloud sessions read upstream sbt/sbt (this session could only reach your fork): "sbt upstream
review mining (read-only)" and "sbt upstream work discovery (read-only)". Their usage meters showed about
$3.70 and $1.20. Their reports are folded into OPERATING-MODEL.md and the notes. You can archive both.
