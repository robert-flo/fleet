# 0020 — pj-fleet no tiene PM ni worker: el CEO es su dueño y RV-pj-fleet revisa

> Enmendada 2026-10-05: `robert-flo/fleet` es público, para que callers públicos puedan reusar `.github/workflows/sync-personal-fork.yml`.

> Enmendada 2026-10-05 por ADR 0024: en un fork migrado (`personal` protegida, default de GitHub), el CEO no sube cambios chicos directo a `main`. Van por PR a `personal`. El split chico/grande (quién llama a RV-pj-fleet) no cambia. fleet, assets y robert-flo siguen con push chico a `main`; assets sigue agregando capturas directo a `main`.

> Enmendada 2026-10-05: `robert-flo/sura` entra a pj-fleet igual que `robert-flo/robert-flo` (dueño Real dr eggbot, sin trío, cambios chicos directo a `main`). Es privado: guarda el prompt canónico y el estado del ciclo de Sura. Sura en Grok Bot lee y escribe ese estado ahí.

> Enmendada 2026-10-05: `robert-flo/ceo` entra a pj-fleet igual que `robert-flo/sura` (dueño Real dr eggbot, sin trío, cambios chicos directo a `main`). Es privado: guarda el prompt canónico y el estado operativo del CEO para coexistir Grok Bot ↔ Cursor/Antigravity.

Fecha: 2026-10-04 · Estado: aceptado · Excepción a: ADR 0019

## Contexto
`robert-flo/fleet` guarda las reglas de todos los bots, incluidas las del PM. Roberto lo refina a diario conversando con el CEO, en cambios chicos y frecuentes. Si un PM lo editara, se estaría reescribiendo sus propias reglas, y cada ajuste daría tres saltos (Roberto, CEO, PM y worker), lo que gasta cuota de Grok Bot y lo hace más lento. `robert-flo/assets` es otra pieza de infraestructura de la flota: el depósito público de las capturas de prueba de todos los PRs. La tercera es `robert-flo/skills`, el fork de `mattpocock/skills` con las skills que usan todos los bots.

## Decisión
- pj-fleet es un proyecto de varios repos: `robert-flo/fleet` (público, clon en `/workspace/fleet`), `robert-flo/assets` (público) `robert-flo/skills` (público, fork de `mattpocock/skills`, carpeta `fo-skills`), `robert-flo/robert-flo` (público, el README de perfil de GitHub, clon en `/workspace/pj-fleet/rf-robert-flo`; agregado el 2026-10-04) `robert-flo/sura` (privado, prompt canónico y estado del ciclo de Sura, clon en `/workspace/pj-fleet/rf-sura`; agregado el 2026-10-05) y `robert-flo/ceo` (privado, prompt canónico y estado operativo del CEO, clon en `/workspace/pj-fleet/rf-ceo`; agregado el 2026-10-05). Las skills del fork se instalan en `/home/box/agent-data/workflows`. Es el único proyecto sin trío: no tiene PM ni WK. El dueño es el CEO, Real dr eggbot (`0d5bf65b-1bcf-4848-8942-c8761c58be3e`).
- Los cambios chicos (una regla, una ficha, un renombre, un dato) se hablan con el CEO. En repos que no son un fork migrado (fleet, assets, robert-flo, sura, ceo) él los sube directo a `main`, como hasta ahora. En assets, los workers y los cloud agents siguen subiendo capturas directo a `main`, solo agregando archivos. En un fork ya migrado (piloto `robert-flo/skills`, ADR 0024) esos cambios chicos van por PR a `personal`; no hay push directo a `main` ni a `personal`, y el RV no los revisa.
- Los cambios grandes, que afectan a todos los bots (un ADR nuevo, una plantilla de `templates/`, una skill compartida, la estructura de un repo la convención de rutas de assets, una skill nueva o reescrita o una sincronización del fork con Matt), van por PR del CEO a la rama por defecto de ese repo (`main` o, en un fork migrado, `personal`). Ese PR lo revisa **RV-pj-fleet** (`58eb97b7-ffce-45dd-b969-8cb46142e942`), y Roberto mergea con «merge».
- En TickTick, pj-fleet tiene su grupo (`6ac302fd8f088b3af7b901fb`) con seis listas: 🇧🇷rf-fleet (`6ac3023e8f088b3af7b8f011`), 🇧🇷rf-assets (`6ac303048f089f3769520e46`), 🇧🇷fo-skills (`6ac304298f088b3af7b91ad9`), 🇧🇷rf-robert-flo (`6ac3096b8f089f376952c45e`), 🇧🇷rf-sura (`6ac41ea28f08929498012a7c`) y 🇧🇷rf-ceo (`6ac434e98f088b3af7e55a66`), las seis con las seis columnas estándar. Ahí el CEO anota cada cambio como tarea, para que Roberto y Sura vean el avance. Las capturas que suben los workers no llevan tarea.
- Tampoco hay fila en Notion Workers, porque no hay worker.
