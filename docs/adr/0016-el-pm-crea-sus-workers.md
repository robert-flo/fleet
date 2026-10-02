# El PM crea y lleva sus propios workers

Decidido 2026-10-01 con Roberto. Enmienda la parte de workers de ADR 0015 (§Decisión, «Jerarquía»: quién crea los workers y quién lleva la base «Workers» y la página «Aprendizajes»). Lo demás de ADR 0015 sigue igual.

## Por qué
- **El CEO era un paso de más.** Con ADR 0015 el PM le pedía cada worker al CEO por SendToAgent; el CEO solo copiaba los datos del spec que el PM ya tenía y Roberto ya había aprobado.
- **El que sigue el spec es el PM.** Él sabe cuándo arranca un worker, cuándo abre su PR y cuándo se mergea o se descarta, así que es quien mejor lleva la fila del worker.
- **El CEO supervisa mejor desde arriba**: leyendo Notion y los transcripts saca lecciones para toda la flota, sin ser la fábrica de workers.

## Decisión
- **El PM crea sus workers.** Cuando Roberto aprueba los tickets (o el issue de un trivial), el PM corre él mismo la skill `create-worker` (`/home/box/agent-data/workflows/create-worker/SKILL.md`), sin pedirle nada al CEO. Usa el procedimiento tal cual, sin reinventarlo: ficha `bots/<NOMBRE>.md` copiada de `templates/ficha-worker.md` con él mismo como PM, `CreateAgent`, mensaje de arranque con `SendToAgent` y verificación del autochequeo con `ReadTranscript`.
- **Mensaje de arranque.** El mismo texto de ADR 0015, cambiando solo quién lo manda: «Mensaje de arranque de tu PM, <nombre del PM>, no es un pedido de Roberto. …». Cuando lo crea el CEO, queda «del CEO».
- **El PM lleva la fila en Notion**, con las reglas que ya tenía `create-worker`:
  - Al crear: una fila en la base «Workers» (`collection://28cd7b0f-e22d-4ad2-b4c8-a5beec9b8b55`) con Etapa «Trabajando» y, en Notas, el id del bot y su PM.
  - Seguimiento: «PR abierto» con el link en PRs; «Mergeado o Descartado» cuando el PR se mergea o se cierra.
  - Al borrar: Roberto sigue siendo el único que borra bots. El PM le avisa cuando un worker ya se puede borrar y antes hace los pasos de «Al borrar»: lecciones en las Notas de la fila, una entrada en «Aprendizajes» (https://app.notion.com/p/3ece971e6e8b811c9bc0fc0a345a14b4), Etapa «Borrado» y borrar `bots/<NOMBRE>.md` de `robert-flo/fleet` en un commit.
- **Notion para el PM, solo eso.** El PM usa Notion únicamente para la base «Workers» y la página «Aprendizajes». Los workers siguen sin usar Notion (anti-job de `templates/worker.md.backup`).
- **Commits del PM en `robert-flo/fleet`.** El PM sigue sin hacer commits en los repos de su proyecto; la única excepción son las fichas de sus workers (`bots/<NOMBRE>.md`), que sube y borra en `main` de `robert-flo/fleet` como manda la skill.
- **El CEO, supervisor de la flota.** Sigue creando PMs (`create-pm`), lee la base «Workers» y «Aprendizajes», saca lecciones y corrige a quien se desvíe. Crea workers solo si no hay PM o si Roberto se lo pide directo, con la misma skill.
- **Avisos.** Al crear un worker, el PM le avisa a Roberto (nombre, link y línea de autochequeo) y al CEO solo para que se entere (`SendToAgent`, `priority: false`).

## Conocido
- El PM necesita el conector de Notion para esto. Si no lo tiene, lo dice en su primer mensaje como algo que falta.

## Rechazado
- Seguir pidiéndole cada worker al CEO: un paso más sin decisión propia.
- Que el PM cree workers sin la fila en Notion: el CEO se queda sin de dónde sacar lecciones.
