# Syllabus

## Positioning

This 5-hour Padova workshop teaches economists to use coding agents as bounded
research assistants for article work. The goal is not prompt entertainment; it
is a repeatable harness for research files, code, papers, reviews, and
replication evidence.

The session uses the Card-Krueger minimum-wage example as a running case because
it has a clear policy question, public references, and a teachable
difference-in-differences structure.

## Prerequisites

Participants should bring:

- a laptop;
- a GitHub account;
- one main agentic coding tool: Codex, Claude Code, or Cursor;
- Python 3.10 or later;
- Node.js 20 or later if they want the TypeScript Playwright path.

Advanced programming is not required. Comfort with folders, Markdown, and basic
terminal commands helps.

## Learning Outcomes

By the end, participants can:

1. Explain the agent loop: read, plan, act, verify.
2. Scope agent work with allowed files, forbidden files, evidence, and review.
3. Use the Card-Krueger example to draft a project brief and research design
   memo.
4. Install or adapt harness pieces for their tool lane: skills, subagents,
   hooks, optional MCP, loops, and goals.
5. Use GitHub issues, branches, PRs, and cloud agents as an orchestration
   surface.
6. Run or interpret a replication/referee-style verification check.
7. Decide what remains human-owned: identification, confidentiality, data access,
   interpretation, and final claims.
8. Leave with a 7-day adoption plan for one research project.

## Five-Hour Schedule

| Time | Block | Output |
| --- | --- | --- |
| 00:00-00:15 | Orientation and tool lanes | Lane selected |
| 00:15-00:45 | Agent loop and privacy boundary | Scoped read-only prompt |
| 00:45-01:20 | Card-Krueger scaffold | Brief or design memo draft |
| 01:20-01:30 | Break | Setup reset |
| 01:30-02:15 | Skills, subagents, hooks, optional MCP | Harness component plan |
| 02:15-03:00 | Issues, cloud agents, swarms, loops, goals | Issue or goal prompt |
| 03:00-03:45 | Research sprint | One changed research artifact |
| 03:45-04:30 | Verification and Playwright evidence | Review or evidence log |
| 04:30-05:00 | Transfer and checklist | Adoption plan |

## Tool Stance

The workshop supports five lanes:

- Codex CLI and Codex app;
- Claude Code CLI and Claude Code app;
- Cursor.

The file paths and UI labels differ by tool and version. Version-sensitive
claims link to official documentation in [`docs/sources.md`](docs/sources.md)
or ask participants to verify in the installed version.

## Completion Criteria

A participant has completed the workshop when they can point to:

- a research brief or memo;
- project instructions and privacy boundaries;
- at least one skill, one reviewer role or subagent, and one hook or equivalent
  deterministic reminder;
- one orchestration artifact such as an issue, goal prompt, or cloud-agent task;
- one verification artifact such as a replication note, review log, or
  Playwright evidence row;
- a next-step plan for their own project.
