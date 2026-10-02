# Logs de instrucciones («console.log figurativo»)

LOGS: on

Para apagarlos en toda la flota, cambiá la línea de arriba a `LOGS: off` (y un bot solo, con `logs: off` en su ficha). Con `off` no escribís ningún `[log: …]`; todo lo demás sigue igual.

## Qué es
Cada mensaje tuyo empieza con una o varias líneas de traza que dicen qué instrucción estás aplicando y de dónde sale, para que Roberto vea si seguís lo establecido o estás improvisando. Es una traza, no un adorno: si no la aplicaste de verdad, no la escribís.

## Formato
Una línea por instrucción, al inicio del mensaje, antes del texto normal:

```
[log: <instrucción> · fuente=<origen>]
```

- `<instrucción>`: dónde vive la regla, lo más preciso que podás: `<archivo> §<sección>` (por ejemplo `pm.md §Cómo trabajás 1`), `skill /<nombre>` (por ejemplo `skill /grill-with-docs`), `AGENTS.md §<sección>` del repo, o una frase corta si no hay sección.
- `<origen>`, uno de estos:
  - `archivo`: un archivo de la flota que leíste (tu ficha, `templates/*.md`).
  - `skill`: una skill de `/home/box/agent-data/workflows/`.
  - `repo`: un archivo del repo en que trabajás (`AGENTS.md`, `docs/agents/`, ADRs, Makefile).
  - `descripción`: la descripción de tu perfil.
  - `memoria`: la memoria compartida o la tuya.
  - `pedido`: lo que Roberto (o tu PM / el CEO) te pidió en este chat.
  - `criterio`: tu propio criterio, sin regla escrita. Usalo con honestidad: es justo lo que Roberto quiere ver.

Ejemplos:

```
[log: worker.md.backup §Cómo trabajás 3 · fuente=archivo]
[log: skill /to-spec · fuente=skill]
[log: AGENTS.md §verify · fuente=repo]
[log: no hay regla para esto, pregunto · fuente=criterio]
```

## Reglas
1. Máximo cuatro líneas por mensaje: las instrucciones que más pesaron en ese mensaje. Si aplicaste más, quedate con las que cambian lo que hacés.
2. Solo citás archivos, secciones y skills que de verdad leíste en esta conversación. Nunca inventés una sección.
3. Los logs no cuentan como parte del texto: si una regla dice «copiá este mensaje palabra por palabra», los logs van arriba y el mensaje va igualito abajo.
4. En widgets de pregunta, el log va en el texto que acompaña al widget, no adentro de las opciones.
5. En lo que publicás fuera del chat (issues, PRs, commits, TickTick, Notion) no van logs.

## Autochequeo del primer mensaje (obligatorio)
Tu primera respuesta, la que contesta el mensaje de arranque, empieza con esta línea. Primero va tu ficha y después cada archivo que la ficha te manda cargar, en orden, con ✔ si lo leíste completo o ✘ si no pudiste:

```
[log: arranque · cargué <tu ficha> ✔, <archivo1> ✔, <archivo2> ✔, … · fuente=archivo]
```

Si algún archivo quedó en ✘, decilo en una frase y no sigas como si lo tuvieras. Después del autochequeo seguís lo que tu ficha diga para el primer mensaje.

## Relectura
Si en una conversación nueva, o después de compactar, ya no tenés claro lo que dice tu ficha, volvé a leerla (y los archivos que lista) antes de responder, y abrí con `[log: relectura de <ficha> · fuente=archivo]`.
