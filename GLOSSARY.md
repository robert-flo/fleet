# Glossary: Roberto's bot fleet

## Proyecto
A body of work Roberto pursues (e.g. CXC, reel). Eggbot is the PM of every Proyecto; Workers execute (ADR 0014).
_Avoid_: using "proyecto" to mean a single repo.

## Repo
Each repo is an independent story with its own issues (specs and tickets), glossary and ADRs. A PM operates several related repos and keeps them aligned.

## Flota
The set of Grok Bots Roberto runs. Its own glossary and ADRs live in the private repo robert-flo/fleet.

## PM
Real dr eggbot, Roberto's single PM for every Proyecto (ADR 0014). There are no per-project PM bots anymore: the PM-<PROYECTO>-<área> bots of ADR 0001 and 0009–0013 are retired; the `create-pm` skill stays intact.
_Avoid_: agente de proyecto, planner, PM-<PROYECTO>-<área> (retired).

## Worker
A disposable Grok Bot created by eggbot from `templates/worker.md` when Roberto asks. Roberto talks to it directly to iterate its PR, ask for the merge, or drop it, and he deletes it himself once he's done. Inside, it may launch Cursor cloud agents to write the code. Eggbot keeps it on the tracking board and records lessons before it is deleted. Decisions: ADR 0014; skill: `create-worker`.
_Avoid_: executor, agente de ejecución, cloud agent (a Cursor cloud agent is a tool a Worker may launch, not a Worker).

## Rama del spec
The integration branch of one spec, created by the PM from the repo's default branch when the spec issue is published. Workers' PRs merge into it; its single final PR to the default branch is the one Roberto approves (ADR 0011).
_Avoid_: feature branch, integration branch (for this concept).

## Listo para mergear
A PR state: CI green, no security findings, no unresolved bot review threads, and real proof for every acceptance criterion. Gates that only await a human approval do not count against it.
_Avoid_: CLEAN, Ready for review, done.

## CEO
Real dr eggbot: the highest authority over the Flota and, since ADR 0014, also its single PM. It holds the shared vision, plans the Proyectos, creates Workers when Roberto asks, and keeps the Workers board.

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
Roberto > eggbot (CEO and single PM) > Workers (disposable, one per request). ADR 0014 replaces the old CEO > Gerente regional > PM > Workers chain.

## Piloto
Retired by ADR 0014: the first run of Etapa 1 with a single per-project PM.

## Board
A TickTick project group (folder, kanban view) holding several lists. Each PM owns exactly one Board, and it is its only area of action in TickTick; columns come from the TickTick Plantilla.
