# Repos start from robert-flo/Template

- **Bash projects**: use the full robert-flo/Template ("Use this template", fresh history), then `make repository-bootstrap` and `make verify`.
- **Any other stack** (Android, iOS...): copy only its agent-facing files: `docs/agents/` (issue-tracker.md, triage-labels.md, domain.md), `AGENTS.md`, `COMMIT_MESSAGE_GUIDELINES.md`, `RELEASE_POLICY.md`. Adapt the Bash-specific sections of AGENTS.md to the stack; keep the Agent skills section as-is.
- **Reference**: whenever it helps (CI workflows, lint config, Makefiles, pre-commit, release automation, issue/PR templates), PMs consult robert-flo/Template as the reference implementation before inventing their own.

The agent files already configure the Matt Pocock skills (GitHub issues via gh, default triage labels, single-context GLOSSARY.md + docs/adr), so PMs do not run setup-matt-pocock-skills; they copy or verify these files. PMs follow their conventions, including issue titles prefixed `<number> - <title>` (create, then rename) and GitHub native issue dependencies for blocking edges.
