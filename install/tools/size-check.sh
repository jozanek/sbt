#!/usr/bin/env bash
# Non-test change size of the current branch vs. its merge-base with develop,
# compared with merged outside-contributor PRs (sbt/sbt, 2026-01..2026-09,
# n=332): non-test lines p50=19, p75=62, p90=137; test lines p50=28, p75=76.
# Re-derive these yearly from history; they drift.
# Usage: size-check.sh [base-ref]   (default: upstream/develop, else origin/develop)
set -euo pipefail
base=${1:-}
if [[ -z "$base" ]]; then
  if git rev-parse -q --verify upstream/develop >/dev/null; then base=upstream/develop; else base=origin/develop; fi
fi
mb=$(git merge-base "$base" HEAD)
git diff --numstat "$mb" HEAD | awk -v P75=62 -v P90=137 '
  $1 == "-" { next }
  { n = $1 + $2; f = $3 }
  f ~ /(\/src\/test\/|sbt-test\/|server-test\/|Test\.scala$|Spec\.scala$)/ { t += n; next }
  f ~ /^notes\// { notes += n; next }
  f ~ /^(\.github\/|build\.sbt$|project\/)/ { infra += n; infraf = infraf " " f }
  { src += n; files++ }
  END {
    printf "non-test lines: %d in %d files | test lines: %d | notes: %d\n", src, files, t, notes
    if (infra > 0) printf "CI/build files touched (always a maintainer decision):%s\n", infraf
    if (src > P90) print "OVER p90: split, or get explicit maintainer OK for the size before submitting"
    else if (src > P75) print "Above p75: say in the PR why it cannot be smaller"
    else print "Within p75 of merged outside-contributor PRs"
  }'
