# Every repo carries the agent files from robert-flo/Template

The repo template is not the whole Bash scaffold of robert-flo/Template, only its agent-facing files, copied into every repo regardless of stack (Bash, Android, iOS...):

- `docs/agents/` (issue-tracker.md, triage-labels.md, domain.md)
- `AGENTS.md`
- `COMMIT_MESSAGE_GUIDELINES.md`
- `RELEASE_POLICY.md`

They already configure the Matt Pocock skills (GitHub issues via gh, default triage labels, single-context GLOSSARY.md + docs/adr), so PMs do not run setup-matt-pocock-skills; they copy or verify these files. PMs follow their conventions, including issue titles prefixed `<number> - <title>` (create, then rename) and GitHub native issue dependencies for blocking edges. Stack-specific sections of AGENTS.md are adapted per repo; the Agent skills section stays as-is.
