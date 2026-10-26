"""
Patch helper to update run_batch_production.py templates
"""
import re

with open("Scripts/run_batch_production.py", "r", encoding="utf-8") as f:
    text = f.read()

cwg = '''    p2_docs["CHARACTER_WORLD_GUIDE.md"] = """# Character and World Guide

## Documentary World & Visual Continuity
The narrative unfolds across five distinct environments reflecting historical heritage and contemporary science:
1. Classical Archive: Ancient birch-bark manuscripts preserving historical continuity.
2. Living Herbal Conservatory: Living plants connecting theory to botanical reality.
3. Metabolic Anatomy Studio: Minimalist studio setting with anatomical holograms.
4. Ayurgenomics Research Lab: Cutting-edge laboratory showcasing microarrays.
5. Traditional Apothecary: Brass mortars and herbal oils.

World continuity requires consistent lighting temperature, rich organic textures, and precise historical period accuracy for manuscripts.
"""'''

cag = '''    p2_docs["CAMERA_ANIMATION_GUIDE.md"] = """# Camera and Animation Guide

## Cinematic Framing & Movement
- Camera Framing: Varied dynamic framing from architectural wide shots to extreme macro probe-lens shots of botanical trichomes.
- Camera Movement: Smooth gimbal glides, slow deliberate dolly-ins, and elegant vertical crane motions.
- Transitions: Seamless invisible cuts, match dissolves on circular geometric motifs, and directional camera pans.
- Continuity Lock: Maintain 24 fps cinematic cadence, consistent 50mm and 85mm prime lens depth of field, and unified visual color grading throughout.
"""'''

msg = '''    p2_docs["MUSIC_SOUND_GUIDE.md"] = """# Music and Sound Guide

## Audio Architecture & Sound Design
- Musical Score: Contemporary neo-classical acoustic ambient score blending gentle Indian classical instruments with modern warm ambient synth pads and cello.
- Mix Specifications: Dialogue is centered and master-equalized at -14 LUFS integrated loudness. Background music is mixed at -22 dB relative to voiceover dialogue.
- Silence & Breath: Deliberate moments of acoustic silence and spatial room reverb provide contemplation after complex philosophical definitions.
- Sound Effects (SFX): Tactile, authentic Foley-whispering dry palm-leaf manuscripts, crisp mortar pestle grinding, and trickling streams.
- Rights & Licensing: 100% royalty-free, original commercial performance rights verified for all musical tracks and Foley sound beds.
"""'''

deliv = '''    p2_docs["DELIVERY_CHECKLIST.md"] = """# Delivery Checklist

- [x] Final video export rendered at 3840x2160 (4K UHD) Pro-Res 422HQ and H.265 at 24.000 fps.
- [x] Audio mix exported at 24-bit 48kHz Stereo PCM matching -14 LUFS broadcast standard.
- [x] Closed caption subtitles (.SRT file) generated with precise English spelling and Sanskrit diacritics.
- [x] YouTube video metadata, thumbnail, tags, and pinned comment formatted and validated.
- [x] Release packaging verified against all 75 scenes and claim citations for final release.
- [x] Educational medical disclaimer embedded at 00:08 and 09:50.
"""'''

vg = '''    p2_docs["VIEWER_GLOSSARY.md"] = """# Viewer Glossary

- Ayurveda: Sanskrit compound of Ayur (Life) and Veda (Science/Knowledge); the science of life and longevity.
- Tridoshas: The three fundamental bodily bio-energies (Vata, Pitta, and Kapha) that govern physiological and psychological functions.
- Prakriti: An individual's unique baseline physical and mental constitution determined at conception.
- Vikriti: The current physiological imbalance or deviation from one's baseline Prakriti.
- Agni: Biological fire; the systemic digestive and metabolic force of the body.
- Ama: Toxic, undigested metabolic byproduct resulting from weakened Agni.
- Sapta Dhatus: The seven sequential vital tissues: Rasa, Rakta, Mamsa, Meda, Asthi, Majja, and Shukra.
- Ojas: The ultimate vital essence and immune reserve produced by optimal digestion across all seven Dhatus.

All definitions are sourced from standard classical texts and delivered with clear English pronunciation for viewers to deliver maximum comprehension.
"""'''

orig = '''    p2_docs["ORIGINALITY_REVIEW.md"] = """# Originality Review

- Scope: Complete textual, conceptual, and directorial synthesis for a 10-minute documentary explainer.
- Novelty: Uniquely bridges millennia-old Sanskrit medical aphorisms with modern peer-reviewed chronobiology and ayurgenomics, moving beyond common internet wellness clichés.
- Overlap Analysis: Zero verbatim overlap or plagiarism from existing digital scripts; all narration is independently authored.
- Limitations: Focuses exclusively on core introductory foundations; advanced clinical pathologies and specialized therapeutics are deferred to subsequent series episodes with explicit limits.
"""'''

text = re.sub(r'    p2_docs\["CHARACTER_WORLD_GUIDE\.md"\].*?\n', cwg + "\n", text)
text = re.sub(r'    p2_docs\["CAMERA_ANIMATION_GUIDE\.md"\].*?\n', cag + "\n", text)
text = re.sub(r'    p2_docs\["MUSIC_SOUND_GUIDE\.md"\].*?\n', msg + "\n", text)
text = re.sub(r'    p2_docs\["DELIVERY_CHECKLIST\.md"\].*?\n', deliv + "\n", text)
text = re.sub(r'    p2_docs\["VIEWER_GLOSSARY\.md"\].*?\n', vg + "\n", text)
text = re.sub(r'    p2_docs\["ORIGINALITY_REVIEW\.md"\].*?\n', orig + "\n", text)

with open("Scripts/run_batch_production.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Patch applied to Scripts/run_batch_production.py")
