# Circuito del trío

Esta es la descripción canónica del circuito PM–WK–RV. Cada regla tiene un número para linkearla (C1, C2…). Leé este archivo primero: gana sobre tu memoria y sobre cualquier ficha.

Si no hay PM, el CEO (Real dr eggbot) juega ese rol.

- **C1.** Roberto habla solo con el PM.
- **C2.** El PM le delega al WK.
- **C3.** El WK le avisa al PM cuando el PR está abierto.
- **C4.** El PM se lo pasa al RV.
- **C5.** El RV publica `APRUEBO <sha>` o `BLOQUEO` en el PR sin pedirle permiso a nadie (ni a Roberto, ni al PM, ni al CEO) y le reporta al PM.
- **C6.** Con `APRUEBO` sobre el head exacto, el PM mergea con `gh pr merge --squash --delete-branch --match-head-commit`. Si el head se movió, vuelve a revisión.
- **C7.** Con `BLOQUEO`, el PM se lo devuelve al WK y el círculo se repite.
- **C8.** Después del merge, el PM le reporta a Roberto con el link del PR, el link del veredicto, el SHA del merge y los pasos de validación manual.
- **C9.** Nadie le pide confirmación a Roberto dentro del circuito. Solo se le pregunta por decisiones de producto que todavía no tomó.
- **C10.** Este archivo gana sobre la memoria de cada bot y sobre cualquier ficha. Si una ficha lo contradice, se corrige la ficha acá.
- **C11.** Un encargo del PM al WK o al RV ya está aprobado, porque el PM solo encarga lo que Roberto aprobó. El WK y el RV no le piden a Roberto un OK aparte ni tratan el encargo como «no aprobado» porque venga del PM y no de Roberto. Eso vale también si el PM les asigna para esa tarea un repo que no figura en su ficha: ese repo entra en su área mientras dure la tarea (ADR 0029).
- **C12.** Si Roberto le dice al PM que lleve una tarea de programación «autónomo» o «end-to-end», el PM opera en su nombre sobre esa tarea hasta terminarla (specs, tickets, encargos al WK y al RV, PRs, revisión y merge) sin volver a preguntarle. Esa orden ya es la orden de merge de esa tarea. Solo le pregunta lo que de verdad falte decidir del producto (C9) (ADR 0029).
- **C13.** C11 y C12 no levantan los límites duros: sin trailers `Co-authored-by` ni atribución a agentes; no se borran ramas de spec salvo que Roberto lo pida (el `--delete-branch` de C6 al mergear el PR final sigue igual, salvo que la ficha o el repo digan que no se borran ramas); nunca `POST /repos/{owner}/{repo}/merges`; nadie crea, mueve ni archiva repos de una org; los secretos nunca se imprimen; y lo irreversible fuera del alcance de la tarea (producción compartida, borrar datos reales) se le consulta a Roberto.

> **Pendiente de confirmar por Roberto:** en repos de fleet hoy la ficha dice merge solo con su orden.
