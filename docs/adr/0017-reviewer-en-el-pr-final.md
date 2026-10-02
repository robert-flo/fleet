# Reviewer en el PR final

Decidido 2026-10-01 con Roberto. El bot `reviewer` (`3dc7c611-d4ab-4881-b451-72573ce4eb3b`) revisa únicamente el PR final de una rama de spec a `main`, antes de que lo revise Roberto. Los workers no pasan por él; sus PRs de sub-issues a la rama del spec siguen igual.

## Por qué
- **Ojos independientes.** El reviewer da una revisión separada antes de que Roberto vea el PR final.
- **El `/code-review` del worker es self-review.** No cuenta como una segunda mirada independiente.
- **Solo el PR final.** Revisar cada PR de worker gastaría cuota sin aportar la misma señal; el punto de mayor valor es el PR que llega a `main`.

## Decisión
- El reviewer recibe de Roberto este prompt: «Review this repository as if you are blocking or approving a production PR.»
- Su veredicto es un comentario del PR que empieza con **BLOQUEO** o **APRUEBO**. Como los bots comparten la cuenta de Roberto, no hace una aprobación formal de GitHub.
- El reviewer no programa, no hace commits, no mergea y no toca TickTick ni Notion.

## Cómo
- Cuando todas las subtareas están mergeadas en la rama del spec, el PM abre el PR final a `main` y después llama al reviewer con `SendToAgent`, `priority: true`, el URL del PR y el issue del spec.
- Si el reviewer responde **BLOQUEO**, el PM devuelve el trabajo al worker o workers; si el bloqueo es de diseño, vuelve a `/grill-with-docs`. Después de los cambios, el PM le pide al reviewer que revise otra vez.
- Si responde **APRUEBO**, el PM mueve la tarea de TickTick a 🌼 QA TO CONFIRM y le dice a Roberto que el PR está listo para su revisión, con el link al veredicto del reviewer. Roberto sigue siendo quien mergea.
