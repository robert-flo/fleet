# fleet

Roberto's Grok Bot fleet: shared glossary, decisions (ADRs) and open blockers. Owned by the CEO (Real dr eggbot).

- `GLOSSARY.md`: canonical terms
- `docs/adr/`: decisions
- `BLOCKERS.md`: pending inputs before creating the first PM
- `templates/`: rules for PMs (`pm.md`) and workers (`worker.md.backup`), the log convention (`logs.md`) and the Ficha templates (ADR 0015)
- `bots/`: one Ficha per live bot, read by the bot from its Mensaje de arranque
- Roles: CEO, PM, Worker and reviewer; the reviewer checks only the final PR to `main`
