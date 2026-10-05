# Glossary: Roberto's bot fleet

## Proyecto
A body of work Roberto pursues (e.g. CXC, reel). Each Proyecto (or Área) has its own PM; Workers execute (ADR 0015).
_Avoid_: using "proyecto" to mean a single repo.

## Repo
Each repo is an independent story with its own issues (specs and tickets), glossary and ADRs. A PM operates several related repos and keeps them aligned.

## Flota
The set of Grok Bots Roberto runs. Its own glossary and ADRs live in the private repo robert-flo/fleet.

## PM
A Grok Bot that owns one Proyecto or Área and runs Matt Pocock's flow (restate-goals, grill-with-docs, to-spec, to-tickets) up to `ready-for-agent` sub-issues, then follows each spec to its final PR (ADR 0015). Its rules are `templates/pm.md`; its data, its Ficha. Created by the CEO with the `create-pm` skill.
_Avoid_: agente de proyecto, planner.

## Worker
A specialized Grok Bot its PM creates for one spec or trivial with the `create-worker` skill (the CEO only when there is no PM or Roberto asks directly; ADR 0016). It runs `/implement-spec` or `/implement` on branches off the Rama del spec and reports to its PM. Rules: `templates/worker.md.backup` (ADR 0012, 0015); data: its Ficha. Its PM tracks it on the Notion «Workers» board; Roberto deletes it.
_Avoid_: executor, agente de ejecución, cloud agent (a Cursor cloud agent is a tool a Worker may launch, not a Worker).

## Reviewer
A Grok Bot that reviews only the final PR from a Rama del spec to the repo's default branch before Roberto reviews it, then comments `BLOQUEO` or `APRUEBO` (ADR 0017). On most repos that default is `main`; on personal forks it is `personal` (ADR 0024). The PM handles `ready-to-merge`, TickTick and summoning Roberto; the reviewer only comments and reports the verdict. Workers' sub-issue PRs do not go through it.

## Rama del spec
The integration branch of one spec, created by the PM from the repo's default branch when the spec issue is published. Workers' PRs merge into it; its single final PR to the default branch is the one Roberto approves (ADR 0011).
_Avoid_: feature branch, integration branch (for this concept).

## Listo para mergear
A PR state: CI green, no security findings, no unresolved bot review threads, and real proof for every acceptance criterion. Gates that only await a human approval do not count against it.
_Avoid_: CLEAN, Ready for review, done.

## CEO
Real dr eggbot: the highest authority over the Flota. It holds the shared vision, creates PMs (sending each its Mensaje de arranque) and supervises the fleet: reads the Notion Workers board and the «Aprendizajes» page and draws lessons from them. PMs create and track their own Workers (ADR 0015, 0016).

## Auditoría de flota
The CEO's weekly review of every agent's real work (transcripts, issues), followed by corrections to agents that drifted.

## Etapa 1
Planning: Agentes de proyecto turn ideas into a spec and tickets on GitHub.

## Etapa 2
Review and execution: an adversarial-review bot checks specs and tickets before worker bots execute them. Designed only after Etapa 1 is refined.

## Plantilla
A fixed format Roberto supplies that agents apply instead of improvising (repo layout, TickTick columns). Agents follow Plantillas; they never invent structure.

## Área
One end-to-end slice of a Proyecto's code (backend, frontend, iOS, Android…).

## Gerente regional
Retired by ADR 0014: it was one manager bot per Proyecto, over all its PMs. Eggbot coordinates work that crosses Áreas.

## Hierarchy
Roberto > CEO (eggbot) > PMs (one per Proyecto or Área) > Workers (specialized, per spec). ADR 0015 replaces ADR 0014's single-PM model.

## Piloto
Retired by ADR 0014: the first run of Etapa 1 with a single per-project PM.

## Board
A TickTick project group (folder, kanban view) holding several lists. Each PM owns exactly one Board, and it is its only area of action in TickTick; columns come from the TickTick Plantilla.

