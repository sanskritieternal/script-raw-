# Handoff to external AI video generation

The user's workflow creates media in external AI tools such as Veo or Seedance. The repository prepares research, creative decisions, timed scenes, narration and generation instructions. No audiovisual pilot or media generation is required for the current depth-planning work.

## Use the existing production documents

This guide supplements the existing 32-document workflow. It is not a 33rd required output, a provider integration, an upload command or a change to CONFIG questions.

| Existing record | Handoff content |
|---|---|
| Character/world and visual/camera guides | Stable character descriptions, reference IDs, setting/period, palette, framing, movement and continuity constraints |
| Scene breakdown | Scene ID, exact intended duration, narrative purpose, visual action, narration, claim IDs and applicable asset references |
| AI prompt output | Scene-linked prompts, reference inputs, exclusions, intended first/last state and any split needed for the chosen generator |
| Music/sound and narration guides | Voice direction, pronunciation, pacing, ambience, music intent and whether audio will be generated separately |
| Asset register | Planned image/video/audio assets, provenance, generation settings when known, file/review status and rights notes |
| Delivery checklist and metadata | Target format, caption/transcript plan, language, chapters and publication fields appropriate to distribution |
| Review/revision log | Prompt or scene changes, factual/continuity issues, affected references and review evidence |

## Per-scene prompt checklist

- Identify the scene and the source-backed point it illustrates.
- Describe subject, setting, action, framing, movement, light and visual treatment.
- Reference character, costume, location and object continuity IDs where applicable.
- Specify the intended duration and start/end states. If a tool needs several clips, retain the parent scene ID and timing total.
- Separate visual instructions from narration and sound instructions. Avoid depending on generated lettering for exact charts, quotations or captions; plan precise overlays separately.
- Identify illustrations, reconstructions and fictional examples. AI imagery must not be described as archival footage, a measured result or documentary evidence.
- Record actual provider/model/version, relevant settings and reference inputs when generation occurs. Before adapting prompts, check the chosen tool's current supported inputs and timing limits; none are assumed here.

## Completion boundary

Planned assets can remain planned and their files need not exist for a text-package handoff. Do not label them created or reviewed until actual files and review evidence exist. The current compiler already supports this distinction.

A finished text package can be audited as text. Render quality, factual visual accuracy, pronunciation, continuity, synchronization, captions and final export quality are reviewed after the user generates media. Publication and required human-review gates still apply at the relevant stage; planning cannot certify unseen media.

## Selected generator and model profile

Keep the episode's selected generator/model/version, verification date and source for capability limits in CAMERA_ANIMATION_GUIDE.md. Selection may remain Pending at text-planning time. Separate creative preferences from verified technical limits. Record supported reference-image/video/audio inputs, aspect ratios, duration options, prompt controls and exclusions only after checking the chosen tool. No historical reference project's fixed limits apply automatically to Veo, Seedance or another tool.

## Reference package and prompt assembly

Link scene IDs to character profiles, approved/proposed appearance versions, location IDs, props/costumes and reference assets. Each prompt identifies subject, action, emotional intent, environment, lighting, framing/movement and selected visual treatment. Reference inputs must be actually attachable files when execution begins; planned sheets are not existing attachments. Adapt exclusions to provider support and preserve intended scene expressions/actions.

## Clip assembly and continuity review

If editorial scene duration exceeds a verified generation limit, assign child clip IDs with durations summing to the parent scene, explicit first/last states, continuity references and join/handle plan. Do not change Q14 or the approved editorial scene durations to fit a provider. Keep exact overlays and sound plans separate where appropriate. After external generation record takes/settings and review identity, costume, environment, motion, audio, continuity and provenance. Text planning does not require an audiovisual pilot or certify unseen media.
## Episode profile template

Use [GENERATOR_PROFILE_TEMPLATE.md](GENERATOR_PROFILE_TEMPLATE.md) as the structured source for an optional episode GENERATOR_PROFILE.md. `python -m Tools.projects.production_workflow prepare-planning "<episode>" --write` creates it only when missing. CAMERA_ANIMATION_GUIDE.md may summarize the selected tool and link the profile as the authoritative detailed record. Pending selection is valid at text-planning time; actual model capabilities must be checked before adaptation/execution. The profile is included in compilation when present; it does not change the 32 required production records.

