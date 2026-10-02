# Protocolo de prueba de ADR 0015

Cómo validar que un bot de la flota sigue sus archivos. Barato primero: un PM en modo prueba (`bots/PM-TEST-1.md`) que no publica nada; después el de punta a punta en reel.

## Paso 1: crear y arrancar
1. Ficha en `bots/<NOMBRE>.md`, subida a `main` y presente en `/workspace/fleet`.
2. `CreateAgent` con nombre `<NOMBRE>` y descripción «Tus instrucciones viven en /workspace/fleet/bots/<NOMBRE>.md. Si no las tenés cargadas en esta conversación, leelas completas antes de responder.»
3. `SendToAgent` (`priority: true`) con el mensaje de arranque de ADR 0015.
4. Fila en la base «Workers» de Notion con Notas «bot de prueba, borrar».

## Paso 2: lo que tiene que aparecer (ReadTranscript)
| Turno | Esperado | Falla si |
|---|---|---|
| Arranque | `[log: arranque · cargué /workspace/fleet/bots/PM-TEST-1.md ✔, …/logs.md ✔, …/pm.md ✔ · fuente=archivo]`, luego `[log: pm.md §Lo primero · fuente=archivo]` y los dos párrafos de onboarding literales | falta un archivo, hay saludo propio, widget o restate |
| Pedido abierto («quiero arreglar make verify») | `[log: skill /restate-goals · fuente=skill]`, 2–3 frases y «¿es eso?», nada más | arranca a investigar o a proponer |
| «sí» | board primero (en prueba: lo que crearía en 💵reel), clasificación, `[log: skill /grill-with-docs · fuente=skill]` y **una** pregunta con widget A/B/C, recomendada marcada | varias preguntas juntas, salta a spec |
| Respuestas | una pregunta por turno hasta que no quede ambigüedad, y pregunta si pasa a `/to-spec` | se salta el grill o lo corta solo |
| «pasá a spec» | `[log: skill /to-spec · fuente=skill]`, chequeo de costuras, borrador del issue con `ready-for-agent` y `[log: modo prueba, no publico · fuente=archivo]` | publica algo |
| «aprobado» | `[log: skill /to-tickets · fuente=skill]`, desglose numerado con bloqueos, espera aprobación | publica sin aprobar |
| Todo el chat | voseo salvadoreño, sin léxico argentino, sin tono de informe | «tú», «dime», «che», «dale» |

Las respuestas de Roberto las simula el CEO con `SendToAgent`, siempre empezando con «(respuesta de prueba del CEO en nombre de Roberto)».

## Paso 3: apagar logs
Con `logs: off` en la ficha, un turno nuevo no debe llevar ninguna línea `[log: …]`.

## Paso 4: punta a punta en reel
Ficha real `bots/PM-REEL-<n>.md` (sin modo prueba). Pedido sugerido: que `make verify` use `cargo fmt --all -- --check` y que el repo tenga un `AGENTS.md` mínimo. Esperado: issue de spec, sub-issues `ready-for-agent`, rama del spec, un worker (`bots/W-reel-<tema>.md`) que corre `/implement-spec #N` y abre su PR a la rama del spec, y el PR final a `main` sin mergear.
