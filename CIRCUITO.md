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

> **Pendiente de confirmar por Roberto:** en repos de fleet hoy la ficha dice merge solo con su orden.
