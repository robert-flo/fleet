# 0019 — Equipo fijo por proyecto: PM, worker y reviewer

Fecha: 2026-10-01 · Estado: aceptado · Enmienda: ADR 0016 y ADR 0017

## Contexto
El PM no puede borrar bots; solo Roberto. Crear un worker por spec deja bots sueltos. Desde ADR 0018 los workers programan con cloud agents, así que un solo worker puede correr varios en paralelo (uno por PR). Un bot quieto no gasta cuota: solo gasta cuando responde.

## Decisión
- Cada proyecto tiene tres bots fijos: su PM, un worker y un reviewer (nombres en §Nombres).
- El PM le pasa cada spec nuevo a su worker fijo por SendToAgent en vez de crear otro bot. El paralelismo lo dan los cloud agents.
- Un worker extra (`WK-<proyecto>-<tema>`) se crea con `create-worker` solo si coinciden dos specs grandes; al terminar, el PM hace los pasos de «Al borrar» y le avisa a Roberto que lo puede borrar.
- Un reviewer por proyecto y no uno global: así guarda en su memoria el stack y las reglas de ese repo, sin mezclar contextos (Rust, Android, web, bash).
- Crear un PM es crear el trío: la skill `create-pm` crea `PM-<proyecto>`, `WK-<proyecto>` y `RV-<proyecto>` de una vez, con sus fichas (`templates/ficha-pm.md`, `ficha-worker.md`, `ficha-reviewer.md`), los ids cruzados y la fila del worker en Notion Workers. Roberto solo dice «creá un PM». Un proyecto puede abarcar varios repos: sigue siendo un solo trío, y el worker lanza el cloud agent en el repo que toque.

## Aplicado en reel
- `5c0e963b-d358-4d0e-8b4e-f600eeae0934`: W-reel-verify pasa a **W-reel** (`bots/W-reel.md`).
- `3dc7c611-d4ab-4881-b451-72573ce4eb3b`: reviewer pasa a **reviewer-reel** (`bots/reviewer-reel.md`).

## Nombres (2026-10-01)
- `PM-<proyecto>`, `WK-<proyecto>` y `RV-<proyecto>`; un worker extra es `WK-<proyecto>-<tema>`. Reemplaza `PM-<PROYECTO>-<área>`, `W-<proyecto>` y `reviewer-<proyecto>`.
- `<proyecto>` lo elige Roberto: el CEO se lo pregunta siempre al crear un PM. Si un proyecto tiene dos PMs, el área va dentro del nombre del proyecto (`PM-reel-desktop`).
- En reel: PM-TEST-1 pasa a **PM-reel** (`901aee5c-e15d-43cb-882d-7d03fdc598fc`), W-reel a **WK-reel** (`5c0e963b-…`) y reviewer-reel a **RV-reel** (`3dc7c611-…`).
