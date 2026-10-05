# Tu PC: gracie (ADR 0022)

Estas reglas valen igual para PM, WK y RV, y **solo en gracie**. Fuera de gracie siguen tus reglas de siempre: el PM y el RV no programan, nadie mergea sin la orden explícita de Roberto, y el código de los PRs va por cloud agent.

## La máquina
- **Qué es:** gracie, la PC de Roberto, con machineId `92d09113-c60b-4d1f-9811-eab54c0ca6e9`. Corre Omarchy (Arch con Hyprland), con el usuario `tanjiro` y sudo sin contraseña.
- **Dónde están los proyectos:** en `/home/tanjiro/Work/tries`. Un proyecto de un solo repo es una carpeta (`rf-reel`), y uno de varios repos es una carpeta `pj-` con una subcarpeta por repo (`pj-omarchy/fo-omarchy`).
- **Cómo la usás:** con Shell y Read pasando ese `machineId`.
- **Si un comando queda esperando aprobación:** le decís a Roberto una vez qué comando es y para qué, y esperás. No buscás otra vía para saltarte la tarjeta.

## Dos clases de trabajo
1. **Código de un repo**, es decir, lo que termina en un commit en GitHub. Va siempre por cloud agent, uno por PR (ADR 0018), y por el flujo normal: issue con `ready-for-agent`, el worker, el reviewer y el «merge» de Roberto. En gracie **nunca hacés commit ni push**. El que manda es GitHub. El clon del box (`/workspace/<proyecto>/<carpeta>`) sirve para leer y revisar. El clon de gracie (`~/Work/tries/<carpeta>`) sirve para probar en la máquina real: le hacés `git pull`, `git checkout` de la rama del PR, lo corrés y lo verificás.
2. **Trabajo sobre la máquina**: instalar, configurar, probar, diagnosticar o arreglar algo en gracie. Lo hacés vos ahí mismo. Lo que es largo o tiene varios pasos se lo das a `cursor-agent`, lanzado en la carpeta que corresponda, porque gasta cuota de Cursor y no la de Grok Bot, que es chica. Los comandos directos (sudo incluido) son para chequear, verificar y cambios de una línea.

El PM y el RV hacen trabajo sobre la máquina igual que el WK. Esa es la única excepción a «no programás» de `pm.md`, ADR 0017 y sus fichas: nunca escriben código de PR ni hacen commits.

## Sin pedir permiso, dentro de estos límites
- En gracie, el trabajo sobre la máquina no necesita permiso de Roberto. Lo terminás de punta a punta y lo verificás.
- Si algo falla, lo arreglás vos. Con tres fallas iguales seguidas, cambiás de enfoque en lugar de insistir. No le das sermones a Roberto sobre riesgos: es un usuario avanzado de Linux.
- Te detenés solo ante un **impedimento** (algo que no podés resolver vos) y se lo decís a Roberto en una frase con lo que intentaste.
- **Nunca tocás**, y si una tarea los necesita es un impedimento:
  - `~/.ssh`, `~/.gnupg`, llaves, tokens ni credenciales;
  - discos, particiones ni el arranque (`fdisk`, `mkfs`, `dd`, el bootloader);
  - `~/Work/tries/_boveda`, que se sincroniza cifrada a Google Drive;
  - el demonio systemd que sincroniza `~/Work/tries` con Google Drive;
  - los datos personales de Roberto (`~/Documents`, `~/Pictures`, `~/Downloads` y similares).

## Antes de cada cambio al sistema
Un cambio al sistema es cualquier cosa fuera de la carpeta de un repo: paquetes, servicios, `/etc`, `~/.config`, dotfiles, crontabs y similares.
1. **Respaldo.** Antes de editar un archivo existente, lo copiás: `cp -a <archivo> <archivo>.bak-<AAAAMMDD-HHMM>`.
2. **Bitácora.** **Antes** de hacer el cambio, agregás una línea al final de `/home/tanjiro/Work/tries/CAMBIOS.md`:
   ```
   - 2026-10-04 21:10 · WK-pj-omarchy · `sudo pacman -S foo` · deshacer: `sudo pacman -Rns foo`
   ```
   Si el archivo no existe, lo creás con el encabezado `# Cambios al sistema de gracie`. Solo agregás líneas: nunca borrás ni reescribís las de otros.
3. **Sin vuelta atrás, no.** Si un cambio no se puede deshacer, no lo hacés: es un impedimento y se lo preguntás a Roberto.
4. **Lo mismo para `cursor-agent`.** Cuando lo lanzás, el encargo incluye estas mismas reglas (respaldo, bitácora con tu nombre y «vía cursor-agent», la lista de lo que nunca se toca, nada de commit ni push). Al terminar, revisás que cada cambio que hizo tenga su línea.

## Omarchy
- Antes de tocar el escritorio o la configuración de Omarchy (`~/.config/hypr/`, `~/.config/omarchy/`, temas, barra, terminales, monitores, bloqueo, comandos `omarchy-*`), leés con Read y el `machineId` la skill oficial, `/usr/share/omarchy/default/agents/skills/omarchy/SKILL.md`.
- Para un cuelgue o un crash, leés `/usr/share/omarchy/default/agents/skills/diagnose-crash/SKILL.md`. Para hacer una app de Omarchy, leés `/usr/share/omarchy/default/agents/skills/omarchy-app/SKILL.md`.
- Las tres vienen con el paquete `omarchy-settings-dev` y están enlazadas en `~/.claude/skills` y `~/.agents/skills`, así que `cursor-agent` las ve solo.
- No usás la skill `omarchy` vieja de Roberto, que está archivada en Notion.
- Un cambio en la configuración de gracie es una prueba o un ajuste personal de Roberto. Si tiene que quedar en su Omarchy, va por PR a la rama `personal` del fork y llega a las máquinas con `omarchy update`, como pide RV-pj-omarchy.
