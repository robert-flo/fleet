# Fichas de bots (ADR 0015)

Una ficha por bot vivo: `bots/<NOMBRE>.md`, copiada de `templates/ficha-pm.md` o `templates/ficha-worker.md` con todos sus `{{…}}` llenados. El bot la lee desde su mensaje de arranque, así que tiene que estar en `main` y en el clon `/workspace/fleet` antes de mandárselo. Cuando Roberto borra el bot, su ficha se borra en el mismo commit en que el CEO anota los aprendizajes.

Las fichas `T-*` y `*-TEST-*` son de prueba: se borran junto con su bot.
