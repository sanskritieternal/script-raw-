# Phase 0: Configuration

Niche ID: 001
Niche: AI + Technology Explainers
Story question: How does the original Transformer combine token relationships, and where does the attention analogy stop?
Episode slug: original_transformer_attention
Subject category: Robotics_AI
Niche identity: `REGISTRY/Niches/001_ai_technology_explainers/NICHE_001_ai_technology_explainers.md`
CAT preset: `REGISTRY/Niches/001_ai_technology_explainers/CAT_001_ai_technology_explainers.md`
Angle preset: `REGISTRY/Niches/001_ai_technology_explainers/Angles/001_ai_technology_explainers_how_it_works.md`
Question schema version: 5.0
Mode: autonomous
Production workflow version: 1.0

## Configuration answers

| ID | Question | Answer | Source |
|---|---|---|---|
| Q1 | Content Category | Robotics_AI | taxonomy |
| Q2 | Target Audience | General Public | niche_cat |
| Q3 | Primary Story Angle | From Input to AI Output | angle_preset |
| Q4 | Content Depth Level | Deep Analysis | niche_cat |
| Q5 | Visual/Media Priority | Heavy | niche_cat |
| Q6 | Interview/Documentation Segments | Quotes Only | niche_cat |
| Q7 | Content Sensitivity Level | Moderate | niche_cat |
| Q8 | Legal/Accuracy Concern | Moderate | niche_cat |
| Q9 | Subject Focus | Topic-Driven | niche_cat |
| Q10 | Contested Facts Included | Attributed research disagreement about attention as explanation; present both positions within their studied model scope | explicit_override |
| Q11 | Expertise Level Required | General knowledge | niche_cat |
| Q12 | Comparative Content | No comparisons | niche_cat |
| Q13 | Monetization Priority | Secondary | niche_cat |
| Q14 | Total Duration | 600 seconds | niche_cat |
| Q15 | Visual Style Primary | Futuristic Tech Editorial | niche_cat |
| Q16 | Voiceover Approach | Engaging Storytelling | niche_cat |
| Q17 | Delivery Format | Single video | niche_cat |
| Q18 | Primary Language | EN | niche_cat |
| Q19 | Additional Languages | None | niche_cat |
| Q20 | On-Screen Text Strategy | Precise editorial overlays for equations, labels and citations; generated footage supplies illustration only | explicit_override |
| Q21 | Graphics Requirement | Essential | niche_cat |
| Q22 | Ending Tone | Reflective/Thoughtful | niche_cat |
| Q23 | Accuracy Priority | Prioritize source-bounded accuracy and clearly labeled simplification for a general audience | explicit_override |
| Q24 | Source Quality Requirements | High | niche_cat |
| Q25 | Update Frequency | As-needed | niche_cat |
| Q26 | Platform Distribution | YouTube + Shorts/Reels | niche_cat |
| Q27 | Production Quality Level | Premium | niche_cat |
| Q28 | Audience Geographic Focus | Global | niche_cat |
| Q29 | Factual Verification Timeline | Standard (3-7 days) | niche_cat |
| Q30 | Expert/Access | No interviews | niche_cat |
| Q31 | Controversial Content Level | No controversial claims | niche_cat |
| Q32 | Comparative/Fairness Level | No comparisons | niche_cat |
| Q33 | Current Events Included | Historical only | niche_cat |
| Q34 | Bias Prevention Strategy | Acknowledge limitations, show multiple perspectives, cite sources | niche_cat |
| Q35 | Sponsored Content | No sponsorships | niche_cat |
| Q36 | Monetization Revenue Model | AdSense revenue | niche_cat |
| Q37 | Series/Playlist Strategy | Reading an AI claim; SER-001-001 episode 1; TOP-001-001 | explicit_override |
| Q38 | SEO Keyword Priority | Specific topic/subject names | niche_cat |
| Q39 | Content Warning/Disclaimer Needed | No warnings | niche_cat |
| Q40 | Video Generation Method | External AI-generated media with precise editorial overlays; user selects the generation tool | explicit_override |
| Q41 | Content Safety Level | Standard | niche_cat |
| Q42 | Scene Duration Strategy | FIXED 8-SECOND | niche_cat |

## Selected angle scope

**Focus / example question:** What happens between an AI input and its final output?

**Coverage:** Follow one defined task through data preparation, model inference, output handling, and human checks.

**Evidence to seek:** original system papers, model or dataset documentation, reproducible evaluations and attributed contributor accounts appropriate to the selected question

**Limits:** Name the system version, task and evaluation conditions; distinguish a demonstration from general capability and verify deployment claims separately.

Before Phase 1, narrow this guidance to a specific case, source or work, and the relevant place, population, version or period. Record that choice in the episode's story question and research summary.

This is the selected angle's planning guidance at project creation. Use the episode story question to choose the concrete case; document its coverage and exclusions in Phase 1.

## Phase 3 timing lock

- Exact runtime: 600 seconds
- Fixed scene duration: 8 seconds
- Planned scenes: 75; final scene: 8 seconds
- Scene batch size: 25

## Review gate

- Risk flags: None
- Human review required before publication: Yes
- Human review status: Pending
- Phase 1 claims require supporting sources before Phase 2.
- This configuration does not certify research, rendered assets, or publication readiness.


## Selected episode idea

Idea ID: IDEA-001-0001
Source idea bank: `REGISTRY/Niches/001_ai_technology_explainers/IDEA_BANK.json`
Idea snapshot SHA-256: d8d719ea4db2c0cabf082e294802f50ce3436a3e11a607d1f78317baefd26b63

```json
{
  "idea_id": "IDEA-001-0001",
  "niche_id": "001",
  "status": "ready_for_project",
  "angle_slug": "how_it_works",
  "topic": "Attention and sequence representation",
  "working_title": "What attention does in the original Transformer",
  "story_question": "How does the original Transformer combine token relationships, and where does the attention analogy stop?",
  "case": "The encoder-decoder architecture in the original Transformer paper",
  "place_period_version": "Historical research model, arXiv 1706.03762v7; not a current product specification",
  "intended_audience": "General adult viewers seeking source-based understanding",
  "purpose": "Build a limited conceptual model without treating attention as human understanding",
  "created_date": "2026-10-18",
  "updated_date": "2026-10-18",
  "evidence_gaps": [
    "Extract architecture passages and check an original illustrative token example."
  ],
  "blocking_gaps": [],
  "related_ideas": [],
  "readiness_note": "Source access and a bounded question support starting Phase 1. Evidence gaps below must be resolved before scripting; no claim or publication approval is asserted.",
  "source_candidates": [
    {
      "title": "Attention Is All You Need",
      "url": "https://arxiv.org/html/1706.03762v7",
      "status": "checked",
      "checked_date": "2026-10-18",
      "check_note": "Opened full HTML; inspected architecture, self-attention rationale and results headings."
    }
  ]
}
```

This is a creation-time snapshot, not a live link or research approval. Later bank edits do not rewrite this episode. Phase 1 still verifies each material claim.
