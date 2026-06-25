# Final Readiness Review

Date: 2026-06-25.

Issue: #15, final participant-usability and workshop-sequence gate for the
5-hour Padova delivery.

## Scope And Method

This review was first delegated to Codex cloud from issue #15, but no connector
worker response appeared after the trigger. The review was completed locally as
the approved fallback on branch `review/15-final-coherence`, starting from main
commit `af2add55022fd9c120b1af86c2ff1cebc388fa91`.

Files and evidence inspected:

- `README.md`, `START_HERE.md`, `SETUP.md`, `SCHEDULE.md`, `GUIDE.md`
- `exercises/README.md` and exercises `00` through `07`
- `materials/module_01_foundations.md` through `module_05_capstone.md`
- `materials/tool_tracks.md` and all files in `tool-lanes/`
- `slides/workshop/workshop_slides.tex`, `slides/workshop/workshop_slides.pdf`,
  and `slides/workshop/demo_map.md`
- `examples/card-krueger/`, `examples/starter_article/`, `examples/playwright/`
- `examples/{codex,codex-app,claude,claude-app,cursor}/`
- `agent-harness/{codex,claude,cursor,mcp}/` and `orchestration/`
- `docs/sources.md`, `docs/tool_claims_audit.md`,
  `docs/verification_report.md`, and `docs/research_article_harness.md`

## Blockers

No open blocker remains after this PR.

Blockers found and fixed:

- Root-level `SETUP_pre_course.md` and `SETUP_pre_course.pdf` still contained
  LSE and 4-hour workshop wording. They were participant-facing by location but
  obsolete because `SETUP.md` is the maintained Padova setup guide. Removed both
  files.
- `pandoc_pre_course_preamble.tex` existed only to build the obsolete
  pre-course PDF. Removed it with the stale setup files.
- `docs/inspiration_notes.md` described the material as an LSE workshop. Updated
  it to Padova.
- `docs/import_manifest.md` still listed the obsolete pre-course files as
  included top-level paths and described the Padova adaptation as future work.
  Updated the manifest to record the removal and the completed issue/PR
  sequence.

## Warnings

- Cloud-agent evidence is limited by account quota/tooling availability. Issues
  #13 and #14 recorded Codex usage-limit blocks, and issue #15 did not receive a
  connector response after the trigger. The repository includes local fallback
  reports for those gates.
- Tool surfaces are version-sensitive. `docs/sources.md` and
  `docs/tool_claims_audit.md` were checked on 2026-06-24 and mark Cursor,
  Claude Code, Codex cloud, hooks, goals, and review commands as version/account
  dependent where appropriate.
- Desktop-app sign-in and UI labels cannot be fully verified from repository
  files. Participants should use `SETUP.md` and the lane manuals to confirm
  their installed version.

## Minor Suggestions

- Keep `docs/sources.md` as the single place to refresh official docs before
  future deliveries.
- If the workshop is repeated, regenerate `slides/workshop/workshop_slides.pdf`
  after any schedule or demo-map edits and rerun the verification report checks.
- Consider opening a post-workshop issue for participant feedback, but this is
  not a readiness blocker for the Padova delivery.

## Review Questions

| Question | Result | Evidence |
| --- | --- | --- |
| Can a participant start at `README.md` and know what to do first? | Pass | `README.md` points to `START_HERE.md`, `SETUP.md`, `SCHEDULE.md`, `GUIDE.md`, exercises, tool tracks, Card-Krueger, starter article, and orchestration. |
| Does the 5-hour schedule match slide and exercise order? | Pass | `SCHEDULE.md`, `exercises/README.md`, `slides/workshop/demo_map.md`, and the rendered 37-page PDF follow orientation, foundations/Card-Krueger, harness, orchestration, sprint/verification, transfer. |
| Are all demos discoverable from deck and guide? | Pass | `slides/workshop/demo_map.md` maps each deck section to repo paths; `GUIDE.md` names Card-Krueger, starter article, orchestration, referee/replication, and Playwright prompts. |
| Does every tool lane have a complete harness? | Pass | Inventory found Codex, Claude Code, and Cursor examples with context files, skills, agents/subagents, hooks, MCP config, goals, orchestration, and cloud/background prompts or caveats. |
| Is Card-Krueger used consistently? | Pass | `GUIDE.md`, slides, exercises, `examples/card-krueger/`, tool-lane prompts, and orchestration goals use Card-Krueger as a synthetic teaching workflow and retain the no-causal-claim caveat. |
| Do examples run according to issue #14? | Pass | `docs/verification_report.md` reports dependency install, Card-Krueger analysis/tests, starter analysis/tests, Playwright Python/Node checks, FRED MCP tests/smoke, and slide build. |
| Are official-doc checks represented? | Pass | `docs/sources.md` and `docs/tool_claims_audit.md` cover Codex, Claude Code, Cursor, MCP/FRED/security, Playwright, and GitHub workflow with caveats. |
| Are private/raw data, secrets, follow-up, and website folders absent? | Pass | Final scans found no `followup/`, `follow_up/`, or `website/` directories or tracked files, and no API-key/private-key/absolute-local-path hits. |

## Commands And Static Checks

| Check | Status | Evidence |
| --- | --- | --- |
| Rendered slide inspection | Pass | `pdfinfo slides/workshop/workshop_slides.pdf` reported 37 pages; `pdftotext` found Padova, Card-Krueger, cloud agents, Playwright, verification, and adoption sections. |
| Harness inventory | Pass | Python inventory found Codex: 6 skills/4 agents; Claude Code: 6 skills/7 agents; Cursor: 6 skills/7 agents, plus hooks, MCP, goals, and orchestration paths. |
| Forbidden folders | Pass | `find` and `git ls-files` scans found no `followup`, `follow_up`, or `website` paths. |
| Secret/path scan | Pass | Strict `rg` scan found no API-key assignments, private-key markers, or absolute local user paths after excluding ignored generated/dependency folders. |
| Core artifact inventory | Pass | `docs/sources.md`, `docs/tool_claims_audit.md`, `docs/verification_report.md`, `docs/research_article_harness.md`, slide demo map, Card-Krueger example, and starter data exist. |
| Stale wording scan | Pass after fixes | Removed obsolete pre-course setup files; remaining LSE/Pavia references are provenance, import-manifest, or explicit parent-workshop links. |
| Local markdown links | Pass | Local markdown link check passed across 211 Markdown files. |

## Readiness Decision

Ready for the 5-hour Padova participant delivery.

Reason: the participant path is discoverable from the top level, schedule,
slides, exercises, guide, examples, and tool-lane manuals align in the same
sequence, the Card-Krueger and starter examples have verification evidence, each
tool lane has a usable economics-research harness, official-doc caveats are
recorded, and stale imported LSE pre-course setup material has been removed.