## Ficha
A bot's small instruction file, `bots/<NOMBRE>.md` in robert-flo/fleet, copied from `templates/ficha-pm.md` or `templates/ficha-worker.md`: its data and the list of rule files it loads (ADR 0015).
_Avoid_: putting rules in the profile description.

## Mensaje de arranque
The first message a bot's creator (the CEO for a PM, the PM for its Workers) sends it with SendToAgent right after CreateAgent, pointing it to its Ficha. It is the reliable channel for instructions; the profile description is not (ADR 0015, 0016).

## Log
A trace line `[log: <instrucción> · fuente=<origen>]` at the top of a bot's chat message, showing which rule it applied and where it came from; the first message carries the self-check of loaded files. Convention and on/off switch: `templates/logs.md`.
_Avoid_: using logs in issues, PRs or commits.

## Trío
The fixed team of one project: `PM-<project>`, `WK-<project>` and `RV-<project>` (ADR 0019). pj-fleet has no trío, only RV-pj-fleet (ADR 0020).
_Avoid_: equipo, squad.

## PC
Roberto's own computer, gracie (Omarchy, user `tanjiro`, projects in `~/Work/tries`). Every bot of a Trío, and RV-pj-fleet (ADR 0022), may do machine work there under `templates/tu-pc.md` (ADR 0022). Repo code still goes through cloud agents; nobody commits or pushes from the PC.
_Avoid_: host, box (the box is Grok Bot's own computer, not Roberto's).

## Bitácora
`~/Work/tries/CAMBIOS.md` on the PC: one line per system change, written before the change, with date, bot, command and how to undo it (ADR 0022).
_Avoid_: log (a Log is the trace line in a chat message).

## cursor-agent
Cursor's command-line agent installed on the PC. Bots launch it in a project folder for long machine work, on Roberto's Cursor quota. It is not a cloud agent: a cloud agent runs on Cursor's servers and opens PRs; cursor-agent runs on the PC and never commits.

## Impedimento
Something a bot cannot solve by itself, the only reason it stops working on the PC (`tu-pc.md`).
_Avoid_: bloqueo (BLOQUEO is a Reviewer verdict).

## personal
The long-lived branch of Roberto's customizations on every personal fork. It is the GitHub default branch of the fork, is protected, and takes day-to-day commits only via PRs (Template-style). The RV of that project's trío reviews those PRs, same Template/fleet flow already agreed (ADR 0024).
_Avoid_: treating `main` as the default on a personal fork once the fork has migrated.

## upstream
On a personal fork, the long-lived branch that is a fast-forward mirror of the tracked line of the real upstream project. It is a branch name, not only a git remote. Omarchy today still mirrors omacom's real `quattro` onto a local branch of that name; that mirror migrates to `upstream` (fetch still comes from omacom's `quattro`). Do not use `quattro` as the generic name for this branch (ADR 0024).
_Avoid_: quattro (as the generic name for the mirror).

## Board column ↔ triage role
A TickTick column tracks a whole spec; a triage role (Matt's `/triage` label) tracks one GitHub issue or PR. They are two views of the same work and use this one mapping (Matt: role names are canonical, tool strings may differ):

| TickTick column | Meaning | GitHub side |
|---|---|---|
| 🌼 MAYBE | Idea not grilled yet | An incoming external issue carries `needs-triage` |
| 🌼 INVESTIGATING | `/grill-with-docs` → `/to-spec` → `/to-tickets` running | Spec issue being written |
| 🌼 IN PROGRESS | Worker implementing the sub-issues | Sub-issues carry `ready-for-agent` |
| 🌼 ON HOLD | Paused on a blocker | `needs-info` when waiting on Roberto or a reporter |
| 🌼 QA TO CONFIRM | Final PR open, reviewer's turn | After APRUEBO the PR carries `ready-to-merge` (our label for Matt's `ready-for-human` role, see `docs/agents/triage-labels.md`) |
| 🌼 DONE | Merged to the default branch | Spec and sub-issues closed, `ready-to-merge` removed from the merged PR (no triage role after merge); a discarded spec closes as `wontfix` |
