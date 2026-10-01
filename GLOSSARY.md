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
CEO > Gerente regional (one per Proyecto) > PM (one per Área, may own several repos) > worker bots (Etapa 2, not modeled yet). PMs only plan and delegate execution.

## Piloto
The first run of Etapa 1: a single PM for a new Proyecto. The Gerente regional is created only once a second PM exists.

## Board
A TickTick project group (folder, kanban view) holding several lists. Each PM owns exactly one Board, and it is its only area of action in TickTick; columns come from the TickTick Plantilla.
