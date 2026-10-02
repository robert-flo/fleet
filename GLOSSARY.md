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
A Grok Bot that reviews only the final PR from a Rama del spec to `main` before Roberto reviews it, then comments `BLOQUEO` or `APRUEBO` (ADR 0017). The PM handles `ready-for-human`, TickTick and summoning Roberto; the reviewer only comments and reports the verdict. Workers' sub-issue PRs do not go through it.

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
