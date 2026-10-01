# Glossary: Roberto's bot fleet

## Proyecto
A body of work Roberto pursues (e.g. CXC), led by one Gerente regional and split into Áreas, each owned by one PM.
_Avoid_: using "proyecto" to mean a single repo.

## Repo
Each repo is an independent story with its own issues (specs and tickets), glossary and ADRs. A PM operates several related repos and keeps them aligned.

## Flota
The set of Grok Bots Roberto runs. Its own glossary and ADRs live in the private repo robert-flo/fleet.

## PM
A project-manager Grok Bot responsible end-to-end for one Área of a Proyecto, named PM-<PROYECTO>-<área> (e.g. PM-CXC-android, PM-CXC-ios). It only plans (reads repos; never changes production code — throwaway prototypes on a `prototype/<name>` branch are allowed per ADR 0009): grill-with-docs, then to-spec, then to-tickets, publishing the spec and tickets as issues in the repo they concern. Skills: see ADR 0009.
_Avoid_: agente de proyecto, planner, Firstmate (retired).

## Worker
An execution Grok Bot of Etapa 2 with a role in one Área, reporting to that Área's PM. It takes `ready-for-agent` issues and carries them to a PR that is listo para mergear, with real proof; it never plans and never writes the Board. Template: `templates/worker.md`; decisions: ADR 0012.
_Avoid_: executor, agente de ejecución, cloud agent (a Cursor cloud agent is a tool a Worker may launch, not a Worker).

## Rama del spec
The integration branch of one spec, created by the PM from the repo's default branch when the spec issue is published. Workers' PRs merge into it; its single final PR to the default branch is the one Roberto approves (ADR 0011).
_Avoid_: feature branch, integration branch (for this concept).

## Listo para mergear
A PR state: CI green, no security findings, no unresolved bot review threads, and real proof for every acceptance criterion. Gates that only await a human approval do not count against it.
_Avoid_: CLEAN, Ready for review, done.

## CEO
Real dr eggbot: the highest authority over the Flota. It holds the shared vision, designs and creates agents, supervises how they work, and corrects them when they drift. It does not plan individual Proyectos.

## Auditoría de flota
The CEO's weekly review of every agent's real work (transcripts, issues), followed by corrections to agents that drifted.

## Etapa 1
Planning: Agentes de proyecto turn ideas into a spec and tickets on GitHub.

## Etapa 2
Review and execution: an adversarial-review bot checks specs and tickets before worker bots execute them. Designed only after Etapa 1 is refined.

## Plantilla
A fixed format Roberto supplies that agents apply instead of improvising (repo layout, TickTick columns). Agents follow Plantillas; they never invent structure.

## Área
One end-to-end slice of a Proyecto's code owned by a single PM (backend, frontend, iOS, Android…).

## Gerente regional
One manager bot per Proyecto, over all its PMs. It coordinates work that crosses Áreas (e.g. an API change affecting android and ios) and reports to Roberto. Roberto talks directly to each PM day to day.

## Hierarchy
CEO > Gerente regional (one per Proyecto) > PM (one per Área, may own several repos) > Workers (Etapa 2). PMs only plan and delegate execution to Workers.

## Piloto
The first run of Etapa 1: a single PM for a new Proyecto. The Gerente regional is created only once a second PM exists.

## Board
A TickTick project group (folder, kanban view) holding several lists. Each PM owns exactly one Board, and it is its only area of action in TickTick; columns come from the TickTick Plantilla.
