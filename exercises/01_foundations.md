# Exercise 01: Foundations

Time: 00:15-00:45

## Output

Run or draft one read-only prompt that teaches the agent the repo map and
boundaries.

## Open

- `GUIDE.md`
- `templates/AGENTS_economics.md`
- `examples/starter_article/AGENTS.md`
- `examples/card-krueger/README.md`

## Prompt

```text
Read README.md, START_HERE.md, SCHEDULE.md, GUIDE.md, and
examples/card-krueger/README.md. Do not edit files. Explain:
1. the workshop path;
2. the Card-Krueger running example;
3. the files I should copy or personalize;
4. the files or folders I should not expose to agents;
5. what evidence I should require before accepting an edit.
```

## Verification

The answer must mention:

- `examples/card-krueger/`;
- `examples/starter_article/`;
- private/raw data boundaries;
- evidence before acceptance;
- human ownership of research claims.
