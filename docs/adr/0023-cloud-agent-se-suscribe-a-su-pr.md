# 0023 — El cloud agent se suscribe a su PR y el WK no hace polling

Fecha: 2026-10-04 · Estado: aceptado · Enmienda: ADR 0018 (supervisión del worker)

## Contexto
Los workers lanzan un cloud agent por PR (ADR 0018) y después se despiertan a menudo a leer transcripts o a chequear CI. Eso gasta cuota de Grok Bot, que es chica, mientras que Cursor ya documenta que un cloud agent **se suscribe solo a los PRs que crea** y los lleva hasta el final (arregla CI y responde comentarios de bots). Un prompt de lanzamiento que pide suscripción explícita refuerza eso en planes sin Teams, donde el auto-fix de CI no corre solo. La decisión sale de la investigación de Roberto del 2026-10-04 sobre Grok Bot + Cursor Cloud Agents.

## Decisión
1. **Cada lanzamiento pide suscripción.** El encargo del WK al cloud agent incluye, en texto claro: abrir el PR listo para review (no draft); suscribirse a ese PR y a su CI; mantener CI verde y atender comentarios de Bugbot o de review hasta que queden limpios; y dejar un comentario final de estado cuando esté listo.
2. **Sin polling frecuente del WK.** El worker no arma routines de cron cada N minutos para leer transcripts. Después del lanzamiento, espera el aviso del cloud agent (o un evento puntual del PR) y un barrido diario de respaldo si hace falta. Los follow-ups (rebase, CI, Bugbot, re-proof) van al **mismo** agente del PR; se lanza uno nuevo solo para un ticket nuevo o una reescritura.
3. **Cuota.** El trabajo de mantener el PR lo paga Cursor. Grok Bot solo se usa para armar el encargo, mostrar la tarjeta y reportar al PM.

## Cómo se aplica
- `templates/ficha-worker.md` §Ajustes lleva la regla, así que toda ficha nueva la hereda.
- Las fichas `bots/WK-*` existentes se actualizan en el mismo cambio.
- `templates/worker.md` y `worker.md.backup` no se tocan.
