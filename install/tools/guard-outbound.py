#!/usr/bin/env python3
"""PreToolUse hook for Bash: block anything that publishes or writes to GitHub.

Install: ~/oss/sbt-notes/tools/guard-outbound.py (chmod +x), referenced by an
absolute path from <clone>/.claude/settings.local.json. Exit code 2 blocks the
call and shows stderr to the agent.

This is a guard rail, not a security boundary: a determined command can evade
any regex. The hard boundary is credentials: give agent sessions a read-only
GH_TOKEN and push from your own terminal.
"""
import json
import re
import shlex
import sys

BLOCK = [
    (r"\bgit\b(\s+-\S+(\s+\S+)?)*\s+push\b", "git push"),
    (r"\bgit\b.*\bremote\s+(add|set-url)\b", "changing git remotes"),
    (r"\bgh\s+(pr|issue)\s+(create|comment|review|merge|close|reopen|edit|ready|lock|unlock|delete)\b",
     "gh pr/issue write"),
    (r"\bgh\s+(release|repo\s+(fork|create|delete|edit|sync|rename|archive)|workflow\s+(run|enable|disable)|run\s+(rerun|cancel|delete))\b",
     "gh repo/workflow write"),
    (r"\bgh\s+(gist|label|secret|variable)\s+(create|edit|delete|set|clone)\b", "gh write"),
    (r"\bgh\s+api\b.*(\s-X\s*|--method[\s=])(POST|PATCH|PUT|DELETE)\b", "gh api write method"),
    (r"\bgh\s+api\b.*(\s-f\s|\s-F\s|--field\b|--raw-field\b|--input\b)", "gh api with body (implies POST)"),
    (r"\bcurl\b.*(-X\s*|--request\s+)(POST|PATCH|PUT|DELETE)\b.*\bgithub\.com\b", "curl write to GitHub"),
    (r"\bcurl\b.*\bgithub\.com\b.*(-X\s*|--request\s+)(POST|PATCH|PUT|DELETE)\b", "curl write to GitHub"),
]


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    if payload.get("tool_name") != "Bash":
        return 0
    cmd = payload.get("tool_input", {}).get("command", "")
    flat = " ".join(cmd.split())
    for pattern, label in BLOCK:
        if re.search(pattern, flat):
            print(
                f"Blocked ({label}). Hard rule: the agent never publishes. "
                f"Print the exact command for Jozef to run instead:\n  {shlex.quote(cmd)}",
                file=sys.stderr,
            )
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
