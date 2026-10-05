# 0024 — En cada fork: rama larga `personal` y espejo `upstream`

Fecha: 2026-10-05 · Estado: aceptado · Enmienda: ADR 0011 (default en forks), ADR 0017 (PR final a la rama por defecto), ADR 0020 (forks migrados: PR a `personal`, no push a `main`)

## Contexto
Roberto cerró un grill-with-docs el 2026-10-05. Hoy Omarchy ya vive en dos líneas: cambios propios en `personal` y un espejo de omacom en `quattro`. Otros forks (skills, y los que vengan) no tienen ese mismo lenguaje: a veces el default es `main`, a veces el remoto se llama `upstream` y se confunde con la rama espejo. Hace falta un modelo único para todos los forks personales, sin inventar un proceso paralelo al de Template y la flota.

Este ADR es la política. La implementación (migrar ramas, workflows, issues de sync) va en issues de seguimiento.

## Decisión
1. **Rama larga de cambios propios.** En cada fork, los cambios personales de Roberto viven en una rama larga llamada **`personal`**.
2. **Espejo de la línea tracked.** El espejo de la línea que se sigue del proyecto de origen es una rama llamada **`upstream`**. Es nombre de rama, no solo el remoto git. Omarchy hoy usa `quattro` como ese espejo; **migra** `quattro` → `upstream`. El fetch sigue viniendo de la rama real de omacom (`quattro`); solo se renombra nuestro espejo. Los workflows de omarchy-pkgs que tienen `quattro` hardcodeado se actualizan en un issue de seguimiento, no como parte de este ADR.
3. **Default de GitHub.** La rama por defecto de cada fork personal es **`personal`**.
4. **`personal` está protegida.** Los commits del día a día entran solo por PRs, al estilo Template. No hay push directo para el trabajo cotidiano. En un fork ya migrado eso incluye los cambios chicos del CEO: van por PR a `personal`, no push directo a `main` ni a `personal` (enmienda ADR 0020).
5. **Quién revisa PRs a `personal`.** En un fork con trío, el **RV de ese trío**, el mismo flujo Template/flota ya acordado. En forks de pj-fleet (hoy `robert-flo/skills`), **RV-pj-fleet**, porque ese proyecto no tiene trío (ADR 0020). El split chico/grande de ADR 0020 no cambia: un cambio chico en un fork de pj-fleet va por PR a `personal` pero no llama al RV; un cambio grande sí. No hay rutinas nuevas ni un proceso paralelo. Más adelante se replica a Antigravity y Cursor; un solo flujo de Development basado en Template + flota.
6. **Misma forma de sync fuera de Omarchy.** Los forks que no son Omarchy usan la misma figura: fast-forward del espejo → rebase de `personal` → force-with-lease, o issue de conflicto. **Sin** la fase de paquetes/build (esa es solo de Omarchy).
7. **Automatización.** El workflow reutilizable de GitHub Actions vive en **`robert-flo/fleet`**. Cada fork tiene un caller delgado. La cadencia es la de Omarchy: **cron diario a las 04:00** (America/El_Salvador / UTC-6).
8. **Conflicto de rebase.** Se abre o actualiza un issue de GitHub (patrón Omarchy `[Conflicto Rebase]`). El trío **no sincroniza por su cuenta**; solo actúa cuando Roberto lo pide.
9. **Orden de rollout.** Primero el piloto **`robert-flo/skills` (fo-skills)**; después el rename/migrate de Omarchy.
10. **Plan de migración de skills.** Crear `personal` desde el `main` actual; poner el default en `personal`; proteger `personal`; introducir `upstream` como espejo FF de `mattpocock/skills` (o del upstream real de ese fork). Seguir documentando que la fase de paquetes es solo Omarchy.

## Cómo se aplica
- Este ADR es la política. Los issues de implementación vienen después: piloto de skills, luego Omarchy (`quattro` → `upstream`), y el workflow reutilizable en fleet más los callers en cada fork.
- En un fork, el PR final de un spec (ADR 0011) y la revisión del RV (ADR 0017) apuntan a la rama por defecto del repo: `personal`, no `main`.
- pj-fleet sigue ADR 0020, enmendado: fleet, assets y robert-flo siguen con cambios chicos directo a `main`; un fork migrado (piloto skills) usa PRs a `personal`. Un cambio grande como este ADR lo revisa RV-pj-fleet. Este PR no migra ramas ni agrega YAML de sync.
