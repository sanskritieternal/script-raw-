# Google Veo Guidelines: Maharana Pratap

**Project:** Maharana Pratap Historical Documentary
**Style:** Ultra Realistic Historical Documentary

---

## Technical Constraints

- **Maximum scene length:** 8 seconds (hard limit, no exceptions)
- **One scene = one primary action**
- **One scene = one main location**
- **One scene = one camera movement**
- **Maximum three important characters per scene**
- **Natural physics, natural lighting, natural human motion**
- **Simple readable composition**
- **No visual clutter, no overcrowded frames**
- **No impossible camera motion**
- **No random character spawning**
- **No unexplained visual changes**

---

## Character Count Rules

**Rule: Maximum 3 important characters per scene.**

This project's character breakdown:
- Scene types with 1 character: Pratap alone, Ajabde alone, Akbar alone, etc.
- Scene types with 2 characters: Pratap + Jhala Man, Pratap + Ajabde, Pratap + Bhamashah
- Scene types with 3 characters: Pratap + 2 commanders, Akbar + 2 advisors
- Scene types with many characters: Battle scenes, crowd scenes, royal courts

**For crowd/battle scenes:**
- Use wide shots — show the scale without showing individual faces
- Focus on 2-3 key characters in foreground
- Background figures are indistinct — no faces, no individual features
- Maximum 3 named/important characters with visible faces per scene

---

## Composition Rules

**Rule: Simple readable composition.**

- One primary subject per scene (usually Pratap)
- Clear focal point — eye naturally goes to main subject
- Background supports the story without competing
- No clutter in frame — empty space is powerful
- Rule of thirds for character placement
- Leading lines from architecture and terrain

**For Battle Scenes:**
- Wide establishing shot first (scale)
- Then medium shots of key characters
- Close-ups only for emotional moments
- Never more than 3 faces visible at once

**For Court/Palace Scenes:**
- Pratap at center or slightly off-center
- One advisor/relative in frame
- Background figures blurred or out of focus

---

## Camera Movement Rules

**Allowed movements:**
- Slow push forward (emotional intensity)
- Slow pull back (reveal scale)
- Slow pan left/right (survey landscape)
- Slow tilt up/down (show architecture)
- Tracking shot (follow character movement)
- Static composition (contemplative scenes)

**Prohibited movements:**
- Fast whip pans (unrealistic for documentary)
- Orbiting shots (distracting)
- Dutch angles (not appropriate for this style)
- Impossible camera positions (floating, through walls)
- Rapid cuts between shots (not applicable to single 8-second scene)

---

## Lighting Rules

**Natural lighting only — no artificial effects:**
- Golden hour (sunrise/sunset) for emotional scenes
- Harsh midday sun for battle/confrontation scenes
- Moonlight/night: cool blue, firelight as accent
- Interior scenes: firelight, torchlight, candles
- No neon, no electric light, no modern lighting
- Volumetric lighting for dramatic moments (dust, smoke, haze)

---

## Safety Replacements for This Historical Period

**Required modifications for AI generation:**

1. **No Hindi/Devanagari text on screen** — the negative prompt handles this
2. **No Islamic calligraphy on Mughal elements** — use abstract patterns instead
3. **No religious symbols that could be misinterpreted** — temple symbols are fine, but avoid modern reinterpretations
4. **No graphic violence** — battle wounds implied, not explicit
5. **No self-immolation (jauhar) shown directly** — implied through composition
6. **No controversial political symbols** — keep banners and flags historical
7. **Traditional weapons only** — no modern-looking firearms
8. **Period-appropriate architecture** — no modern buildings, no architectural anachronisms
9. **Natural skin tones** — avoid AI's tendency toward unnaturally smooth or light skin
10. **Realistic animal behavior** — horses don't float, elephants don't fly

---

## Prompt Structure (Google Veo Format)

Every video prompt must follow this structure (under 1200 characters):

```
[Main Subject] + [Action] + [Emotion] + [Environment] + [Lighting] + [Camera Movement] + [Visual Style] + [Master Suffix]
Negative: [Master Negative Prompt + Veo Negative Prompt]
Duration: 8 seconds
```

**Example:**
```
Maharana Pratap sitting on Chetak at Haldighati pass, looking toward enemy army with determined resolve, Aravalli mountains behind, golden sunrise light, slow cinematic push forward, ultra realistic historical documentary, authentic 16th century Rajput warrior appearance, ultra realistic historical documentary, authentic architecture, realistic fabrics, natural skin texture, cinematic lighting, physically accurate proportions, highly detailed, documentary film quality, historically grounded, natural environmental storytelling, photorealistic materials, authentic historical atmosphere
Negative: No subtitles, no captions, no text overlay, no titles, no watermark, no logo, no Hindi text on screen, no cinematic typography, no UI elements, no credits, no banners, no floating letters, no symbols, no modern objects, no distortion, no low quality artifacts, no blurry output, no noise, no grainy texture, anime, cartoon, fantasy, magic, plastic skin, science fiction, modern buildings, modern roads, modern vehicles, electric lights, modern clothing, modern weapons, text, watermark, logo, duplicate people, extra fingers, extra limbs, bad anatomy, floating objects, video game graphics, oversaturated colors, low quality, blurry, artifacts, random objects, inconsistent costumes, inconsistent architecture
Duration: 8 seconds
```

---

## Veo Compliance Checklist (Per Scene)

- [ ] Scene is exactly 8 seconds
- [ ] Maximum 3 important characters with visible faces
- [ ] Background characters are indistinct
- [ ] Simple, readable composition
- [ ] One primary action
- [ ] One main location
- [ ] One camera movement
- [ ] Natural physics and lighting
- [ ] No visual clutter
- [ ] Negative prompt included
- [ ] Prompt under 1200 characters
- [ ] No modern objects
- [ ] No text/Hindi text on screen
