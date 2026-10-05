# 0021 — rf-Template es infraestructura: el lenguaje común de todos los repos

Fecha: 2026-10-04 · Estado: aceptado · Complementa: ADR 0019, ADR 0020

## Contexto
Roberto tiene muchos repos, todos distintos. `robert-flo/Template` es su intento de darles a todos un lenguaje común: estructura, convenciones, `AGENTS.md`, `GLOSSARY.md`, etiquetas, quality gate y flujo de PR. Por eso es infraestructura, igual que fleet, assets y skills. Pero, a diferencia de esos tres (docs y reglas que el CEO cambia platicando con Roberto, ADR 0020), Template es código con specs, tickets y PRs, donde el trío PM/WK/RV rinde.

## Decisión
- rf-Template conserva su trío (PM-rf-Template, WK-rf-Template y RV-rf-Template) y su lista 🇧🇷rf-Template, y no entra a pj-fleet.
- Es infraestructura: un cambio al lenguaje común (estructura del repo, convenciones, `AGENTS.md`, `GLOSSARY.md`, `docs/agents/`, etiquetas, quality gate o flujo de PR) necesita un ADR en `docs/adr/` de Template, que va en el mismo spec. El PM lo pide al armar el spec, y RV-rf-Template pone BLOQUEO al PR que cambie el lenguaje común sin su ADR.
- Propagación: cuando se mergea un cambio así, PM-rf-Template se lo avisa al CEO con el ADR y lo que cambia. El CEO decide con Roberto a qué repos se propaga, y se lo pasa a los PMs de esos proyectos como pedido nuevo, que siguen su flujo normal.
- Los cambios que no tocan el lenguaje común (bugs, scripts, docs internas) siguen el flujo de siempre, sin ADR.
