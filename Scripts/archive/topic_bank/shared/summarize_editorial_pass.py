from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

"""Readable results for the second, scope-based editorial pass."""
import json
from pathlib import Path
import manage_all_topic_banks as m

ROOT=Path(__file__).resolve().parents[4]


def main():
    validation=m.read(ROOT/'topics/TOPIC_BANK_EDITORIAL_VALIDATION.json')
    structure=m.read(ROOT/'topics/TOPIC_BANK_VALIDATION.json')
    preservation=m.read(ROOT/'topics/TOPIC_BANK_SOURCE_PRESERVATION.json')
    consolidation=m.read(ROOT/'Scripts/editorial_duplicate_consolidation.json')
    total=validation['totals']
    lines=['# Topic-bank editorial review','',
       '[Main bank index](ALL_NICHE_TOPIC_BANKS.md) · [Remaining case and evidence work](TOPIC_BANK_OPEN_COVERAGE.md) · [Recorded checks](TOPIC_BANK_EDITORIAL_VALIDATION.json)','',
       'This pass reviewed subject coverage, starter mappings, documented gaps and possible reworded overlaps. These remain topic proposals. No new source or factual claim was researched or verified.','',
       '| Result | Count |','|---|---:|',
       f"| Niches with saved per-bank review | {validation['banks_with_audit']} |",
       f"| Active proposals before this pass | {total['active_before']} |",
       f"| Newly added proposals still active | {total['new_active']} |",
       f"| Previously active proposals retired with preserved IDs | {total['retired_previous']} |",
       f"| Reviewed duplicate retirements in final consolidation | {len(consolidation['applied'])} |",
       f"| Active proposals after review | {total['active_after']} |",
       f"| Original starter subjects | {total['starter_subjects']} |",
       f"| Starter subjects without a coverage referral | {total['unmapped_starters']} |",
       f"| Original ZIP records preserved | {preservation['original_records_preserved']} |",'',
       '## What changed','',
       '- Added missing subject mechanisms and bounded cases where the prior scope did not cover them. Addition counts vary by the actual findings; no common quota was used.',
       '- Checked starter subjects against what each proposed video would actually cover. A nonempty but overly broad mapping was corrected or replaced with a specific question.',
       '- Reviewed two lexical candidate lists by question and scope. Related words were not treated as proof of duplication. Same-episode proposals were retired and referred to one primary question.',
       '- Preserved full retired records, original IDs and source subcategory metadata, including redundant imported originals. Archived wording remains traceable; inactive proposals do not inflate active counts.',
       '- Distinguished genuine missing subject coverage from cases, versions, dates, editions, languages, participant groups and source work needed to develop an existing proposal.',
       '- Kept recipe, season, regional illustration and short-form packaging variants as cases of an existing question when they did not create a distinct inquiry.','',
       '## Review evidence','',
       '- [001 and 281: direct scope, starter, gap and legacy decisions](../Scripts/editorial_review_root.json)',
       '- [002–184: per-bank review](../Scripts/editorial_review_002_184.json)',
       '- [185–367 except 281: per-bank review](../Scripts/editorial_review_185_367.json)',
       '- [368–550: per-bank review](../Scripts/editorial_review_368_550.json)',
       '- [Explicit duplicate consolidation](../Scripts/editorial_duplicate_consolidation.json)',
       '- [Reviewed duplicate decisions and distinct-scope boundaries](../Scripts/editorial_duplicate_decisions_final.json)',
       '- [Additional lexical candidate decisions after new proposals](../Scripts/editorial_final_semantic_decisions.json)',
       '- [Saved baseline of questions, scopes and gaps](../Scripts/editorial_review_inputs/before_editorial_pass.json)','',
       '## Validation and limits','',
       f"- Structural check: {structure['niches_checked']} banks, {len(structure['errors'])} errors, {len(structure['exact_cross_niche_duplicate_questions'])} exact question collisions, {structure['local_links_checked']} local links.",
       f"- Independent ZIP comparison: {preservation['niches_checked']} niches, {len(preservation['errors'])} errors.",
       f"- Editorial coverage/preservation check: {len(validation['errors'])} errors.",
       '- The repository-wide validator retains two existing Ayurveda identity/output findings; production and registry identity were not changed by this pass.',
       '- Scope review and similarity triage reduce repetition; they cannot mathematically prove that every semantic overlap has been found. The catalog has no fixed completeness threshold or final topic cap.',
       '- Exact case/source selection and factual verification remain separate work. Future documented mechanisms or overlooked perspectives may justify further additions. Nothing was pushed to GitHub.','',
       '## Per-niche changes','',
       '| Niche | Before | After | New active | Retired from baseline | Main file |',
       '|---|---:|---:|---:|---:|---|']
    for e in validation['banks']:
        nid=e['niche_id'];d=m.home(nid)
        lines.append(f"| {nid} | {e['before']} | {e['after']} | {len(e['added_active_ids'])} | {len(e['retired_before_ids'])} | [Read]({d.name}/IN_DEPTH_TOPIC_BANK.md) |")
    m.save_bytes(ROOT/'topics/TOPIC_BANK_EDITORIAL_REVIEW.md',('\n'.join(lines)+'\n').encode('utf-8'))
    changed=[]
    before=m.read(ROOT/'Scripts/editorial_review_inputs/before_editorial_pass.json')['banks']
    for nid,v in before.items():
        d=m.home(nid);p=d/'IN_DEPTH_TOPIC_BANK.json'
        if m.sha(p.read_bytes())!=v['sha256']:
            for name in ('IN_DEPTH_TOPIC_BANK.json','IN_DEPTH_TOPIC_BANK.md','topics_status.json','TOPICS_COVERED_REPORT.md','TOPIC_BANK_RECONCILIATION.md'):
                if (d/name).exists():changed.append((d/name).relative_to(ROOT).as_posix())
            b=m.read(p)
            changed += [(d/name).relative_to(ROOT).as_posix() for name in b.get('local_reconciliation',{}).get('local_files',{}) if name.endswith('_CHANNEL_TOPIC_ROADMAP.md')]
            if nid=='001':changed.append((d/'001_AI_TECHNOLOGY_EXPLAINERS_CHANNEL_TOPIC_ROADMAP.md').relative_to(ROOT).as_posix())
    m.write(ROOT/'topics/TOPIC_BANK_EDITORIAL_CHANGED_FILES.json',{'scope':'Second editorial pass; generated topic views plus supporting scripts and shared indexes/reports.',
        'niche_files':sorted(set(changed)),'shared_files':['topics/ALL_NICHE_TOPIC_BANKS.md','topics/TOPIC_BANK_PROGRESS.json','topics/README.md','topics/TOPIC_BANK_GUIDE.md','topics/TOPIC_BANK_OPEN_COVERAGE.md','topics/ALL_NICHE_RECONCILIATION_REPORT.md','topics/TOPIC_BANK_VALIDATION.json','topics/TOPIC_BANK_SOURCE_PRESERVATION.json','topics/TOPIC_BANK_EDITORIAL_VALIDATION.json','topics/TOPIC_BANK_EDITORIAL_REVIEW.md','topics/TOPIC_BANK_EDITORIAL_CHANGED_FILES.json'],
        'supporting_scripts':'See Scripts/editorial_* and the linked audit/consolidation files; Scripts/manage_ai_topics.py and Scripts/manage_all_topic_banks.py maintain the generated views.'})
    print(f"Saved editorial report for {validation['banks_with_audit']} niches; {total['active_after']} active proposals.")


if __name__=='__main__':main()
