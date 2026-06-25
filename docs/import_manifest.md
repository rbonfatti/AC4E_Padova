# Import Manifest

This repository was initialized from the LSE PhD short-course materials as the
base for the Padova 5-hour participant workshop.

## Source

- Source repository: `meleantonio/AC4E_LSE_PhD_Students`
- Source branch: `main`
- Source commit: `6cf822a47b7cc5545b483b3f0663ae6418805aaa`
- Import method: copied tracked files from the local source checkout with Git
  pathspec exclusions.

## Included Top-Level Paths

The import included the following tracked top-level paths from the source
repository:

| Path | Tracked file count |
| --- | ---: |
| `.cursor/` | 1 |
| `.gitignore` | 1 |
| `AGENTS.md` | 1 |
| `INSTRUCTOR_RUNBOOK.md` | 1 |
| `README.md` | 1 |
| `SETUP.md` | 1 |
| `SYLLABUS.md` | 1 |
| `cursor_chat_recording.md` | 1 |
| `docs/` | 3 |
| `examples/` | 87 |
| `materials/` | 6 |
| `package.json` | 1 |
| `requirements.txt` | 1 |
| `scripts/` | 3 |
| `slides/` | 12 |
| `templates/` | 11 |

## Excluded Paths

The user explicitly requested that follow-up and website material not be copied.
The LSE source repository uses `followup/`, so the import excluded both common
spellings:

- `followup/`
- `follow_up/`
- `website/`

## Notes

- Only files tracked by the LSE Git repository were copied.
- Untracked local files in the LSE checkout were not copied.
- `SETUP_pre_course.md`, `SETUP_pre_course.pdf`, and
  `pandoc_pre_course_preamble.tex` were removed during the final Padova
  readiness review because `SETUP.md` is the maintained participant setup guide
  and the pre-course files retained LSE/4-hour wording.
- The Padova adaptation, Card-Krueger examples, updated guide, documentation
  audit, verification report, and final readiness review were handled in the
  issue/PR sequence after import.
