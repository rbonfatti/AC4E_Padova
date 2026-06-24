# Claude Code App Track (Lane B2)

Same Claude project files as CLI: `CLAUDE.md`, `.claude/skills/`,
`.claude/agents/`, `.claude/settings.json`, `.claude/hooks/`, and `.mcp.json`.
Differences are UI and session/checkpoint handling.

## Setup

1. Code tab → project folder = your `starter_article` copy.
2. Merge files per [`../claude/README.md`](../claude/README.md).
3. Invoke skills from the `/` menu or prompt by name; invoke subagents by name.

## Surface notes

- Use app sessions and checkpoints for app work. Use `claude --continue` only for
  CLI sessions unless you intentionally hand off through an official command.
- UI labels and feature availability are version-sensitive; verify in the
  installed app and official docs.

See [`docs/research_article_harness.md`](../../docs/research_article_harness.md).
