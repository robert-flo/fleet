---
name: trio-bajo-demanda
description: >-
  Use this when Roberto asks to create, delete, or back up a Grok Bot fleet
  trio (PM-/WK-/RV-<proyecto>) on demand from robert-flo/fleet/respaldo, or
  says «crea el trío de …», «eliminá el trío de …» or «respaldá los tríos».
  Recreates a trio idempotently from the saved backup; never invents fields.
---

# Tríos bajo demanda

Los tríos de la flota no tienen que vivir prendidos. El respaldo canónico está en `robert-flo/fleet/respaldo/<proyecto>/`. Las fichas siguen en `bots/<BOT>.md` y no se duplican. No hay issues ni estado: eso envejece. No toques Notion ni TickTick. Nunca inventes un nombre, un título, una descripción, una foto o una rutina que no estén en el respaldo o en la ficha. Si falta un archivo, parás y lo decís.

Antes de actuar: `git -C /workspace/fleet pull --ff-only` (o `pull --rebase --autostash` si hace falta) y leé `respaldo/<proyecto>/README.md`. El export se regenera con `scripts/respaldar-trios.py` (idempotente: misma entrada → mismos archivos).

## Creá el trío de `<proyecto>`

Idempotente: corrélo dos veces y el segundo paso no crea nada de nuevo.

1. Confirmá que existe `respaldo/<proyecto>/README.md`. Si no existe, parás: no hay respaldo de ese proyecto, no lo inventés.
2. Para cada bot listado (PM, WK, RV; si el README dice que falta un rol, no lo creés):
   - Leé `<BOT>.json`. Tienen que estar `name`, `title`, `description` e `id` (el id es solo referencia; el agente nuevo va a tener otro).
   - Confirmá que existe `bots/<BOT>.md`. Si falta la ficha, parás y lo decís.
   - En la lista de teammates (agentes vivos del usuario), buscá uno con ese `name` exacto.
   - Si ya existe, lo dejás como está: no lo recreés, no le cambies la descripción ni la foto.
   - Si no existe, `CreateAgent` con el `name`, el `title` y la `description` tal cual están en el JSON. La descripción ya apunta a `bots/<BOT>.md`; no la reescribas. Anotá el id nuevo. Ignorá el saludo automático al nacer (ADR 0015).
   - Si hay foto (`<BOT>.png` u otra extensión en el README, no «sin foto») y acabás de crear el bot, cargásela con `UpdateAgent` / `UpdateAvatar` (o la herramienta equivalente) desde ese archivo. Si no hay foto, no inventés una.
   - Si existe `<BOT>.rutinas.json` y acabás de crear el bot, recreá esas rutinas. Si no hay archivo, no inventés rutinas.
3. Si actualizaste ids en las fichas (un bot nuevo tiene id distinto al que figura en «Worker fijo», «Reviewer» o el PM), abrí un PR a `main` de fleet con esos ids. No lo mergeés: los PR de fleet solo se mergean con orden explícita de Roberto. El Mensaje de arranque espera a que esas fichas estén en `main` y en `/workspace/fleet`.
4. Mensaje de arranque, solo a los bots que acabás de crear (a los que ya existían no les vuelvas a mandar el arranque), con `SendToAgent` y `priority: true`, en este orden: PM, WK, RV. El texto es el de `create-pm` / `create-worker`, exacto, solo cambia `<NOMBRE>`:
   > Mensaje de arranque del CEO, no es un pedido de Roberto. Antes de responder, leé /workspace/fleet/bots/<NOMBRE>.md y seguí lo que dice al pie de la letra, incluidos los archivos que te manda cargar. Tu respuesta la va a leer Roberto.
5. Verificá con `ReadTranscript` el autochequeo de `logs.md`, como dicen `create-pm` y `create-worker`: todos abren con `[log: arranque · cargué … ✔ … · fuente=archivo]`; el PM sigue con `[log: pm.md §Lo primero · fuente=archivo]` y su primer mensaje. Si falta algo, una sola vez: «Releé /workspace/fleet/bots/<NOMBRE>.md completo y rehacé tu primera respuesta.» Si sigue mal, avisale a Roberto con la cita; no lo des por listo.
6. Reportá los ids (los nuevos y los que ya estaban), los links `grokbot://app/v1/agent?id=<id>` y el resultado del self-check. Si el trío estaba incompleto en el respaldo, decilo.

## Eliminá el trío de `<proyecto>`

No borres vos los agentes. No hagas auditoría de trabajo pendiente.

1. Refrescá el respaldo de ese trío: `python3 /workspace/fleet/scripts/respaldar-trios.py --proyecto <proyecto>`.
2. Si hay cambios, commitealos en una rama auxiliar (`ceo/respaldo-trios` o `ceo/respaldo-<proyecto>`) y abrí un PR a `main`. Identidad: `Roberto Flores <25asab015@ujmd.edu.sv>`. Sin trailers ni `Co-authored-by`. No mergeés.
3. Pasale a Roberto los nombres exactos de los agentes vivos de ese trío (normalmente los tres: `PM-<proyecto>`, `WK-<proyecto>`, `RV-<proyecto>`) para que los borre él en la app. No toques las fichas, los repos, Notion ni TickTick.

## Respaldá los tríos

1. `python3 /workspace/fleet/scripts/respaldar-trios.py`
2. El script borra `respaldo/` y lo vuelve a escribir desde los agentes vivos. Misma entrada → mismos archivos (claves JSON ordenadas, sin marcas de tiempo). Corrélo dos veces y no tiene que haber diff.
3. Si hay cambios, PR a `main` como arriba, sin mergear.

El destino por defecto es `/workspace/fleet/respaldo`. Úsalo también con `--agents-dir` y `--out-dir` si estás probando.
