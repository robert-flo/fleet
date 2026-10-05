# fleet

Roberto's Grok Bot fleet: shared glossary, decisions (ADRs) and open blockers. Owned by the CEO (Real dr eggbot).

- `GLOSSARY.md`: canonical terms
- `docs/adr/`: decisions
- `BLOCKERS.md`: pending inputs before creating the first PM
- `templates/`: rules for PMs (`pm.md`) and workers (`worker.md.backup`), the log convention (`logs.md`), the rules for working on Roberto's PC (`tu-pc.md`, ADR 0022) and the Ficha templates (ADR 0015)
- `bots/`: one Ficha per live bot, read by the bot from its Mensaje de arranque
- `.github/workflows/sync-personal-fork.yml`: reusable `workflow_call` that fast-forwards a fork's `upstream` mirror and rebases `personal` (ADR 0024). Callers live in each fork; see `.github/workflows/README.md`.
- Roles: CEO, PM, Worker and reviewer; the reviewer checks only the final PR to `main`. Each project has a fixed team: its PM, `WK-<project>` and `RV-<project>`, next to `PM-<project>` (ADR 0019)

## Dónde viven los clones

El árbol de `/workspace` en la computadora de los bots es el mismo que `~/Work/tries` en gracie: una carpeta `pj-<proyecto>/` por proyecto de varios repos (con un clon `rf-<repo>` o `fo-<repo>` por repo adentro) y una carpeta `rf-<repo>` o `fo-<repo>` suelta por proyecto de un solo repo. Por ejemplo, fleet vive en `/workspace/pj-fleet/rf-fleet` y en `~/Work/tries/pj-fleet/rf-fleet`. `/workspace/fleet` queda como atajo fijo (symlink) porque las descripciones de los bots apuntan ahí. Los atajos viejos `/workspace/{Template,reel,try-clone,x-bookmarks,rf-robert-flo}` son temporales y se borran cuando todas las fichas usen la ruta nueva.
