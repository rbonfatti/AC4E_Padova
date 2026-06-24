#!/usr/bin/env python3
"""Claude Code hook example: remind the agent to report verification evidence."""

from __future__ import annotations

import json
import re
import sys


def _payload_text(payload: dict) -> str:
    tool_input = payload.get("tool_input") or {}
    parts = [
        str(tool_input.get("command") or ""),
        str(tool_input.get("file_path") or ""),
        str(tool_input.get("path") or ""),
    ]
    return " ".join(parts)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        payload = {}

    text = _payload_text(payload)
    patterns = [
        r"\bpytest\b",
        r"\bpython3?\b.*examples/card-krueger",
        r"examples/card-krueger/.+did_analysis\.py",
        r"\blatexmk\b",
        r"\bplaywright\b",
    ]
    if any(re.search(pattern, text) for pattern in patterns) or not text:
        print(
            json.dumps(
                {
                    "systemMessage": (
                        "If this turn changed files or ran verification commands, "
                        "summarize the diff, command result, generated files, and "
                        "remaining risks before claiming completion."
                    )
                }
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
