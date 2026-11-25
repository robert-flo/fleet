# 0028 — HR-KODIGO: GitHub Issues orquesta

Fecha: 2026-11-25 · Estado: aceptado · Extiende: ADR 0027

## Contexto
Roberto crea el proyecto HR-KODIGO sobre el Home Repo privado [robert-flo/HR-KODIGO](https://github.com/robert-flo/HR-KODIGO) (rama por defecto `master`). Ese repo controla las actividades del Grupo 12 (AI For Devs Jr. 5, Kodigo); los entregables viven en la org [kodigo-grupo-12](https://github.com/kodigo-grupo-12). Quiere un trío PM/WK/RV-HR-KODIGO que orqueste el trabajo en GitHub Issues de ese home, sin lista de TickTick y sin Linear, igual que HR-CLAVIS (ADR 0027). El trío local de agy/herdr (`pj-trio`) ya existe en ese repo y convive.

## Decisión
1. Para HR-KODIGO, **GitHub Issues de `robert-flo/HR-KODIGO` orquesta el trabajo** (tablero, specs y sub-issues). No hay lista de TickTick ni Linear. Esto reemplaza ADR 0025 y no usa ADR 0026 para este proyecto.
2. El trío trabaja el Home Repo `robert-flo/HR-KODIGO` (rama `master`) y **todos los repos de la org `kodigo-grupo-12`** (hoy: `monorepo`, `documentacion` y `.github`; rama `main`). Un PR en un repo de la org cuelga de un issue de HR-KODIGO. `robert-flo/pj-template` y `robert-flo/ravn-trio` quedan fuera del alcance de este trío.
3. En el Home Repo mandan sus propias reglas (`AGENTS.md`, `onboarding.yml`): rama por defecto `master` (nunca `main`), sin trailers `Co-authored-by`, nada directo a `master`, y no crear, mover ni archivar repos dentro de la org.
4. El trío de Grok Bot convive con el trío local de agy/herdr (`pj-trio`); no lo reemplaza. El trabajo se sigue orquestando en los Issues del home.
