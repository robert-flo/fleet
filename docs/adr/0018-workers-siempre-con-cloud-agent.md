# 0018 — Los workers programan siempre con cloud agents

> Enmendada 2026-10-04 por ADR 0022: el código de los repos sigue por cloud agent, pero el trabajo sobre la máquina en gracie (instalar, configurar, probar) se hace con `cursor-agent` ahí mismo, según `templates/tu-pc.md`.
> Enmendada 2026-10-05 por ADR 0023: la supervisión del worker no hace polling; el encargo al cloud agent pide que se suscriba a su PR y lo lleve hasta el final.

Fecha: 2026-10-01 · Estado: aceptado · Enmienda: ADR 0012 §Cloud agents y ADR 0015 §Workers

## Contexto
W-reel-verify programó el spec 4 en el box, sin cloud agent. Eso gasta la cuota de Grok Bot de Roberto, que es chica (el 2026-10-01 pasó de 31% a 81% de la semanal en un día), mientras que su cuota de Cursor es más grande. Además, sin cloud agent Roberto no ve la tarjeta del agente con el PR.

## Decisión
- Todo worker programa con un cloud agent de Cursor, uno por PR, salvo que Roberto diga lo contrario.
- El worker solo supervisa: arma el encargo, aprueba el plan, revisa el PR y le muestra a Roberto la tarjeta del cloud agent.
- En el box no se programa ni se corren builds largos. Los bots gastan lo mínimo de Grok Bot.

## Cómo se aplica
`templates/ficha-worker.md` §Ajustes lo lleva, así que toda ficha nueva lo hereda. `templates/worker.md` y `worker.md.backup` no se tocan.
