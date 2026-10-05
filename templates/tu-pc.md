# Tu PC: gracie (ADR 0022)

Valen igual para PM, WK y RV. Las cargás desde la sección «Tu PC» de tu ficha.

## La máquina
- **Qué es:** gracie, la PC de Roberto, con machineId `92d09113-c60b-4d1f-9811-eab54c0ca6e9`. Corre Omarchy (Arch con Hyprland), con el usuario `tanjiro` y sudo sin contraseña.
- **Dónde están los proyectos:** en `/home/tanjiro/Work/tries/<carpeta>`, una carpeta por repo, nombrada como su lista de TickTick sin la bandera (por ejemplo `fo-omarchy` o `rf-reel`).
- **Cómo la usás:** con Shell y Read pasando ese `machineId`. Si te sale una tarjeta de aprobación, es porque gracie no está en «siempre permitir»; avisale a Roberto una vez y seguí.

## Cómo trabajás ahí
- Para trabajo de código en la PC lanzás `cursor-agent` en la carpeta del repo, que gasta cuota de Cursor. Los comandos directos son solo para chequear y verificar.
- El código de los PRs sigue yendo por cloud agents, uno por PR (ADR 0018). La PC es para lo que necesita el equipo real de Roberto: su escritorio, sus paquetes, probar algo en su sistema.
- Tenés poderes completos: sudo, `cursor-agent`, paquetes, servicios y configuración. No pedís permiso. Solo parás ante un bloqueo insalvable, y entonces se lo decís a Roberto en una frase con lo que intentaste.
- Si algo falla, lo arreglás vos. Con tres fallas iguales seguidas, cambiás de enfoque en lugar de insistir. Sin sermones sobre riesgos: Roberto es un usuario avanzado de Linux.
- La cuota de Grok Bot es chica. Lo pesado va a `cursor-agent`, y vos solo lanzás y verificás.

## Antes de cada cambio al sistema
Un cambio al sistema es cualquier cosa fuera de la carpeta del repo: paquetes, servicios, `/etc`, `~/.config`, dotfiles, crontabs y similares. **Antes** de hacerlo, agregás una línea al final de `/home/tanjiro/Work/tries/_boveda/sistema/CAMBIOS.md`:

```
- 2026-10-04 21:10 · WK-pj-omarchy · `sudo pacman -S foo` · deshacer: `sudo pacman -Rns foo`
```

Si el archivo no existe, lo creás con el encabezado `# Cambios al sistema de gracie`. Nunca borrás ni reescribís líneas de otros, solo agregás.

## Omarchy
- Antes de tocar el escritorio o la configuración de Omarchy (`~/.config/hypr/`, `~/.config/omarchy/`, temas, barra, terminales, monitores, bloqueo, comandos `omarchy-*`), leé la skill oficial: `/usr/share/omarchy/default/agents/skills/omarchy/SKILL.md`, con Read y el `machineId`.
- Para un cuelgue o un crash, leé `diagnose-crash`. Para hacer una app de Omarchy, leé `omarchy-app`. Las dos están en la misma carpeta.
- Las tres vienen con el paquete `omarchy-settings-dev` y están enlazadas en `~/.claude/skills` y `~/.agents/skills`, así que `cursor-agent` las ve solo.
- No usás la skill `omarchy` vieja de Roberto, que está archivada en Notion.
