# Project Consistency Rules: Maharana Pratap

**Project:** Maharana Pratap Historical Documentary
**Visual Style:** Ultra Realistic Historical Documentary
**Tone:** Inspirational & Heroic
**Language:** Hindi

---

## Visual Style Lock

- Rendering: Ultra realistic, cinematic quality, photorealistic
- Medium: Live-action documentary aesthetic (not animated, not stylized)
- Lighting: Natural sunlight, golden hour, volumetric lighting for emotional scenes
- Color Palette: Warm earth tones, saffron accents, golden sunrise, cool mountain shadows
- Textures: Authentic fabric textures, weathered stone, natural skin texture, metallic armor
- Resolution: 8K quality, IMAX-compatible
- Platform Aesthetic: BBC Earth + National Geographic + Netflix Documentary hybrid

## Character Consistency Rules

- Never redesign any character's face after approval
- Never change body proportions, hairstyle, or beard style without story reason
- Only allowed changes: age progression, battle scars, natural wear, seasonal clothing, story-driven injuries
- Character names spelled exactly as in 01_Main_Characters.md and 02_Supporting_Characters.md
- Royal titles used consistently (Maharana, Rani, Rawat, Rao, Raja)
- Character consistency prompt must be appended to every image/video generation

## Location Consistency Rules

- Architecture, scale, layout must remain identical across all scenes
- Previously established locations maintain: lighting philosophy, architectural identity
- If a location changes due to war/siege/time, changes remain visible in later scenes
- Fort names: Chittorgarh, Kumbhalgarh, Udaipur, Gogunda, Chavand, Panthioli
- Aravalli mountain range: consistent geology, vegetation, color across all scenes

## Environment Memory Rules

- Weather and seasons tracked in MASTER_CONTEXT.md
- Time of day progression follows chronological story order
- Battle damage visible in subsequent scenes (e.g., Chittorgarh after siege)
- Seasonal clothing changes tracked

## Audio Consistency Rules

- Background music genre matches scene mood (see MASTER_CONTEXT.md)
- No modern instruments or sounds in any scene
- Ambient sounds appropriate to location and era

## Language Consistency

- All voiceover text in Hindi (Devanagari script)
- All production notes in English
- Character names and place names in their authentic form (Hindi transliteration)

## Historical Accuracy Rules

- All facts tagged with confidence score: VERIFIED/LIKELY/TRADITIONAL/LEGEND/DEBATED
- Never present debated history as absolute fact
- Include alternative viewpoints for controversial topics
- Modern historians' perspectives noted alongside traditional accounts

## Master Prompt Suffixes

Every AI image/video prompt must end with:
```
ultra realistic historical documentary, authentic architecture, realistic fabrics, natural skin texture, cinematic lighting, physically accurate proportions, highly detailed, documentary film quality, historically grounded, natural environmental storytelling, photorealistic materials, authentic historical atmosphere
```

## Master Negative Prompt

Every AI image/video prompt must include:
```
anime, cartoon, fantasy, magic, plastic skin, science fiction, modern buildings, modern roads, modern vehicles, electric lights, modern clothing, modern weapons, text, watermark, logo, duplicate people, extra fingers, extra limbs, bad anatomy, floating objects, video game graphics, oversaturated colors, low quality, blurry, artifacts, random objects, inconsistent costumes, inconsistent architecture
```

## Google Veo Negative Prompt

Every video generation prompt must include:
```
No subtitles, no captions, no text overlay, no titles, no watermark, no logo, no Hindi text on screen, no cinematic typography, no UI elements, no credits, no banners, no floating letters, no symbols, no modern objects, no distortion, no low quality artifacts, no blurry output, no noise, no grainy texture.
```
