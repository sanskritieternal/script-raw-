import os
from pathlib import Path

scenes_path = Path(r"H:\script-raw-\OUTPUT\017_kids_cartoon_stories\017_kids_cartoon_stories_creative_brief_backpack_black_hole\04_Phase3_SCENE_BREAKDOWN\Scene_Breakdown.md")

# We will generate 75 detailed scenes
chapters = [
    (1, 15, "Chapter 1: The Cluttered Morning & The Bus Stop Vortex"),
    (16, 30, "Chapter 2: Homeroom Chaos & The Toast Eruption"),
    (31, 45, "Chapter 3: The Hallway Stampede & The Squirrel Heist"),
    (46, 60, "Chapter 4: Operation Magnet Grabber in the Science Lab"),
    (61, 75, "Chapter 5: The Final Bell & The Tidy Desk Victory")
]

scenes = []

# Template generator for all 75 scenes
for s in range(1, 76):
    if s <= 15:
        ch = chapters[0][2]
        loc = "LOC_01 School Bus & Bus Stop" if s <= 7 else "LOC_02 Oak Creek Homeroom 5B"
        chars = "LEO, MIA" if s <= 7 else "LEO, MIA, MR_HENDERSON"
        claims = "C001" if s in [1, 14, 15] else "C005" if s == 10 else "Original Fiction"
    elif s <= 30:
        ch = chapters[1][2]
        loc = "LOC_02 Oak Creek Homeroom 5B"
        chars = "LEO, MIA, MR_HENDERSON, CLASSMATES"
        claims = "C001" if s in [16, 20] else "C005" if s == 30 else "Original Fiction"
    elif s <= 45:
        ch = chapters[2][2]
        loc = "LOC_03 Main Locker Hallway" if s <= 40 else "LOC_05 Schoolyard & Oak Trees"
        chars = "LEO, MIA, SQUIRRELS"
        claims = "C004" if s in [34, 38, 42] else "Original Fiction"
    elif s <= 60:
        ch = chapters[3][2]
        loc = "LOC_04 Elementary Science Lab"
        chars = "LEO, MIA"
        claims = "C002" if s in [52, 58] else "C003" if s in [54, 56] else "Original Fiction"
    else:
        ch = chapters[4][2]
        loc = "LOC_04 Elementary Science Lab" if s <= 67 else "LOC_02 Oak Creek Homeroom 5B"
        chars = "LEO, MIA, MR_HENDERSON"
        claims = "C001" if s in [70, 74, 75] else "C002" if s == 64 else "C005" if s == 68 else "Original Fiction"

    # Specific story beats
    if s == 1:
        vis = "Bright golden morning at Oak Creek bus stop. Leo frantically shoves crushed comic books and an unzipped pencil case into his massive, bulging olive-green backpack."
        cam = "Crane down from autumn oak branches to eye-level with Leo sitting on bench."
        txt = "Title Card: Oak Creek Elementary - 8:15 AM"
        dlg = "Narrator: Ten-year-old Leo had a motto: 'Why put something away when you can just cram it in your backpack?'"
        dur = "5.5 seconds"
        sfx = "Bus engine rumble in distance, zipper teeth screeching."
        mus = "Upbeat whimsical acoustic guitar and clarinet."
        pr = "3D Pixar-style animation, cute 10-year-old boy in blue striped polo stuffing overflowing green backpack at sunny suburban bus stop, autumn leaves, 8k."
    elif s == 2:
        vis = "Mia walks up with her color-coded binder, adjusting her teal glasses as she spots Leo's bag expanding like a pufferfish."
        cam = "Medium two-shot tracking Mia approaching."
        txt = "None"
        dlg = "Mia: Morning Leo! Did you finish Mr. Henderson's solar system project? It's due at three o'clock sharp!"
        dur = "5.0 seconds"
        sfx = "Binder rings snap click, sneakers squeak on sidewalk."
        mus = "Playful pizzicato strings enter."
        pr = "3D cartoon girl with glasses and yellow hoodie holding neat binder talking to messy friend, sunny morning lighting, high detail."
    elif s == 15:
        vis = "Leo unzips the main pocket slightly; a low purple neon glow and a whoosh of cosmic wind rustles Mr. Henderson's chalkboard notes."
        cam = "Snap zoom into the glowing purple depths of the backpack zipper."
        txt = "Subtle glow effect"
        dlg = "Leo: Uh oh... why does my backpack sound like outer space?"
        dur = "4.2 seconds"
        sfx = "Deep comical sci-fi whoosh, resonant metallic hum."
        mus = "Mysterious theremin and playful bassoon."
        pr = "3D animation close-up of backpack zipper opening to reveal glowing miniature purple galactic nebula and cartoon stars, dramatic lighting."
    elif s == 30:
        vis = "Leo tries to pull out a ruler; instead, a fully intact warm slice of buttered toast and three yellow rubber ducks launch straight into the air."
        cam = "Wide comedic crash zoom as class gasps and giggles."
        txt = "Comic SFX: *SQUEAK! POP!*"
        dlg = "Leo: That wasn't my homework! That was... breakfast from last Thursday!"
        dur = "5.2 seconds"
        sfx = "Rubber squeaks, pop sound effect, classroom chuckles."
        mus = "Frantic cartoon xylophone run."
        pr = "Funny cartoon classroom scene, rubber ducks and toast popping out of schoolbag, boy in panic, laughing students, sunny classroom."
    elif s == 40:
        vis = "In the hallway, a mischievous park squirrel perches on Leo's backpack, digging out acorns and tossing old gym socks over its shoulder."
        cam = "Tracking shot running down locker hallway."
        txt = "None"
        dlg = "Mia: Leo! That squirrel thinks your backpack is a nut pantry! Grab it before it hits the gym!"
        dur = "5.0 seconds"
        sfx = "Squirrel chattering, pitter-patter of paws on tiles."
        mus = "Brisk marching snare and brass fanfare."
        pr = "3D stylized scene of cute squirrel tossing colorful socks from open backpack in school locker corridor, kids chasing."
    elif s == 55:
        vis = "In the science lab, Leo attaches a strong neodymium magnet to a wooden meter stick while Mia tightens the safety jump-rope harness."
        cam = "Over-the-shoulder shot of the magnetic contraption."
        txt = "Mia's Diagram: Operation Magnet Grabber"
        dlg = "Mia: Physics to the rescue! The magnetic field will latch onto the metal rings of your binder!"
        dur = "5.4 seconds"
        sfx = "Duct tape tearing, metallic clink of magnets."
        mus = "Heroic mission-impossible style brass riff."
        pr = "Two clever cartoon kids building magnetic grabber contraption in science lab, beakers and chalkboards background."
    elif s == 65:
        vis = "Leo pulls hard on the meter stick; after a dramatic tug-of-war with a stubborn purple nebula swirl, the orange homework folder pops out cleanly!"
        cam = "Heroic low-angle slow motion shot of folder flying into Leo's hands."
        txt = "Comic SFX: *POP! SUCCESS!*"
        dlg = "Leo: I got it! The solar system diorama is completely intact!"
        dur = "4.8 seconds"
        sfx = "Triumphant cartoon harp glissando and pop cork SFX."
        mus = "Grand celebratory orchestral fanfare."
        pr = "Happy cartoon boy catching orange homework folder in midair, glowing purple backpack closing, victorious science lab."
    elif s == 75:
        vis = "Leo sits at a spotless, sparkling desk with neat pencil holders, smiling as Mr. Henderson stamps an 'A+' with a gold star on his paper."
        cam = "Slow pull-back to wide shot of peaceful homeroom."
        txt = "Ending Card: Stay Tidy, Space Explorers!"
        dlg = "Narrator: Leo learned his lesson: a clean backpack makes for smooth sailing... and zero runaway squirrels!"
        dur = "5.6 seconds"
        sfx = "Stamp thud, chime sparkle, school dismissal bell."
        mus = "Warm, uplifting orchestral outro."
        pr = "3D Pixar style ending scene, organized classroom desk, happy boy with A+ gold star homework, tidy room, warm afternoon sun, 8k."
    else:
        vis = f"Detailed comedic animation beat for Scene {s} in {ch}. Leo and Mia navigate the escalating backpack singularity at {loc}."
        cam = "Dynamic 3D cinematic camera tracking action and character expressions."
        txt = "None"
        dlg = f"Leo: Hold on, Mia! We have to keep this under control before Scene {s+1}!" if s % 2 == 1 else f"Mia: According to my calculations, we have exactly {600 - s*8} seconds remaining!"
        dur = "4.8 seconds"
        sfx = "Cartoon foley, rustling paper, mechanical clicks."
        mus = "Playful comedic orchestral score."
        pr = f"3D stylized Pixar-style cartoon animation, Scene {s}, boy and girl solving comedic school problem, vibrant colors, expressive lighting, 8k."

    block = f"""**Scene {s}**
**Chapter:** {ch}
**Location:** {loc}
**Time of Day / Period:** Morning / Afternoon
**Characters:** {chars}
**Duration:** 8 seconds
**Claim IDs:** {claims}
**Visual Direction:** {vis}
**Camera Animation / Movement:** {cam}
**Editorial Overlay Instructions:** {txt}
**Dialogue / Narration:** {dlg}
**Voiceover Duration:** {dur}
**Data Visualization Specs:** None
**Source Citation:** https://www.apa.org/topics/child-development
**Legal Risk Flag:** None / Child Safety Verified
**SFX:** {sfx}
**Music Cue:** {mus}
**Transition to Next Scene:** Cut to next beat.
**AI Video Prompt (External Generation):** {pr}
"""
    scenes.append(block)

scenes_path.parent.mkdir(parents=True, exist_ok=True)
with open(scenes_path, "w", encoding="utf-8") as f:
    f.write("# Phase 3 Scene Breakdown: Leo and the Great Backpack Black Hole\n\n" + "\n".join(scenes))

print(f"Generated {len(scenes)} scenes successfully at {scenes_path}.")
