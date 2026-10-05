# 0020 — fleet no tiene PM ni worker: el CEO es su dueño y RV-rf-fleet revisa

Fecha: 2026-10-04 · Estado: aceptado · Excepción a: ADR 0019

## Contexto
`robert-flo/fleet` guarda las reglas de todos los bots, incluidas las del PM. Roberto lo refina a diario conversando con el CEO, en cambios chicos y frecuentes. Si un PM-rf-fleet lo editara, se estaría reescribiendo sus propias reglas, y cada ajuste daría tres saltos (Roberto, CEO, PM y worker), lo que gasta cuota de Grok Bot y lo hace más lento.

## Decisión
- rf-fleet es el único proyecto sin trío: no tiene PM ni WK. El dueño es el CEO, Real dr eggbot (`0d5bf65b-1bcf-4848-8942-c8761c58be3e`).
- Los cambios chicos (una regla, una ficha, un renombre, un dato) se hablan con el CEO y él los sube directo a `main`, como hasta ahora.
- Los cambios grandes, que afectan a todos los bots (un ADR nuevo, una plantilla de `templates/`, una skill compartida o la estructura del repo), van por PR del CEO. Ese PR lo revisa **RV-rf-fleet**, y Roberto mergea con «merge».
- Hay una lista de TickTick, 🇧🇷rf-fleet (id `6ac3023e8f088b3af7b8f011`), con las seis columnas estándar. Ahí el CEO anota cada cambio como tarea, para que Roberto y Sura vean el avance.
- Tampoco hay fila en Notion Workers, porque no hay worker.
