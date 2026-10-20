Yes—that AI explainer was generated using this system. **The easiest way to invoke it is to give the agent a clear request in chat.**

### Start a new episode

Copy this and replace the details:

```text
Use this repository’s production system.
Read CLAUDE.md and CORE/PIPELINE/CONTRACT.md.

Niche: 001 — AI + Technology Explainers
Topic/question: [What should this episode explain?]
Audience: General public
Language: English
Duration: 600 seconds
Media generation: I will generate it externally using AI tools.

Choose an appropriate registered angle.
Use autonomous mode and complete Phases 0–5.
Validate each phase, preserve source references, and report
any unresolved review requirements without inventing approvals.
```

You can also provide an existing **idea ID** instead of a new topic.

### Continue an existing episode

Specify its folder and the next action:

```text
Continue this project:
OUTPUT/017_kids_cartoon_stories/017_kids_cartoon_stories_creative_brief_pip_birthday_cake/

Read its configuration and current progress.
Complete the next unfinished phase and validate it.
```

### Use the terminal

Run from `F:\The Script of 1`:

```powershell
python -m Tools.projects.create_project --id 001 --angle how_it_works --story-question "How does a Transformer combine information?" --episode-slug transformer_information --mode autonomous
```

**This command creates the configuration and draft production files.** The agent then researches and writes the remaining phases.

The reference is [INVOKE_COMMANDS.md](</F:/The Script of 1/CORE/RULES/INVOKE_COMMANDS.md>). Phrases such as `/run_all` are not executable commands in this repository.


==============


Other 

=======================


Yes. **You can give just the topic**, and the agent can search the registry, select the niche and angle, then prepare the script.

For example:

> Create a Hindi script about the Pandavas’ exile in the Mahabharata. Find the most suitable niche and angle automatically. Make it 10 minutes long for a general audience. Ask me only if an important decision is unclear.

### Two ways to run it

| Mode | What happens |
|---|---|
| **Interactive** | The agent proposes the niche and angle, asks about missing details, and pauses at review stages. |
| **Autonomous** | The agent selects suitable defaults, records its choices, researches and generates the text package, reporting unresolved requirements. |

For your example, the workflow would be:

**“Pandavas” → search niche registry → choose relevant angle → narrow the episode → configure → research → script → scenes and prompts.**

“Pandavas” is broad, so the agent may ask whether you want their childhood, exile, relationships, war decisions or complete journey. If you specify **“Pandavas’ exile,”** it can proceed with fewer questions. It should also identify which text or retelling it follows.

**Current distinction:** this works through an agent interpreting your request. The Python creation command still requires a niche ID; a dedicated automatic topic-routing command has not been implemented.

You can explicitly say:

> Find the niche and angle yourself. Use reasonable defaults for missing details, show the selected configuration, and continue autonomously.


======================

other one 


======================

Yes—**mention the entry instructions once**, together with your topic. You don’t need to list every template or choose a niche yourself.

Use this reusable prompt:

```text
Use the production system in this workspace.

First read:
- CLAUDE.md
- CORE/PIPELINE/CONTRACT.md
- CORE/RULES/INVOKE_COMMANDS.md

Topic: The Pandavas’ exile in the Mahabharata.
Language: Hindi.
Audience: General public.
Duration: 10 minutes.
Mode: Autonomous.

Search the registry and select the most suitable niche
and registered angle. Record why they fit.

Use the relevant niche configuration and phase templates.
Identify the text or retelling used for research.
Ask only when an essential decision cannot reasonably
be inferred; otherwise record your assumptions and proceed.

Complete Phases 0–5: configuration, research, production
bible, scene breakdown, compiled package and final audit.

Prepare scene-linked prompts for external AI generation.
I will generate the media myself.

Validate each phase, preserve citations, and report unresolved
requirements without inventing facts or approval records.
```

For another episode, replace the **topic, language, audience and duration**.

You can keep this in `Prompt for Invoke.md` and later say:

> Read `Prompt for Invoke.md` and follow it for this topic: [your topic].

===================


Use the production system in this workspace.

First read:
- CLAUDE.md
- CORE/PIPELINE/CONTRACT.md
- CORE/RULES/INVOKE_COMMANDS.md

Topic: The Pandavas’ exile in the Mahabharata.
Language: Hindi.
Audience: General public.
Duration: 10 minutes.
Mode: Autonomous.

Search the registry and select the most suitable niche
and registered angle. Record why they fit.

Use the relevant niche configuration and phase templates.
Identify the text or retelling used for research.
Ask only when an essential decision cannot reasonably
be inferred; otherwise record your assumptions and proceed.

Complete Phases 0–5: configuration, research, production
bible, scene breakdown, compiled package and final audit.

Prepare scene-linked prompts for external AI generation.
I will generate the media myself.

Validate each phase, preserve citations, and report unresolved
requirements without inventing facts or approval records.