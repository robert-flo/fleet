# Request flow and the PM's slice of it

Roberto's flow (also in robert-flo/Template AGENTS.md):

1. New request → classify Trivial or Engineering (Task Sizing criteria), state the classification and path out loud, and give Roberto a cheap veto before starting.
2. Trivial → /implement.
3. Engineering → /grill-with-docs, repeated in the same context until design ambiguity is resolved → /to-spec → multi-session build? (per ask-matt, not file count)
   - No → /implement from the spec, same context.
   - Yes → /to-tickets → /implement per ticket, fresh context each (via handoff if needed).
4. /code-review (standards + spec) → commit → push → PR into master (never direct commits).

The PM owns only the design part: classification + veto, grill-with-docs, to-spec, the multi-session decision, and to-tickets. Everything from /implement onward is execution (Etapa 2). So the hand-off to Etapa 2 can be a trivial request, a spec alone, or a spec plus tickets; each gets `ready-for-agent` only with verifiable acceptance criteria.

TickTick: 🌼 QA TO CONFIRM means all work is done and a PR is about to go up; it is not where the PM's planning results land.
