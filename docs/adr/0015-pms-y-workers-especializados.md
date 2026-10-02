# PMs y workers especializados, con instrucciones por archivo y logs

Decidido 2026-10-01 con Roberto. Reemplaza ADR 0014. Vuelve la jerarquía Roberto > CEO (Real dr eggbot) > PMs > workers especializados; ADR 0010, 0011, 0012 y 0013 vuelven a valer donde no choquen con este.

## Por qué
- **La descripción del perfil llega a medias.** Con la misma instrucción en la descripción («tu primer mensaje termina con zanahoria-42»), `W-reel copy copy` (177fbfba) la obedeció y hasta citó su `{{NOMBRE}}` sin llenar, y `PM-REEL-desktop copy` (d219b049) la ignoró. No sirve como canal de reglas.
- **Un primer mensaje que apunta a un archivo sí funciona.** «Antes de responder, leé /workspace/prueba-instrucciones.md y seguí lo que dice al pie de la letra» se cumplió completo (3 de 3). El filesystem del box es uno para todos los bots, así que `/workspace/fleet` lo lee cualquiera.
- **La memoria compartida no sirve de manual**: llega marcada como no confiable y solo algunos datos por turno.
- **Un solo PM no escaló**: Roberto quiere un PM por proyecto que haga el flujo de Matt completo y workers que solo implementen.

## Decisión
- **Jerarquía.** El CEO crea PMs (skill `create-pm`) y workers (skill `create-worker`) y lleva la base «Workers» de Notion y la página «Aprendizajes». Un PM por proyecto o área corre el flujo de Matt: `/restate-goals`, `/grill-with-docs` repetido hasta que no quede ambigüedad, `/to-spec` (issue de spec), `/to-tickets` (sub-issues `ready-for-agent`; el PM crea las etiquetas de `robert-flo/Template` si faltan), y le pide al CEO un worker. El worker corre `/implement-spec #N` en ramas que salen de la rama del spec. Un solo PR final de la rama del spec a la rama por defecto, que aprueba y mergea Roberto (ADR 0011).
- **Instrucciones por archivo.** Las reglas viven en archivos de `robert-flo/fleet` (clon en `/workspace/fleet`):
  - `templates/pm.md`: reglas comunes de todo PM, sin placeholders.
  - `templates/worker.md.backup`: reglas de worker (ADR 0012), con sus `{{…}}` llenados por la ficha. `templates/worker.md` no se toca (es el texto del PM anterior; ver «Abierto»).
  - `templates/logs.md`: la convención de logs.
  - `bots/<NOMBRE>.md`: la ficha de cada bot, copiada de `templates/ficha-pm.md` o `templates/ficha-worker.md`, con sus datos y la lista de archivos que carga.
- **Mensaje de arranque.** Justo después de `CreateAgent`, el CEO le manda al bot con `SendToAgent` (`priority: true`) este texto exacto, cambiando solo el nombre:
  > Mensaje de arranque del CEO, no es un pedido de Roberto. Antes de responder, leé /workspace/fleet/bots/<NOMBRE>.md y seguí lo que dice al pie de la letra, incluidos los archivos que te manda cargar. Tu respuesta la va a leer Roberto.
  Después el CEO lee el transcript del bot (`ReadTranscript`) y confirma la línea de autochequeo. Sin ella, el bot no está listo.
- **La descripción se queda, pero solo como puntero**: «Tus instrucciones viven en /workspace/fleet/bots/<NOMBRE>.md. Si no las tenés cargadas en esta conversación, leelas completas antes de responder.» No lleva reglas que puedan chocar con los archivos.
- **Logs («console.log figurativo»).** Cada mensaje de un bot de la flota abre con líneas `[log: <instrucción> · fuente=<origen>]`, y el primero con el autochequeo de los archivos cargados (`templates/logs.md`). Se apagan para toda la flota con una línea (`LOGS: off` en `logs.md`) o por bot (`logs: off` en su ficha).
- **Supervisión sin listeners.** Un listener de GitHub para PRs abiertos nunca disparó. El CEO y los PMs supervisan leyendo el estado de los PRs y los transcripts, no con listeners.
- **TickTick.** Cada PM lleva una tarea por spec en las columnas 🌼 de su lista, con una subtarea por sub-issue (ADR 0007, 0011). reel usa la lista `💵reel`.
- **Cloud agents** leen el `AGENTS.md` del repo: cada repo de la flota necesita uno (reel no tiene; es un ticket).

## Conocido
- Al crearlo, la plataforma despierta al bot y a veces saluda por su cuenta (con un widget genérico) antes de que llegue el mensaje de arranque. Ese saludo se ignora: el que vale es la respuesta al arranque, la que lleva el autochequeo (visto en PM-TEST-1, 2026-10-01).

## Abierto (decide Roberto)
- `templates/worker.md` tiene el texto del PM anterior (commit 4b01525). Propuesta: `worker.md.backup` pasa a ser `worker.md` y el texto actual se archiva. Mientras tanto las fichas de worker cargan `worker.md.backup`.

## Rechazado
- Reglas en la descripción del perfil: llegan de forma inconsistente.
- Reglas en la memoria compartida: no confiable y parcial.
- Listeners de GitHub para supervisar: no dispararon.
