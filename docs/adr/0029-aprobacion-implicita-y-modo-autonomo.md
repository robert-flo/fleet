# 0029 — Aprobación implícita del trío y modo autónomo del PM

Fecha: 2026-11-25 · Estado: aceptado · Enmienda: ADR 0005, ADR 0010 (Roberto aprueba cada paso) y ADR 0017 (el merge con orden explícita), además de `templates/pm.md`, `ficha-worker.md`, `ficha-reviewer.md` y `tu-pc.md`

## Contexto
El 2026-11-25, en HR-KODIGO, Roberto le dio a su PM una tarea «end-to-end» en un repo de pruebas nuevo (`robert-flo/monorepo-pruebas`). El WK no arrancó: el repo no estaba en su ficha y pidió el OK de Roberto con sus propias palabras, porque que el PM le dijera que Roberto lo había aprobado no le alcanzaba. Roberto tuvo que repetir una aprobación que ya había dado. El arreglo de ese día (commit `cab63cd`) fue una sección a mano en dos fichas, que no llega a los tríos nuevos.

Roberto fijó la regla general, en sus palabras: «WK y RV tienen autorización implícita ya que solo trabajan en tareas aprobadas por mí y por el PM. Si yo le digo al PM que puede proceder autónomo o end-to-end, es porque tiene mi permiso definitivo para operar en mi nombre sobre la tarea de programación que le pedí.»

## Decisión
1. **Encargo del PM = aprobado.** El PM solo encarga lo que Roberto aprobó, así que un encargo del PM al WK o al RV ya está aprobado. El WK y el RV no le piden a Roberto un OK aparte. Si el PM les asigna para esa tarea un repo que no figura en sus fichas, ese repo entra en su área mientras dure la tarea (CIRCUITO C11).
2. **Modo autónomo.** Cuando Roberto le dice al PM «autónomo» o «end-to-end» sobre una tarea de programación, el PM opera en su nombre sobre esa tarea hasta terminarla (specs, tickets, encargos, PRs, revisión y merge) sin volver a preguntar. Esa orden cuenta como la orden de merge de esa tarea. El flujo de Matt se hace completo igual; solo deja de esperar el visto bueno entre pasos (CIRCUITO C12).
3. **Límites duros que siguen.** Sin trailers `Co-authored-by` ni atribución a agentes; no borrar ramas de spec salvo que Roberto lo pida (el `--delete-branch` de C6 al mergear el PR final queda como está, salvo que la ficha o el repo digan otra cosa); nunca `POST /repos/{owner}/{repo}/merges`; no crear, mover ni archivar repos de una org; los secretos nunca se imprimen; y lo irreversible fuera del alcance de la tarea (producción compartida, borrar datos reales) se le consulta a Roberto (CIRCUITO C13).

## Cómo se aplica
- La regla vive en `CIRCUITO.md` (C11–C13), que todas las fichas cargan primero y que gana sobre cualquier ficha, así que los bots vivos la reciben sin tocar sus fichas.
- `templates/pm.md` gana la sección «Aprobación implícita y modo autónomo»; `ficha-worker.md` y `ficha-reviewer.md` la repiten para que todo trío nuevo nazca con ella. `templates/worker.md.backup` no se toca (ADR 0022).
- Las fichas de HR-KODIGO cambian la sección de `cab63cd` por una que solo da los datos del repo de pruebas y los límites propios del proyecto.
- `scripts/check-circuito.sh` falla si una ficha o plantilla vuelve a pedir el OK de Roberto «en sus propias palabras».
