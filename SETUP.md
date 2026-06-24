# Setup Guide

Complete as much as you can before the Padova workshop. If something fails,
still attend; the session is designed so you can follow the demos and complete
Markdown artifacts even with partial setup.

## Quick Checklist

- [ ] Git installed and configured.
- [ ] GitHub account available.
- [ ] Python 3.10 or later installed.
- [ ] Node.js 20 or later installed if you want Playwright codegen or the
      TypeScript path.
- [ ] One main agentic coding tool installed: Codex, Claude Code, or Cursor.
- [ ] This repository opens locally.
- [ ] You can read `START_HERE.md`, `SCHEDULE.md`, and `GUIDE.md`.

## Get The Repository

```bash
git clone <course-repository-url>
cd AC4E_Padova
```

If you received a folder directly, open a terminal in it and confirm:

```bash
pwd
ls
```

You should see `README.md`, `START_HERE.md`, `SCHEDULE.md`, `GUIDE.md`,
`materials/`, `examples/`, and `templates/`.

## Python

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
```

Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Node.js And Playwright

```bash
node --version
npm --version
npm install
npx playwright install chromium
```

The Python Playwright path is enough for the live demo. Node.js is useful for
Playwright codegen and TypeScript examples.

## Choose One Agentic Coding Tool

You do not need every tool. Pick the one you will use during the session.

| Lane | Tool | Use when |
| --- | --- | --- |
| A1 | Codex CLI | Terminal-first workflow |
| A2 | Codex app | Desktop app workflow |
| B1 | Claude Code CLI | Terminal-first Claude workflow |
| B2 | Claude Code app | Desktop Claude workflow |
| C | Cursor | IDE-first workflow |

Tool surfaces change quickly. For all installs, use the official docs in
[`docs/sources.md`](docs/sources.md) and verify labels, commands, and feature
availability in your installed version.

## Codex

Official references:

- Codex docs: <https://developers.openai.com/codex/>
- AGENTS.md guide: <https://developers.openai.com/codex/guides/agents-md/>
- Codex web/cloud: <https://developers.openai.com/codex/cloud/>

CLI path:

```bash
npm i -g @openai/codex
codex --version
codex
```

For the app path, open the project folder in the Codex desktop app and start
with a read-only prompt:

```text
Read README.md, START_HERE.md, and SCHEDULE.md. Do not edit files. Tell me what
I should do first in this workshop.
```

## Claude Code

Official references:

- Overview: <https://code.claude.com/docs/en/overview>
- Settings: <https://code.claude.com/docs/en/settings>
- Skills: <https://code.claude.com/docs/en/skills>
- Subagents: <https://code.claude.com/docs/en/sub-agents>
- Hooks: <https://code.claude.com/docs/en/hooks>

Install from the official setup page for your platform, then verify:

```bash
claude --version
claude
```

Start with a read-only prompt:

```text
Read README.md and GUIDE.md. Do not edit files. Explain the Padova workshop path.
```

## Cursor

Official references:

- Docs landing: <https://cursor.com/docs>
- CLI: <https://cursor.com/docs/cli/overview>
- Rules and AGENTS.md: <https://cursor.com/docs/rules>
- Skills: <https://cursor.com/docs/skills>
- Subagents: <https://cursor.com/docs/subagents>
- Hooks: <https://cursor.com/docs/hooks>
- MCP: <https://cursor.com/docs/mcp>

Install Cursor, open this repository, and let indexing finish. If you use the
CLI path, verify:

```bash
cursor --version
```

Start with a read-only prompt:

```text
Read START_HERE.md and examples/starter_article/README.md. Do not edit files.
List the first three workshop actions.
```

## Verify Setup

Run this if dependencies are available:

```bash
python3 scripts/validate_setup.py
```

It is acceptable if optional tools you did not choose are missing. For example,
a Cursor participant does not need Codex or Claude commands installed.

## Privacy Boundary

Do not put API keys, confidential data, restricted microdata, or private
manuscripts in this repository. The `.gitignore` excludes common local folders
such as `.venv/`, `data/`, `outputs/`, and `.env` files. Keep raw or restricted
data outside agent context unless you have explicit permission and a safe local
workflow.
