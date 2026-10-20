#!/usr/bin/env bash
# Pull review data from sbt/sbt into compact JSONL for checklist mining.
# Run it yourself, with an authenticated gh (read-only token is enough). Read-only.
# Usage: mine-reviews.sh <out-dir> [since YYYY-MM-DD] [limit]
# Then ask the agent (haiku subagent) to classify maintainer comments into
# checklist categories; you review the proposed rule changes.
set -euo pipefail
R=sbt/sbt
OUT=${1:?out dir}; SINCE=${2:-$(date -d '-90 days' +%F 2>/dev/null || date -v-90d +%F)}; LIMIT=${3:-80}
MAINT='eed3si9n|xuwei-k|anatoliykmetyuk'
mkdir -p "$OUT"; : > "$OUT/comments.jsonl"

gh pr list -R $R --state merged --search "merged:>=$SINCE -author:app/dependabot" --limit "$LIMIT" \
  --json number,author,title,additions,deletions,changedFiles,createdAt,mergedAt > "$OUT/merged.json"
gh pr list -R $R --state closed --search "is:unmerged closed:>=$SINCE" --limit "$((LIMIT/2))" \
  --json number,author,title,additions,deletions,createdAt,closedAt > "$OUT/closed.json"
gh pr list -R $R --state all --author @me --limit 100 \
  --json number,title,state,additions,deletions,createdAt,mergedAt,closedAt > "$OUT/mine.json"

NUMS=$(python3 -I -c '
import json, sys
ns = set()
for f in sys.argv[1:]:
    ns |= {p["number"] for p in json.load(open(f))}
print(" ".join(map(str, sorted(ns))))' "$OUT/merged.json" "$OUT/closed.json" "$OUT/mine.json")

for n in $NUMS; do
  for ep in "pulls/$n/comments" "issues/$n/comments" "pulls/$n/reviews"; do
    gh api "repos/$R/$ep" --paginate \
      --jq ".[] | select(.user.login|test(\"^($MAINT)\$\")) | {pr:$n, kind:\"${ep%%/*}\", user:.user.login, state:(.state//null), path:(.path//null), line:(.line//null), at:(.created_at//.submitted_at), body:((.body//\"\")[0:1200])}" \
      >> "$OUT/comments.jsonl" || echo "warn: $ep failed" >&2
  done
done
wc -l "$OUT"/comments.jsonl
