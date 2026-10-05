# 0022 — Los tríos operan en la PC de Roberto

Fecha: 2026-10-04 · Estado: propuesto · Enmienda: ADR 0018 (agrega `cursor-agent` en la PC como segunda vía, sin quitar los cloud agents)

## Contexto
Roberto quiere que todos los bots de los tríos (PM, WK y RV) puedan trabajar directo en su PC, gracie, como lo hacía omarchy-dev. Gracie corre Omarchy y ya está registrada en Grok Bot. Ahí tiene `cursor-agent`, que gasta cuota de Cursor, que es la grande, y no la de Grok Bot, que es chica (ADR 0018). Lo decidió en un grilling con el CEO el 2026-10-04. Ese mismo día decidió también que, para todo lo de Omarchy, se use la skill oficial que trae Omarchy y no su skill `omarchy` vieja, que quedó archivada en Notion.

## Decisión
1. **Cómo.** En la PC el bot lanza `cursor-agent` en la carpeta del repo, `~/Work/tries/<carpeta>`, y usa comandos directos solo para chequear y verificar. El código de los PRs sigue yendo por cloud agents, uno por PR (ADR 0018).
2. **Quién.** PM, WK y RV tienen los mismos poderes completos en la PC, sudo y `cursor-agent` incluidos.
3. **Límites.** Nada necesita permiso de Roberto. El bot solo se detiene ante un bloqueo insalvable.
4. **Cambios al sistema.** Cualquier trío puede tocar el sistema. Antes de cada cambio lo anota en una bitácora compartida.
5. **Bitácora.** Es el archivo `~/Work/tries/_boveda/sistema/CAMBIOS.md`, en Markdown y compatible con Obsidian, con una línea por cambio que lleva fecha, bot, comando y cómo deshacerlo. La memoria común de todos los agentes (Cursor, Antigravity, pi, Grok Bot) se diseña después en su propio grilling, que queda como pendiente en TickTick 🇧🇷rf-fleet.
6. **Omarchy.** Para tocar el escritorio o la configuración de Omarchy, el bot lee primero la skill oficial instalada en gracie, `/usr/share/omarchy/default/agents/skills/omarchy/SKILL.md`. La trae el paquete `omarchy-settings-dev` junto con `diagnose-crash` y `omarchy-app`, y las tres ya están enlazadas en `~/.claude/skills` y `~/.agents/skills`.
7. **Despliegue.** Las reglas viven en `templates/tu-pc.md`. Toda ficha (las plantillas `ficha-pm.md`, `ficha-worker.md` y `ficha-reviewer.md`, y cada `bots/*.md` de un trío) lleva una sección «Tu PC» que la manda a leer. Al mergear este PR, el CEO avisa a cada bot.

## Cómo se aplica
- `templates/tu-pc.md` tiene las reglas. Si una regla de la PC cambia, se edita solo ese archivo.
- `templates/worker.md` y `worker.md.backup` no se tocan. La sección va en las fichas.
- pj-fleet no tiene trío (ADR 0020). RV-pj-fleet lleva la sección igual, porque es un bot de trío para estos efectos.
- Roberto deja gracie en «siempre permitir» en Local execution, para que los comandos no pidan aprobación uno por uno.
