#!/usr/bin/env python3
"""Find stale code anchors in the notes, so notes don't quietly rot.

An anchor is `path/to/File.scala:123@abc1234` (line optional). For each one:
  GONE    the file no longer exists on the base ref
  CHANGED the file changed between the anchor's SHA and the base ref
  OK      unchanged
Also flags notes whose `last-verified:` date is older than --max-age days.

Usage: check-anchors.py --repo ~/src/sbt --notes ~/oss/sbt-notes [--base upstream/develop] [--max-age 90]
"""
import argparse
import datetime
import pathlib
import re
import subprocess

ANCHOR = re.compile(r"`?([\w./-]+\.(?:scala|java|sbt|md|sh|yml|json|contra))(?::(\d+))?@([0-9a-f]{7,40})`?")
VERIFIED = re.compile(r"^last-verified:\s*(\d{4}-\d{2}-\d{2})", re.M)


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--notes", required=True)
    ap.add_argument("--base", default="upstream/develop")
    ap.add_argument("--max-age", type=int, default=90)
    a = ap.parse_args()
    if git(a.repo, "rev-parse", "-q", "--verify", a.base).returncode != 0:
        a.base = "origin/develop"
    today = datetime.date.today()
    counts = {"OK": 0, "CHANGED": 0, "GONE": 0, "UNKNOWN-SHA": 0}
    for note in sorted(pathlib.Path(a.notes).expanduser().rglob("*.md")):
        text = note.read_text(encoding="utf-8")
        m = VERIFIED.search(text)
        if m and (today - datetime.date.fromisoformat(m.group(1))).days > a.max_age:
            print(f"OLD      {note}  last-verified {m.group(1)}")
        for path, line, sha in set(ANCHOR.findall(text)):
            if git(a.repo, "cat-file", "-e", f"{sha}^{{commit}}").returncode != 0:
                status = "UNKNOWN-SHA"
            elif git(a.repo, "cat-file", "-e", f"{a.base}:{path}").returncode != 0:
                status = "GONE"
            elif git(a.repo, "diff", "--quiet", sha, a.base, "--", path).returncode != 0:
                status = "CHANGED"
            else:
                status = "OK"
            counts[status] += 1
            if status != "OK":
                loc = f"{path}:{line}" if line else path
                print(f"{status:8} {note.name}: {loc}@{sha}")
    print(" ".join(f"{k}={v}" for k, v in counts.items()))


if __name__ == "__main__":
    main()
