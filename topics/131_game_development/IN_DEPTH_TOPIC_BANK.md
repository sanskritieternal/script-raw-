# 131 — Game Development: main topic bank

Updated: 2026-10-23 · **35 active BANK proposals · 7 categories · 8 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Original bounded cases and mechanisms](#catalog-131-r01) → [Rules, state and feedback](#catalog-131-r05).
- **Intermediate:** [Original bounded cases and mechanisms](#catalog-131-r02) → [Original bounded cases and mechanisms](#catalog-131-r03) → [Worlds, content and networking](#catalog-131-r06).
- **Advanced:** [Original bounded cases and mechanisms](#catalog-131-r04) → [Accessibility and release](#catalog-131-r07) → [Finding frame-time bottlenecks](#catalog-131-r08).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Tier 1: Foundational Frameworks](#domain-131-01) | 5 | 0 | 0 |
| [Tier 2: Practical Mechanics & Channels](#domain-131-02) | 0 | 5 | 0 |
| [Tier 3: Strategic & Advanced Architectures](#domain-131-03) | 0 | 5 | 0 |
| [Tier 4: Future Horizons & Masterclasses](#domain-131-04) | 0 | 0 | 5 |
| [Game foundations](#domain-131-05) | 4 | 0 | 0 |
| [Game production](#domain-131-06) | 0 | 4 | 0 |
| [Game evaluation](#domain-131-07) | 0 | 0 | 7 |

<a id="domain-131-01"></a>
## Category: Tier 1: Foundational Frameworks

<a id="catalog-131-r01"></a>
### Original bounded cases and mechanisms

Subcategory `CATALOG-131-R01` · foundation.

<a id="bank-131-010"></a>
#### BANK-131-010 — The Core Gameplay Loop: How 30 Seconds of Fun Built Halo and Mario

**Video question:** How did Bungie's '30 seconds of fun repeated thousands of times' philosophy create the greatest console shooter in history?

**Individual coverage scope:** The Golden Triangle of Halo (guns, grenades, melee), Nintendo's jump curve physics, action-feedback loops, and player retention.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-131-011"></a>
#### BANK-131-011 — The Game Loop and Delta Time: The Code That Powers Every Game

**Video question:** What happens under the hood when a game processes user input, updates physics, and renders pixels 60 times a second?

**Individual coverage scope:** ProcessInput -> Update -> Render, variable vs fixed time-steps, delta time (dt) frame rate independence, and preventing physics explosions at high FPS.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-131-012"></a>
#### BANK-131-012 — Juice It or Lose It: The Art of Screenshake, Particles, and Game Feel

**Video question:** How does adding 3 frames of hit-stop, a 5-pixel screen rumble, and white flash turn a boring square into a satisfying weapon?

**Individual coverage scope:** Jan Willem Nijman's Vlambeer design principles, freeze frames, sound design layering, squash-and-stretch animation, and micro-satisfactions.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-131-013"></a>
#### BANK-131-013 — Collision Detection: How Computers Know When Two Virtual Objects Touch

**Video question:** How do physics engines detect bullet hits without lagging the CPU using Axis-Aligned Bounding Boxes and SAT?

**Individual coverage scope:** AABB broad-phase pruning, Separating Axis Theorem (SAT) for convex polygons, spatial hashing, raycasting, and tunneling bullet glitches.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-131-014"></a>
#### BANK-131-014 — The Psychology of Flow in Games: Pacing, Difficulty Curves, and Frustration

**Video question:** How do games like Dark Souls and Celeste keep players in the sweet spot between boring ease and rage-quitting despair?

**Individual coverage scope:** Mihaly Csikszentmihalyi's flow channel, dynamic difficulty adjustment (Resident Evil 4), failure feedback framing, and player mastery loops.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.


<a id="domain-131-02"></a>
## Category: Tier 2: Practical Mechanics & Channels

<a id="catalog-131-r02"></a>
### Original bounded cases and mechanisms

Subcategory `CATALOG-131-R02` · intermediate.

<a id="bank-131-015"></a>
#### BANK-131-015 — Level Design Architecture: Leading the Player's Eye Without Breadcrumbs

**Video question:** How does Valve's Half-Life 2 guide players through complex city ruins using light contrast, architectural silhouettes, and weenies?

**Individual coverage scope:** Walt Disney's 'weenie' visual landmarks, contrasting light pools, architectural lines pointing to goals, pinch points, and psychological affordances.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-131-016"></a>
#### BANK-131-016 — Shader Programming: The Math of Painting Light on Polygonal Surfaces

**Video question:** How do vertex and fragment shaders calculate specular shine, metallic roughness, and water ripples on GPU cores?

**Individual coverage scope:** Graphics pipeline (rasterization), Phong vs PBR (Physically Based Rendering) lighting models, normal mapping optical illusions, and HLSL code.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-131-017"></a>
#### BANK-131-017 — Procedural Generation: How Spelunky and Minecraft Build Infinite Worlds

**Video question:** How do algorithms generate unique, beatable dungeons and continental mountain ranges from a single numerical seed?

**Individual coverage scope:** Perlin and Simplex noise, Derek Yu's Spelunky room-template grid algorithm, cellular automata cave generation, and guaranteeing level solvability.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-131-018"></a>
#### BANK-131-018 — Finite State Machines vs Behavior Trees: Programming Game AI

**Video question:** Why did Halo 2 abandon basic state machines (Patrol, Alert, Attack) for modular behavior trees?

**Individual coverage scope:** FSM spaghetti code breakdown, behavior tree Composites (Selectors/Sequences), decorators, blackboard memory, and reactive enemy coordination.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-131-019"></a>
#### BANK-131-019 — Multiplayer Netcode: Client-Side Prediction, Reconciliation, and Rollback

**Video question:** How do online shooters and fighting games (GGPO) eliminate lag when player signals take 80ms to cross continents?

**Individual coverage scope:** Deterministic lockstep vs client prediction, server reconciliation rubberbanding, lag compensation rewind, and fighting game rollback mechanics.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.


<a id="domain-131-03"></a>
## Category: Tier 3: Strategic & Advanced Architectures

<a id="catalog-131-r03"></a>
### Original bounded cases and mechanisms

Subcategory `CATALOG-131-R03` · intermediate.

<a id="bank-131-020"></a>
#### BANK-131-020 — The Immersive Sim: Looking Glass Studios and Emergent Gameplay

**Video question:** How did System Shock and Deus Ex invent games where player curiosity and physical simulation break developer expectations?

**Individual coverage scope:** Warren Spector's rules of immersion, systemic consistency (if it looks flammable, it must burn), player agency, and emergent problem solving.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-131-021"></a>
#### BANK-131-021 — A* Pathfinding: How Game Characters Navigate Massive Game Maps in Milliseconds

**Video question:** How do hundreds of RTS units find the shortest route through a winding maze without bringing the CPU to a screeching halt?

**Individual coverage scope:** Dijkstra's algorithm, heuristic distance functions (Manhattan/Euclidean), priority queues, navigation meshes (NavMesh), and funnelling path smoothing.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-131-022"></a>
#### BANK-131-022 — The Tragedy of Development Hell: Why Duke Nukem Forever and Daikatana Failed

**Video question:** How do brilliant game directors trap multi-million dollar projects in 14-year development nightmares?

**Individual coverage scope:** Feature creep, engine-switching traps (Quake II to Unreal to Unreal 2), lack of vertical slice discipline, perfectionism, and sunk cost fallacy.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-131-023"></a>
#### BANK-131-023 — Data-Oriented Design (ECS): Squeezing 100,000 Entities on Screen

**Video question:** Why does traditional Object-Oriented Programming (OOP) choke modern CPU caches, and how does Entity Component System fix it?

**Individual coverage scope:** L1/L2 CPU cache lines, cache misses, array-of-structures vs structure-of-arrays, Unity DOTS, and mass parallel data processing.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-131-024"></a>
#### BANK-131-024 — Predatory Monetization: The Dark Psychology of Gacha, Loot Boxes, and Battle Passes

**Video question:** How do mobile gaming algorithms deploy Skinner Box operant conditioning and variable reward schedules to hunt 'whales'?

**Individual coverage scope:** B.F. Skinner variable ratio rewards, FOMO artificial urgency, loss aversion, anchoring premium currencies, and European gambling regulatory crackdowns.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.


<a id="domain-131-04"></a>
## Category: Tier 4: Future Horizons & Masterclasses

<a id="catalog-131-r04"></a>
### Original bounded cases and mechanisms

Subcategory `CATALOG-131-R04` · advanced.

<a id="bank-131-025"></a>
#### BANK-131-025 — Interactive Audio: Dynamic Music Systems and Vertical Layering in Video Games

**Video question:** How does the soundtrack of Red Dead Redemption 2 seamlessly add percussion when combat starts and fade to violin when you win?

**Individual coverage scope:** Vertical layering (stems fading based on game state parameters), horizontal re-sequencing (metric-boundary transitions), Wwise and FMOD middleware.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-131-026"></a>
#### BANK-131-026 — The Solo Indie Phenomenon: How Stardew Valley and Undertale Made Millions

**Video question:** How did Eric Barone spend 4.5 years working 12-hour days in total isolation to create a $100M agricultural empire alone?

**Individual coverage scope:** Full-stack solo discipline (art, code, music, design), scope management, community goodwill marketing, and surviving extreme isolation.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-131-027"></a>
#### BANK-131-027 — Procedural Animation and Ragdoll Physics: The Euphoria Engine Behind GTA

**Video question:** Why do pedestrians in Grand Theft Auto IV realistically stumble down stairs and reach for handrails instead of playing canned death animations?

**Individual coverage scope:** NaturalMotion Euphoria engine, active biomechanical ragdolls, self-balancing PID controllers, muscle actuation, and procedural collision responses.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-131-028"></a>
#### BANK-131-028 — Unreal Engine 5: Nanite, Lumen, and the Disappearance of Polygon Budgets

**Video question:** How does Nanite render billions of micro-polygons directly from film-quality ZBrush sculpts without baking normal maps?

**Individual coverage scope:** Virtualized cluster geometry, continuous Level of Detail (LOD) down to 1 pixel, Lumen software/hardware ray-traced global illumination, and VRAM bandwidth.

**Research follow-up:** [Bounded case and source-access note](RESEARCH_NOTES/BANK-131-044.md). This does not change proposal or production status.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-131-029"></a>
#### BANK-131-029 — The Master Game Design Architecture: From Prototype to Commercial Masterpiece

**Video question:** What comprehensive production framework unites greybox prototyping, vertical slices, playtesting telemetry, and post-launch liveops?

**Individual coverage scope:** Rapid greybox prototyping, fail-fast mechanics testing, player analytics heatmaps, production pipeline milestone gates, and post-release support.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.


<a id="domain-131-05"></a>
## Category: Game foundations

<a id="catalog-131-r05"></a>
### Rules, state and feedback

Subcategory `CATALOG-131-R05` · foundation.

<a id="bank-131-030"></a>
#### BANK-131-030 — What makes a playable prototype different from a collection of game assets?

**Individual coverage scope:** Build one action, rule, state change and feedback loop before adding art or content volume.

<a id="bank-131-031"></a>
#### BANK-131-031 — How does a game remember whether a door is open, locked or destroyed?

**Individual coverage scope:** Compare state machines, saved state and transitions in a small engine-independent example.

<a id="bank-131-032"></a>
#### BANK-131-032 — Why does frame rate change the behavior of some poorly designed games?

**Individual coverage scope:** Separate rendering, simulation steps and input timing; demonstrate a reproducible movement test.

<a id="bank-131-033"></a>
#### BANK-131-033 — What does collision detection decide before physics response begins?

**Individual coverage scope:** Compare shapes, broad phase, contact and resolution using simple geometry.


<a id="domain-131-06"></a>
## Category: Game production

<a id="catalog-131-r06"></a>
### Worlds, content and networking

Subcategory `CATALOG-131-R06` · intermediate.

<a id="bank-131-034"></a>
#### BANK-131-034 — How can a level teach a mechanic before explaining it in text?

**Individual coverage scope:** Analyze sightlines, safe practice, feedback and increasing demands in an original sample level.

<a id="bank-131-035"></a>
#### BANK-131-035 — Why does pathfinding fail when a map changes during play?

**Individual coverage scope:** Compare navigation graphs, dynamic obstacles, replanning and agent size.

<a id="bank-131-036"></a>
#### BANK-131-036 — What makes multiplayer movement look smooth despite network delay?

**Individual coverage scope:** Explain prediction, interpolation, reconciliation and tradeoffs without recommending exploit techniques.

<a id="bank-131-037"></a>
#### BANK-131-037 — How does procedural generation produce variety without making every level random noise?

**Individual coverage scope:** Compare constraints, seeds, structure and playability checks in a bounded generator.


<a id="domain-131-07"></a>
## Category: Game evaluation

<a id="catalog-131-r07"></a>
### Accessibility and release

Subcategory `CATALOG-131-R07` · advanced.

<a id="bank-131-038"></a>
#### BANK-131-038 — How can playtests distinguish a confusing rule from an unresponsive control?

**Individual coverage scope:** Define observation tasks, consent, input logs and interview limits rather than relying on completion time alone.

<a id="bank-131-039"></a>
#### BANK-131-039 — Why is a game's save format part of its long-term maintenance burden?

**Individual coverage scope:** Trace versioning, migrations, corruption handling and compatibility using fictional saved data.

<a id="bank-131-040"></a>
#### BANK-131-040 — What makes an accessibility option change the game system rather than just its interface?

**Individual coverage scope:** Compare remapping, timing, readability, feedback and alternatives while retaining explicit design goals.

<a id="bank-131-041"></a>
#### BANK-131-041 — How should a small game team decide what to cut before release?

**Individual coverage scope:** Map dependencies, player value, defects, production cost and scope limits in a sample backlog.

<a id="bank-131-042"></a>
#### BANK-131-042 — How can a monetization system be evaluated without treating engagement as player welfare?

**Individual coverage scope:** Compare transparency, spending controls, incentives and vulnerable players; avoid revenue-maximizing manipulation advice.

<a id="catalog-131-r08"></a>
### Finding frame-time bottlenecks

Subcategory `CATALOG-131-R08` · advanced.

<a id="bank-131-043"></a>
#### BANK-131-043 — Why can a game report a high average frame rate while still producing noticeable stutters?

**Individual coverage scope:** Compare frame-time distributions, CPU work, GPU work, asset loading, shader compilation and capture overhead in one reproducible scene; distinguish a bottleneck measurement from a guessed optimization.

<a id="bank-131-044"></a>
#### BANK-131-044 — When does an Unreal Engine 5.8 Nanite mesh still need a fallback representation?

**Individual coverage scope:** Use Epic's versioned Nanite documentation to compare rendered virtualized detail with collision, ray tracing and stereo-VR support; specify asset type, renderer and hardware instead of asserting that polygon budgets disappeared.

**Research follow-up:** [Bounded case and source-access note](RESEARCH_NOTES/BANK-131-044.md). This does not change proposal or production status.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

### pending_topics/0 — The Core Gameplay Loop: How 30 Seconds of Fun Built Halo and Mario

**Original question:** How did Bungie's '30 seconds of fun repeated thousands of times' philosophy create the greatest console shooter in history?

**Original planning scope:** The Golden Triangle of Halo (guns, grenades, melee), Nintendo's jump curve physics, action-feedback loops, and player retention.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-010](#bank-131-010).

### pending_topics/1 — The Game Loop and Delta Time: The Code That Powers Every Game

**Original question:** What happens under the hood when a game processes user input, updates physics, and renders pixels 60 times a second?

**Original planning scope:** ProcessInput -> Update -> Render, variable vs fixed time-steps, delta time (dt) frame rate independence, and preventing physics explosions at high FPS.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-011](#bank-131-011).

### pending_topics/2 — Juice It or Lose It: The Art of Screenshake, Particles, and Game Feel

**Original question:** How does adding 3 frames of hit-stop, a 5-pixel screen rumble, and white flash turn a boring square into a satisfying weapon?

**Original planning scope:** Jan Willem Nijman's Vlambeer design principles, freeze frames, sound design layering, squash-and-stretch animation, and micro-satisfactions.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-012](#bank-131-012).

### pending_topics/3 — Collision Detection: How Computers Know When Two Virtual Objects Touch

**Original question:** How do physics engines detect bullet hits without lagging the CPU using Axis-Aligned Bounding Boxes and SAT?

**Original planning scope:** AABB broad-phase pruning, Separating Axis Theorem (SAT) for convex polygons, spatial hashing, raycasting, and tunneling bullet glitches.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-013](#bank-131-013).

### pending_topics/4 — The Psychology of Flow in Games: Pacing, Difficulty Curves, and Frustration

**Original question:** How do games like Dark Souls and Celeste keep players in the sweet spot between boring ease and rage-quitting despair?

**Original planning scope:** Mihaly Csikszentmihalyi's flow channel, dynamic difficulty adjustment (Resident Evil 4), failure feedback framing, and player mastery loops.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-014](#bank-131-014).

### pending_topics/5 — Level Design Architecture: Leading the Player's Eye Without Breadcrumbs

**Original question:** How does Valve's Half-Life 2 guide players through complex city ruins using light contrast, architectural silhouettes, and weenies?

**Original planning scope:** Walt Disney's 'weenie' visual landmarks, contrasting light pools, architectural lines pointing to goals, pinch points, and psychological affordances.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-015](#bank-131-015).

### pending_topics/6 — Shader Programming: The Math of Painting Light on Polygonal Surfaces

**Original question:** How do vertex and fragment shaders calculate specular shine, metallic roughness, and water ripples on GPU cores?

**Original planning scope:** Graphics pipeline (rasterization), Phong vs PBR (Physically Based Rendering) lighting models, normal mapping optical illusions, and HLSL code.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-016](#bank-131-016).

### pending_topics/7 — Procedural Generation: How Spelunky and Minecraft Build Infinite Worlds

**Original question:** How do algorithms generate unique, beatable dungeons and continental mountain ranges from a single numerical seed?

**Original planning scope:** Perlin and Simplex noise, Derek Yu's Spelunky room-template grid algorithm, cellular automata cave generation, and guaranteeing level solvability.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-017](#bank-131-017).

### pending_topics/8 — Finite State Machines vs Behavior Trees: Programming Game AI

**Original question:** Why did Halo 2 abandon basic state machines (Patrol, Alert, Attack) for modular behavior trees?

**Original planning scope:** FSM spaghetti code breakdown, behavior tree Composites (Selectors/Sequences), decorators, blackboard memory, and reactive enemy coordination.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-018](#bank-131-018).

### pending_topics/9 — Multiplayer Netcode: Client-Side Prediction, Reconciliation, and Rollback

**Original question:** How do online shooters and fighting games (GGPO) eliminate lag when player signals take 80ms to cross continents?

**Original planning scope:** Deterministic lockstep vs client prediction, server reconciliation rubberbanding, lag compensation rewind, and fighting game rollback mechanics.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-019](#bank-131-019).

### pending_topics/10 — The Immersive Sim: Looking Glass Studios and Emergent Gameplay

**Original question:** How did System Shock and Deus Ex invent games where player curiosity and physical simulation break developer expectations?

**Original planning scope:** Warren Spector's rules of immersion, systemic consistency (if it looks flammable, it must burn), player agency, and emergent problem solving.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-020](#bank-131-020).

### pending_topics/11 — A* Pathfinding: How Game Characters Navigate Massive Game Maps in Milliseconds

**Original question:** How do hundreds of RTS units find the shortest route through a winding maze without bringing the CPU to a screeching halt?

**Original planning scope:** Dijkstra's algorithm, heuristic distance functions (Manhattan/Euclidean), priority queues, navigation meshes (NavMesh), and funnelling path smoothing.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-021](#bank-131-021).

### pending_topics/12 — The Tragedy of Development Hell: Why Duke Nukem Forever and Daikatana Failed

**Original question:** How do brilliant game directors trap multi-million dollar projects in 14-year development nightmares?

**Original planning scope:** Feature creep, engine-switching traps (Quake II to Unreal to Unreal 2), lack of vertical slice discipline, perfectionism, and sunk cost fallacy.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-022](#bank-131-022).

### pending_topics/13 — Data-Oriented Design (ECS): Squeezing 100,000 Entities on Screen

**Original question:** Why does traditional Object-Oriented Programming (OOP) choke modern CPU caches, and how does Entity Component System fix it?

**Original planning scope:** L1/L2 CPU cache lines, cache misses, array-of-structures vs structure-of-arrays, Unity DOTS, and mass parallel data processing.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-023](#bank-131-023).

### pending_topics/14 — Predatory Monetization: The Dark Psychology of Gacha, Loot Boxes, and Battle Passes

**Original question:** How do mobile gaming algorithms deploy Skinner Box operant conditioning and variable reward schedules to hunt 'whales'?

**Original planning scope:** B.F. Skinner variable ratio rewards, FOMO artificial urgency, loss aversion, anchoring premium currencies, and European gambling regulatory crackdowns.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-024](#bank-131-024).

### pending_topics/15 — Interactive Audio: Dynamic Music Systems and Vertical Layering in Video Games

**Original question:** How does the soundtrack of Red Dead Redemption 2 seamlessly add percussion when combat starts and fade to violin when you win?

**Original planning scope:** Vertical layering (stems fading based on game state parameters), horizontal re-sequencing (metric-boundary transitions), Wwise and FMOD middleware.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-025](#bank-131-025).

### pending_topics/16 — The Solo Indie Phenomenon: How Stardew Valley and Undertale Made Millions

**Original question:** How did Eric Barone spend 4.5 years working 12-hour days in total isolation to create a $100M agricultural empire alone?

**Original planning scope:** Full-stack solo discipline (art, code, music, design), scope management, community goodwill marketing, and surviving extreme isolation.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-026](#bank-131-026).

### pending_topics/17 — Procedural Animation and Ragdoll Physics: The Euphoria Engine Behind GTA

**Original question:** Why do pedestrians in Grand Theft Auto IV realistically stumble down stairs and reach for handrails instead of playing canned death animations?

**Original planning scope:** NaturalMotion Euphoria engine, active biomechanical ragdolls, self-balancing PID controllers, muscle actuation, and procedural collision responses.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-027](#bank-131-027).

### pending_topics/18 — Unreal Engine 5: Nanite, Lumen, and the Disappearance of Polygon Budgets

**Original question:** How does Nanite render billions of micro-polygons directly from film-quality ZBrush sculpts without baking normal maps?

**Original planning scope:** Virtualized cluster geometry, continuous Level of Detail (LOD) down to 1 pixel, Lumen software/hardware ray-traced global illumination, and VRAM bandwidth.

**Editorial disposition:** routed. Existing Nanite scope. Epic's versioned documents describe supported uses and fallback meshes; polygon and performance constraints have not disappeared.

**Scoped proposals:** [BANK-131-028](#bank-131-028).

### pending_topics/19 — The Master Game Design Architecture: From Prototype to Commercial Masterpiece

**Original question:** What comprehensive production framework unites greybox prototyping, vertical slices, playtesting telemetry, and post-launch liveops?

**Original planning scope:** Rapid greybox prototyping, fail-fast mechanics testing, player analytics heatmaps, production pipeline milestone gates, and post-release support.

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-029](#bank-131-029).

### trending_topics/0 — The '30 Seconds of Fun' Rule: How Halo's Secret Design Formula Changed Gaming

**Editorial disposition:** routed. Duplicate Halo loop pitch; a slogan is not evidence of a universal design formula or a ranking of games.

**Scoped proposals:** [BANK-131-010](#bank-131-010).

### trending_topics/1 — Juice It or Lose It: The Simple Tricks That Make Indie Games Feel Amazing

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-012](#bank-131-012).

### trending_topics/2 — How One Man Spent 4.5 Years Alone in His Bedroom Building Stardew Valley

**Editorial disposition:** routed. Existing Stardew Valley creator scope; exact solitary hours, earnings and causes require developer or filed records.

**Scoped proposals:** [BANK-131-026](#bank-131-026).

### trending_topics/3 — Why GTA IV's Ragdoll Physics Still Look Better Than GTA V (Euphoria Engine)

**Editorial disposition:** routed. Existing Euphoria procedural-animation scope; 'better than GTA V' needs a defined shot comparison.

**Scoped proposals:** [BANK-131-027](#bank-131-027).

### trending_topics/4 — How Spelunky's Room Generation Algorithm Solved Infinite Random Dungeons

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-017](#bank-131-017), [BANK-131-037](#bank-131-037).

### trending_topics/5 — Rollback Netcode Explained: The Mathematics That Saved Fighting Games

**Editorial disposition:** routed. Existing network prediction and rollback scopes; do not claim physical latency was eliminated or that one algorithm saved all fighting games.

**Scoped proposals:** [BANK-131-019](#bank-131-019), [BANK-131-036](#bank-131-036).

### trending_topics/6 — The 14-Year Disaster of Duke Nukem Forever: The Ultimate Development Hell

**Editorial disposition:** routed. Existing imported BANK question covers the mechanism or case; quoted performance, earnings and causal claims need primary production records.

**Scoped proposals:** [BANK-131-022](#bank-131-022).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-131-01"></a>
### Game systems

<a id="bank-131-001"></a>
- `BANK-131-001` — Game loops and state machines → [BANK-131-031](#bank-131-031)
<a id="bank-131-002"></a>
- `BANK-131-002` — Collision detection → [BANK-131-033](#bank-131-033)
<a id="bank-131-003"></a>
- `BANK-131-003` — Entity-component architecture → [BANK-131-023](#bank-131-023)

<a id="catalog-131-02"></a>
### Design

<a id="bank-131-004"></a>
- `BANK-131-004` — Feedback loops and player learning → [BANK-131-034](#bank-131-034)
<a id="bank-131-005"></a>
- `BANK-131-005` — Difficulty curves → [BANK-131-014](#bank-131-014)
<a id="bank-131-006"></a>
- `BANK-131-006` — Level readability → [BANK-131-034](#bank-131-034)

<a id="catalog-131-03"></a>
### Production

<a id="bank-131-007"></a>
- `BANK-131-007` — Save-system versioning → [BANK-131-039](#bank-131-039)
<a id="bank-131-008"></a>
- `BANK-131-008` — Performance profiling → [BANK-131-043](#bank-131-043)
<a id="bank-131-009"></a>
- `BANK-131-009` — Accessible control remapping → [BANK-131-040](#bank-131-040)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [025 Gaming Stories / Lore](../025_gaming_stories_lore/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [132 Retro Gaming](../132_retro_gaming/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [133 Board Games & Tabletop](../133_board_games_tabletop/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [134 Chess](../134_chess/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

## Editorial coverage review

Question scopes, source concepts and documented gaps reviewed.


## Coverage remaining open

- **Case and source readiness:** Epic's versioned Nanite documentation bounds one rendering-versus-fallback question; see RESEARCH_NOTES/BANK-131-044.md. Archived game comparisons, creator income, performance figures and employment claims require primary records. Game engine rendering stays here; VR hardware experience belongs in niche 128. No idea was approved.
- **Reviewed starter branches and primary-home boundaries:** All original starter concepts now have explicit individual-scope targets. See the starter crosswalk below and Scripts/editorial_review_002_184.json for scope evidence and semantic pair decisions; follow the primary-home referrals after consolidation.
- **Regional and participant variation:** Compare less-visible regions, languages, participants and contrary cases within this niche; record substantive distinctions before adding another proposal.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/131_game_development/NICHE_131_game_development.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
