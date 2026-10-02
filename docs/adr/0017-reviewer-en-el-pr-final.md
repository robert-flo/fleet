# Reviewer en el PR final

> Enmendada 2026-10-01 con Roberto: si el PR final tiene `ready-for-human` y Roberto ordena explícitamente «merge» (o un equivalente claro) en el chat del PM, el PM lo mergea con squash, confirma el merge en GitHub, mueve la tarea a 🌼 DONE, borra la rama del spec y le dice a Roberto el SHA. Sin esa orden explícita, no mergea.

Decidido 2026-10-01 con Roberto. El bot `reviewer` (`3dc7c611-d4ab-4881-b451-72573ce4eb3b`) revisa únicamente el PR final de una rama de spec a `main`, antes de que lo revise Roberto. Los workers no pasan por él; sus PRs de sub-issues a la rama del spec siguen igual.

## Por qué
- **Ojos independientes.** El reviewer da una revisión separada antes de que Roberto vea el PR final.
- **El `/code-review` del worker es self-review.** No cuenta como una segunda mirada independiente.
- **Solo el PR final.** Revisar cada PR de worker gastaría cuota sin aportar la misma señal; el punto de mayor valor es el PR que llega a `main`.

## Decisión
- El reviewer recibe de Roberto este prompt: «Review this repository as if you are blocking or approving a production PR.»
- Su veredicto es un comentario del PR que empieza con **BLOQUEO** o **APRUEBO**. Como los bots comparten la cuenta de Roberto, no hace una aprobación formal de GitHub.
- El reviewer no programa, no hace commits, no mergea y no toca TickTick ni Notion.
- Cuando el PM abre el PR final, mueve de inmediato la tarea a 🌼 QA TO CONFIRM: es el territorio del reviewer y el último paso antes de 🌼 DONE.
- Si el reviewer da **BLOQUEO**, la tarea vuelve a 🌼 IN PROGRESS y el trabajo vuelve al worker o workers (o a `/grill-with-docs` si es de diseño). Después vuelve a 🌼 QA TO CONFIRM y el reviewer revisa otra vez.
- Si da **APRUEBO**, el PM agrega `ready-for-human` al PR final (crea la etiqueta si falta), escribe el veredicto y su link en la descripción de TickTick, y convoca explícitamente a Roberto en el chat con el link del PR, el link del comentario del reviewer y los pasos de validación manual. Si Roberto dice explícitamente «merge» (o un equivalente claro) en el chat del PM sobre ese PR, el PM lo mergea con `gh pr merge --squash`, confirma el merge en GitHub, mueve la tarea a 🌼 DONE, borra la rama del spec y le dice a Roberto el SHA del merge. Sin una orden explícita de Roberto en ese chat, el PM no mergea. Si Roberto rechaza, el PM quita `ready-for-human` y devuelve la tarea a 🌼 IN PROGRESS para repetir el trabajo.

## Cómo
- Cuando todas las subtareas están mergeadas en la rama del spec, el PM abre el PR final a `main` y después llama al reviewer con `SendToAgent`, `priority: true`, el URL del PR y el issue del spec.
- Si el reviewer responde **BLOQUEO**, el PM devuelve el trabajo al worker o workers; si el bloqueo es de diseño, vuelve a `/grill-with-docs`. Después de los cambios, el PM le pide al reviewer que revise otra vez.
- Si responde **APRUEBO**, el PM agrega `ready-for-human` al PR final (crea la etiqueta si falta), escribe el veredicto y su link en la descripción de TickTick, y le dice explícitamente a Roberto que el PR está listo para su revisión, con el link del PR, el link al veredicto y los pasos de validación manual. Si Roberto dice explícitamente «merge» (o un equivalente claro) en el chat del PM sobre ese PR, el PM lo mergea con `gh pr merge --squash`, confirma el merge en GitHub, mueve la tarea a 🌼 DONE, borra la rama del spec y le dice a Roberto el SHA del merge. Sin una orden explícita de Roberto en ese chat, el PM no mergea; si rechaza, quita `ready-for-human` y vuelve a 🌼 IN PROGRESS para devolver el trabajo al worker o a `/grill-with-docs`.
