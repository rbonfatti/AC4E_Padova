#!/usr/bin/env python3
"""Claude Code hook example: add economics research safety context."""

from __future__ import annotations

import json

print(
    json.dumps(
        {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": (
                    "Economics research safety reminder: do not process "
                    "confidential manuscripts, private raw data, secrets, or "
                    "credentials unless the user explicitly confirms permission."
                ),
            }
        }
    )
)
