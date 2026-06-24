# CLAUDE.md For Economics Research

Read the project README, task or issue, and any relevant data source map before
editing. Prefer small, reviewable changes and explicit verification evidence.

## Research Boundaries

- Do not invent citations, data sources, coefficients, or robustness results.
- Keep causal language tied to the stated identification assumptions.
- Treat `data/raw/`, `data/private/`, private drafts, and credentials as
  protected. Do not inspect, print, or edit them without explicit approval.
- Use relative paths and document the command that reproduces each output.
- For synthetic teaching data, state that no substantive research claim follows.

## Card-Krueger Running Case

The workshop running case is `examples/card-krueger/`. The bundled CSV is
synthetic teaching data inspired by Card and Krueger (1994). It illustrates data
documentation, DiD mechanics, tests, subagent review, checkpoints, hooks, and MCP
configuration. It is not the Card-Krueger raw data and it does not reproduce the
published estimates.

## Review Standard

Before claiming completion, report:

- files changed;
- verification command and result, or why it was not run;
- whether data, assumptions, and caveats stayed consistent;
- residual risks or needed human checks.

For paper or code review, lead with decision-relevant issues. Separate blockers
from optional improvements and cite exact files, lines, tables, or equations when
available.
