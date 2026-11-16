# 0027 — HR-CLAVIS: GitHub Issues orquesta

Fecha: 2026-11-16 · Estado: aceptado

## Contexto
Roberto crea el proyecto HR-CLAVIS sobre el Home Repo [robert-flo/HR-CLAVIS](https://github.com/robert-flo/HR-CLAVIS) (renombrado desde PJ-CLAVIS; rama por defecto `master`). Ese repo agrupa el ecosistema PJ-CLAVIS (workstation, dotfiles, forkhub, workflows). Quiere un trío PM/WK/RV-HR-CLAVIS que orqueste el trabajo en GitHub Issues de ese repo, sin lista de TickTick y sin Linear. El trío PM/WK/RV-workstation se queda como está y convive: workstation sigue con su hub `PJ-NIRI-rf-omarchy-workstation` y su tablero TickTick (ADR 0026).

## Decisión
1. Para HR-CLAVIS, **GitHub Issues de `robert-flo/HR-CLAVIS` orquesta el trabajo** (tablero, specs y sub-issues). No hay lista de TickTick ni Linear. Esto reemplaza ADR 0025 y no usa ADR 0026 para este proyecto.
2. El trío PM/WK/RV-workstation permanece y convive: workstation trabaja el hub; HR-CLAVIS trabaja el Home Repo.
3. En el Home Repo mandan sus propias reglas (`AGENTS.md`): rama por defecto `master` (nunca `main`), sin trailers `Co-authored-by`, nunca PRs hacia StatIndet, y la única puerta a `/` es `pacman`.
