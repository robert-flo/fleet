# 0019 — Equipo fijo por proyecto: PM, worker y reviewer

Fecha: 2026-10-01 · Estado: aceptado · Enmienda: ADR 0016 y ADR 0017

## Contexto
El PM no puede borrar bots; solo Roberto. Crear un worker por spec deja bots sueltos. Desde ADR 0018 los workers programan con cloud agents, así que un solo worker puede correr varios en paralelo (uno por PR). Un bot quieto no gasta cuota: solo gasta cuando responde.

## Decisión
- Cada proyecto tiene tres bots fijos: su PM, un worker `W-<proyecto>` y un reviewer `reviewer-<proyecto>`.
- El PM le pasa cada spec nuevo a su worker fijo por SendToAgent en vez de crear otro bot. El paralelismo lo dan los cloud agents.
- Un worker extra (`W-<proyecto>-<tema>`) se crea con `create-worker` solo si coinciden dos specs grandes; al terminar, el PM hace los pasos de «Al borrar» y le avisa a Roberto que lo puede borrar.
- Un reviewer por proyecto y no uno global: así guarda en su memoria el stack y las reglas de ese repo, sin mezclar contextos (Rust, Android, web, bash).
- Crear un PM es crear el trío: la skill `create-pm` crea el PM, `W-<proyecto>` y `reviewer-<proyecto>` de una vez, con sus fichas (`templates/ficha-pm.md`, `ficha-worker.md`, `ficha-reviewer.md`), los ids cruzados y la fila del worker en Notion Workers. Roberto solo dice «creá un PM». Un proyecto puede abarcar varios repos: sigue siendo un solo trío, y el worker lanza el cloud agent en el repo que toque.

## Aplicado en reel
- `5c0e963b-d358-4d0e-8b4e-f600eeae0934`: W-reel-verify pasa a **W-reel** (`bots/W-reel.md`).
- `3dc7c611-d4ab-4881-b451-72573ce4eb3b`: reviewer pasa a **reviewer-reel** (`bots/reviewer-reel.md`).
