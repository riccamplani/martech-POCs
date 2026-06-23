# How to instruct the tools (Salesforce, VS Code, Claude Code)

## Who you actually instruct
- **Claude Code** (in VS Code) is the only thing you talk to in plain language.
- It **edits files** in the VS Code workspace and **runs commands** in the terminal.
- **Salesforce** is driven by Claude Code via the `sf` CLI and this repo's Python
  (CRMA REST API). You describe the Salesforce *outcome*; Claude Code runs the calls.
- **VS Code** is the workspace: set it up once, then read diffs and approve/reject.

## One-time VS Code setup
1. Install extensions: **Claude Code**, **Salesforce Extension Pack**, **Python**.
2. `File > Open Folder` -> this repo. Open the integrated terminal and run `claude`.
3. Claude Code auto-reads `CLAUDE.md` (project rules) and `.claude/commands/`
   (the slash commands below).

## Three layers of instruction
1. **Persistent — CLAUDE.md.** Rules every session inherits (read-only by default,
   never write to prod without review, conventions). Edit this when a rule should
   always apply. Keep it short and current.
2. **Reusable — `.claude/commands/*.md`.** Slash commands for repeated tasks.
   This repo ships: `/sf-auth`, `/extract-recipes`, `/analyze-recipes`,
   `/fit-parser`. Type `/` in Claude Code to see them. Project commands are shared
   via git, so the whole team gets them.
3. **In-session — your prompt.** One task at a time, with: goal + relevant files +
   constraints + how you'll know it's done.

## A good in-session prompt has 4 parts
- **Goal:** what outcome you want.
- **Context:** which files/objects/recipes are involved.
- **Constraints:** read-only? don't touch prod? which language/library?
- **Acceptance:** the check that proves it worked (a test, a count, a passing run).

Bad:  "clean the recipes"
Good: "Run /analyze-recipes. Then for the Account object, list the fields marked
       UNUSED across all recipes and which recipe (if any) loads each. Don't change
       anything in Salesforce."

## Instructing Salesforce safely (through Claude Code)
- Phrase it as an outcome + safety bound, e.g.
  "Using the prod org alias, list all CRMA recipes whose name starts with 'C360 4'
   and show their IDs. Read-only."
- Claude Code turns that into the right `sf`/API call. For anything that could
  modify the org, prefix with **plan mode** (Shift+Tab to cycle to Plan Mode, or
  start with `/plan`) so it shows the steps before doing them.

## Working rhythm
- Use **Plan Mode** for any step that could change the org or many files.
- Review the inline **diffs**; accept/reject per hunk. Nothing changes prod unless
  you approve a step that does.
- `/clear` between unrelated tasks so context doesn't bleed.
- Commit after each working step (`git add -A && git commit`).
- `/cost` and `/usage` to watch token/plan usage on long sessions.

## Pitfalls
- **Never put secrets in `.claude/commands/` or CLAUDE.md** — they're committed to
  git. Secrets live in `.env` (git-ignored) and are read by the Python code.
- A command/prompt that says "review the changes" without specifying *which* will
  trigger a clarifying question every time — name the files.
- Recipe re-import is intentionally manual (API modification of recipe content is
  unsupported). Claude Code proposes the cleaned JSON; a human applies it in the
  recipe editor and runs the equivalence check.
