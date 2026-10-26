# Selected source note ? BANK-549-050

Checked 2026-10-24. This is a named technical-format premise, not a promise of lossless cross-application transfer or an IDEA-readiness finding. New topic remains `proposed` with `verified_sources: []`.

## Primary project records

- Academy Software Foundation, OpenTimelineIO project README: https://github.com/AcademySoftwareFoundation/OpenTimelineIO . Describes editorial-cut order and duration, external media references, adapters and the explicit distinction from a media container. This is a living repository; cite release or commit for version-dependent statements.
- OpenTimelineIO documentation overview: https://github.com/AcademySoftwareFoundation/OpenTimelineIO/blob/main/docs/index.rst . Lists clips, timing, tracks, transitions, markers and metadata; audio/video is not embedded.
- OpenTimelineIO architecture guide: https://github.com/AcademySoftwareFoundation/OpenTimelineIO/blob/main/docs/tutorials/architecture.md . Describes timeline/track/clip structure and media-reference mechanisms; code examples are illustrative, not an interoperability guarantee.

## Bounded premise

OTIO is an API and interchange format for editorial timeline information. It can represent ordered clips and timing and may preserve richer metadata than a basic EDL. The media itself remains external. Translating a project into another application's format depends on adapters and tool support, and connecting referenced media depends on paths, linkers or site-specific conventions.

## Version, rights and operational limits

Open-source project documentation explains the data model but does not prove that a particular pair of applications round-trips effects, color, audio automation or every edit without loss. The README's supported-platform and adapter lists can change; choose a tagged release before citing compatibility. An OTIO file alone is not an archived film master or rights clearance; source media, plugins, fonts, music and license records may be needed. Avoid instruction that encourages unauthorized access or redistribution of protected assets. No performance or workflow-savings claim is established here.

## Semantic boundary

BANK-549-045 asks generally what an EDL preserves; this is OTIO's named interchange model and adapter boundary. 514 can cover open-source project stewardship; 127 VFX handoff and 369 documentary production are adjacent, but timeline interchange belongs to 549.
