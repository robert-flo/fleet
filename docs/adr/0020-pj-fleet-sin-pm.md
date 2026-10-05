# 0020 — pj-fleet no tiene PM ni worker: el CEO es su dueño y RV-pj-fleet revisa

Fecha: 2026-10-04 · Estado: aceptado · Excepción a: ADR 0019

## Contexto
`robert-flo/fleet` guarda las reglas de todos los bots, incluidas las del PM. Roberto lo refina a diario conversando con el CEO, en cambios chicos y frecuentes. Si un PM lo editara, se estaría reescribiendo sus propias reglas, y cada ajuste daría tres saltos (Roberto, CEO, PM y worker), lo que gasta cuota de Grok Bot y lo hace más lento. `robert-flo/assets` es la otra pieza de infraestructura de la flota: el depósito público de las capturas de prueba de todos los PRs.

## Decisión
- pj-fleet es un proyecto de varios repos: `robert-flo/fleet` (privado, clon en `/workspace/fleet`) y `robert-flo/assets` (público). Es el único proyecto sin trío: no tiene PM ni WK. El dueño es el CEO, Real dr eggbot (`0d5bf65b-1bcf-4848-8942-c8761c58be3e`).
- Los cambios chicos (una regla, una ficha, un renombre, un dato) se hablan con el CEO y él los sube directo a `main`, como hasta ahora. En assets, los workers y los cloud agents siguen subiendo capturas directo a `main`, solo agregando archivos.
- Los cambios grandes, que afectan a todos los bots (un ADR nuevo, una plantilla de `templates/`, una skill compartida, la estructura de un repo o la convención de rutas de assets), van por PR del CEO. Ese PR lo revisa **RV-pj-fleet** (`58eb97b7-ffce-45dd-b969-8cb46142e942`), y Roberto mergea con «merge».
- En TickTick, pj-fleet tiene su grupo (`6ac302fd8f088b3af7b901fb`) con dos listas: 🇧🇷rf-fleet (`6ac3023e8f088b3af7b8f011`) y 🇧🇷rf-assets (`6ac303048f089f3769520e46`), ambas con las seis columnas estándar. Ahí el CEO anota cada cambio como tarea, para que Roberto y Sura vean el avance. Las capturas que suben los workers no llevan tarea.
- Tampoco hay fila en Notion Workers, porque no hay worker.
