# 0022 — Los bots de los tríos operan en la PC de Roberto

Fecha: 2026-10-04 · Estado: aceptado · Enmienda: ADR 0017 (el RV opera la máquina) y ADR 0018 (`cursor-agent` en gracie para el trabajo sobre la máquina), además de `templates/pm.md` (el PM opera la máquina)

## Contexto
Roberto quiere que todos los bots de los tríos (PM, WK y RV) puedan trabajar directo en su PC, gracie, que corre Omarchy y ya está registrada en Grok Bot. Ahí tiene `cursor-agent`, que gasta cuota de Cursor, la grande, y no la de Grok Bot, que es chica (ADR 0018). Lo decidió en un grilling con el CEO el 2026-10-04. Ese mismo día decidió también que, para todo lo de Omarchy, se use la skill oficial que trae Omarchy y no su skill `omarchy` vieja, que quedó archivada en Notion.

## Decisión
1. **Dos clases de trabajo.** El código de un repo, lo que termina en un commit, sigue por cloud agent con el flujo normal (ADR 0005, 0018). El trabajo sobre la máquina (instalar, configurar, probar, diagnosticar) se hace en gracie: lo largo con `cursor-agent` y lo corto con comandos directos. En gracie nadie hace commit ni push. GitHub manda; el clon del box es para leer y revisar, y el de `~/Work/tries` para probar.
2. **Quién.** PM, WK y RV tienen los mismos poderes sobre la máquina, sudo y `cursor-agent` incluidos. Para el PM y el RV es la única excepción a «no programás»: nunca escriben código de PR ni hacen commits.
3. **Límites.** En gracie, el trabajo sobre la máquina no necesita permiso de Roberto, y el bot se detiene solo ante un impedimento. Eso no cubre merges, mensajes ni nada fuera de gracie. Hay una lista corta de lo que nunca se toca: llaves y credenciales, discos y arranque, `_boveda`, el demonio de sincronización de `~/Work/tries` y los datos personales.
4. **Bitácora.** Cualquier bot de un trío puede cambiar el sistema. Antes de cada cambio, respalda el archivo que va a editar y anota una línea en `~/Work/tries/CAMBIOS.md` con fecha, bot, comando y cómo deshacerlo. Un cambio sin vuelta atrás no se hace sin preguntar. El `cursor-agent` lanzado sigue las mismas reglas. La memoria común de todos los agentes (Cursor, Antigravity, pi, Grok Bot) se diseña después en su propio grilling, que queda pendiente en TickTick 🇧🇷rf-fleet.
5. **Omarchy.** Para tocar el escritorio o la configuración de Omarchy, el bot lee primero la skill oficial instalada en gracie, `/usr/share/omarchy/default/agents/skills/omarchy/SKILL.md`. La trae el paquete `omarchy-settings-dev` junto con `diagnose-crash` y `omarchy-app`, y las tres ya están enlazadas en `~/.claude/skills` y `~/.agents/skills`. Lo que tenga que quedar en el Omarchy de Roberto va por PR a la rama `personal` del fork.
6. **Despliegue.** Las reglas viven en `templates/tu-pc.md`. Toda ficha de un trío (las plantillas y cada `bots/PM-*`, `WK-*` y `RV-*`) lo carga y lleva una sección «Tu PC». Al mergear, el CEO les avisa a todos los bots.

## Cómo se aplica
- `templates/tu-pc.md` tiene las reglas. Si una regla de la PC cambia, se edita solo ese archivo.
- `templates/worker.md` y `worker.md.backup` no se tocan; la sección va en las fichas.
- pj-fleet no tiene trío (ADR 0020), pero RV-pj-fleet lleva la sección igual.
- Roberto deja gracie en «siempre permitir» en Local execution, para que los comandos no pidan aprobación uno por uno.
