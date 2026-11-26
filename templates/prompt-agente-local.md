# Plantilla: prompt para el agente local de Roberto

Estructura de los prompts que Roberto le pasa a su agente de código local (en su PC) para resolver un spec y sus tickets en una sola rama y un solo PR. Sale de los prompts que se usaron con `kodigo-grupo-12/monorepo` (specs #105, #106 y #107) y con `robert-flo/monorepo-pruebas` (spec #15), el 2026-11-26.

## Cómo se usa

- Todo lo que está dentro del bloque de código se copia en el prompt.
- Los bloques fijos van **palabra por palabra**: no se reescriben, no se traducen y no se resumen.
- Cada `<...>` es una parte variable. Se reemplaza entero, con la línea de guía de arriba (`<!-- ... -->`) como criterio, y se borra la línea de guía.
- Las secciones marcadas «(opcional)» se omiten enteras si no aplican.
- Un prompt cubre un spec, o una fase de un spec, y abre un PR. Si un spec tiene varias fases con PRs distintos, va un prompt por fase en el mismo archivo, con un encabezado que diga el orden.
- Encima del bloque de código, para Roberto (no para el agente), va un resumen corto: qué prompt va primero y qué tiene que estar mergeado antes.
- El remolque `Co-authored-by` es parte del formato de Roberto para la org (rotación del grupo). Es la única excepción a la regla de la flota «sin trailers `Co-authored-by`», y solo vive dentro de estos prompts. Si la rotación del grupo pide a otra persona, Roberto lo cambia; el PM no lo cambia solo.

## Plantilla

```
Importante: sin firma ni pie de agente o plataforma en commits, PRs ni comentarios. Escribí como una persona.

Modo de trabajo (vale para todo el cambio): el cambio más pequeño que resuelve el problema; un test que falla antes de tocar código (si un test honesto no es práctico, no escribas uno falso); arregla la causa raíz, no el síntoma; si dos arreglos que comparten una premisa fallan el mismo gate, escribe la premisa en una frase y elimínala antes de seguir. Antes de abrir el PR itera hasta que TUS gates pasen limpios, re-corriendo los comandos tras cada cambio. Regla dura: todo hallazgo de un run real (dispatch, CI, push, instalación) se convierte en aserción estática en la suite antes de abrir el PR, para que esa clase de fallo no vuelva. Apunta al estado final verificable, no a pasos.

<!-- Pedido: issues en orden, repo, tema, spec padre, una sola rama y un PR, implement-spec y los bloqueos. -->
Hola, necesito que resolvás los issues <#a, #b y #c> de <owner/repo>: <tema en una frase> según el spec <#spec>, todo sobre una sola rama de integración y en un único PR, con el flujo de implement-spec (un subagente por ticket, en ese orden; <#b va bloqueado por #a, …>). Cada sub-issue tiene su cuerpo en el tracker con <el detalle, los archivos, las funciones, los mensajes exactos>, sus criterios y la prueba que pide cada criterio.

<!-- Contexto: estado de main, de qué viene esto (port o diseño nuevo), qué ya está comprobado, ADR y decisiones que no se reabren. -->
Contexto: <qué hay hoy en main que importa; si es un port, de dónde y con qué commits; qué se comprobó y con qué resultado>.

<!-- Orden (opcional): dónde cae este prompt entre varios specs o fases, y qué hace este agente. -->
Orden: <este es el N de M: X (#…, rama …) → Y (#…, rama …)>. Vos hacés solo <X>.

<!-- Precondición (opcional): qué tiene que estar mergeado, el comando exacto para comprobarlo sobre origin/main y la orden de parar si no se cumple. -->
Precondición: <el PR de … tiene que estar mergeado en main>. Comprobalo con <comando> sobre origin/main; si no, pará y decímelo.

<!-- Pasos de rama: crear la rama desde origin/main y remotos extra si hay port. -->
Pasos de rama: git fetch origin && git switch -c <rama> origin/main.

<!-- Estado de servicios externos (opcional): Firebase, consola, datos de producción; qué ya se hizo a mano, con fecha, y qué no se toca. -->
Estado de <servicio> (<fecha>): <qué está hecho y qué no>.

<!-- Reglas o hallazgos que no se reabren (opcional): decisiones cerradas que el agente podría querer cambiar. -->
<Reglas que no se reabren:>
- <regla>

<!-- Choques (opcional): archivos que comparte con otros specs o PRs abiertos y qué conservar al rebasar. -->
Choques: <archivo> lo toca también <spec o PR>: <qué conservar>.

<!-- Gotchas (opcional): trampas conocidas del repo o del entorno, con lo que hay que hacer. -->
Gotchas conocidos:
- <gotcha>

<!-- Evidencia (opcional): cómo levantar el entorno para capturas y videos (emuladores, build igual al de producción, puerto) y qué hacer si no se puede grabar. -->
Para la evidencia: <pasos>. Si no podés grabar o capturar, dejá ese criterio sin marcar y decilo; no lo sustituyas.

<!-- Prohibido: despliegues, consolas, datos reales, ramas o repos ajenos. -->
Prohibido:
- <acción>

<!-- Skills: cuáles cargar y para qué (según el repo: cwb-mobile-ui y theming si hay UI nueva) y cuáles no. -->
Skills: <cargá … (para …) | no cargues …>. No cargues <cwb-local-first, cwb-ship-coach, cwb-app-launch, cwb-onboarding, local-build, implement ni tdd>.

Cada commit de la rama lleva este remolque en el mensaje, tal cual:
Co-authored-by: kevingeogarcia <38563386+kevingeogarcia@users.noreply.github.com>

<!-- Qué construir: un punto por ticket, en orden, con el título del commit, los archivos y funciones por nombre y las pruebas. -->
Qué construir (en orden):
- <#a> (commit «<a> - <título>»): <qué, con archivos, funciones y tests>.
- <#b> (commit «<b> - <título>»): <…>.

No cambies el comportamiento de nada más. Sin force-push.

<!-- Gates: los comandos exactos de typecheck y tests del repo. -->
Corré los comandos de typecheck y tests del repo (<comandos>) y decime cuáles corriste.

<!-- PR: rama, Closes de cada ticket, spec padre, seguimiento (si hay) y qué dice Merge Danger. -->
Abrí un PR desde la rama <rama> contra main, con «Closes #a, Closes #b», «Spec padre: #spec»<, «Seguimiento: owner/repo#n»> y las secciones Summary, Evidence y Merge Danger en el cuerpo. Merge Danger dice:
- <riesgo de mergear y qué hay que hacer antes o después, con quién lo aprueba>.
Las capturas y videos que piden los criterios van en robert-flo/assets/<repo>/pr-<n>/ con el sha en el nombre. Cuando termines, respondeme con el formato de «Respuesta final» de abajo.

Formato de tu respuesta final:
- Primera línea: «Listo. PR: <link> — sha del último commit: <sha completo>, CI <verde/rojo> (<qué jobs>).»
- Un párrafo por commit (o por cambio, si es uno solo): <sha corto>, qué cambió y por qué, con archivos y funciones por nombre, y qué test nuevo lo cubre.
- Lo que encontraste y no estaba en el pedido: choques con la rama por defecto, supuestos que no se cumplían, decisiones que tomaste. Una línea cada uno, diciendo qué hiciste.
- Tests: qué comandos corriste, cuántos ok y fail, y cuáles fallan también en la rama por defecto limpia, con la causa.
- Lo que no hiciste o dejaste pendiente, si hay.
Sin saludo ni resumen al final.
```
