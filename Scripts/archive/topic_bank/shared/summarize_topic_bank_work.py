from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

"""Build cross-niche reconciliation, open-coverage and changed-file reading indexes."""
from collections import Counter
import subprocess

from manage_all_topic_banks import ROOT, TOPICS, rows, home, read, write, records, save_bytes, table


def main():
    entries=[];files=[];stages=Counter()
    totals=Counter()
    for nid,row in rows().items():
        directory=home(nid);b=read(directory/'IN_DEPTH_TOPIC_BANK.json')
        rs=records(b);rec=b.get('local_reconciliation')
        stages[b.get('integration_stage','reconciled_niche_001')]+=1
        totals['active_proposals']+=len(rs)
        totals['parent_categories']+=len(b['parent_categories'])
        totals['subcategories']+=len(b['categories'])
        initial=b.get('prior_initial_map',{})
        starter=[t for c in initial.get('categories',[]) for t in c['topics']]
        mapped=b.get('starter_concept_crosswalk',{})
        unmapped=[t for t in starter if t['id'] not in mapped]
        if rec:
            imported={t for t in rec['source_records']} if rec['source_kind']!='subject_map' else set()
            reused=sum(t.get('origin')=='repository_roadmap' for c,t in rs)
            new=sum(t['id'] not in imported and t.get('origin')!='repository_roadmap' for c,t in rs)
            totals['new_authored_active_proposals_this_pass']+=new
            totals['reconciled_specific_local_proposals']+=reused
            totals['archived_generic_local_frameworks']+=len(b.get('archived_local_frameworks',[]))
            totals['retired_duplicate_local_proposals']+=len(b.get('retired_duplicate_proposals',[]))
            controlled=['IN_DEPTH_TOPIC_BANK.json','IN_DEPTH_TOPIC_BANK.md','TOPIC_BANK_RECONCILIATION.md','topics_status.json','TOPICS_COVERED_REPORT.md']
            controlled += [name for name in rec['local_files'] if name.endswith('_CHANNEL_TOPIC_ROADMAP.md')]
            for name in controlled:
                files.append({'path':(directory/name).relative_to(ROOT).as_posix(),'niche_id':nid,
                    'change':'modified' if name in rec['local_files'] else 'new'})
        entries.append({'niche_id':nid,'title':row['title'],'directory':directory.name,
            'main_reading_file':f'{directory.name}/IN_DEPTH_TOPIC_BANK.md','active_proposals':len(rs),
            'starter_concepts':len(starter),'explicit_starter_coverage_links':len(mapped),
            'unmapped_starter_checklist':[{'id':t['id'],'title':t.get('title',t['question'])} for t in unmapped],
            'open_coverage':b.get('open_coverage',[]),'stage':b.get('integration_stage','reconciled_niche_001')})
    new_scripts=subprocess.check_output(['git','ls-files','--others','--exclude-standard','Scripts'],cwd=ROOT,text=True).splitlines()
    for path in new_scripts:
        if path not in {'Scripts/integrate_ayurveda_topics.py','Scripts/manage_ai_topics.py'}:
            files.append({'path':path,'change':'new','role':'catalog authoring, reconciliation or validation support'})
    shared=[('README.md','modified'),('topics/README.md','modified'),('topics/ALL_NICHE_TOPIC_BANKS.md','new'),
        ('topics/TOPIC_BANK_PROGRESS.json','new'),('topics/TOPIC_BANK_GUIDE.md','new'),
        ('topics/TOPIC_BANK_VALIDATION.json','new'),('topics/TOPIC_BANK_SOURCE_PRESERVATION.json','new'),
        ('topics/ALL_NICHE_RECONCILIATION_REPORT.md','new'),('topics/TOPIC_BANK_OPEN_COVERAGE.md','new'),
        ('topics/TOPIC_BANK_CHANGED_FILES.json','new')]
    files += [{'path':path,'change':kind,'role':'shared discovery, status or verification'} for path,kind in shared]
    write(TOPICS/'TOPIC_BANK_CHANGED_FILES.json',{'scope':'This pass:002–550 and shared discovery/support;001 catalog retained from preceding work.',
        'file_count':len(files),'files':sorted(files,key=lambda x:x['path'])})
    gaps=['# Topic-bank coverage and review queues','',
        '[All-niche index](ALL_NICHE_TOPIC_BANKS.md) · [Reconciliation report](ALL_NICHE_RECONCILIATION_REPORT.md)','',
        'All banks remain proposal drafts. Explicit starter links are editorial cross-references, not verified facts or a measure of total subject completeness. An unmapped starter concept is a review item; it may already be addressed in a broader active scope. Read the actual question and scope before adding another episode. Do not generate a duplicate just to fill a mapping cell.','',
        '| Niche | Active BANK proposals | Starter concepts | Explicit links | Unmapped checklist items | Main reading file |',
        '|---|---:|---:|---:|---:|---|']
    for e in entries:
        gaps.append(f"| {e['niche_id']} {table(e['title'])} | {e['active_proposals']} | {e['starter_concepts']} | {e['explicit_starter_coverage_links']} | {len(e['unmapped_starter_checklist'])} | [Read]({e['main_reading_file']}) |")
    gaps += ['','## Per-niche remaining coverage','']
    for e in entries:
        if not e['open_coverage'] and not e['unmapped_starter_checklist']:continue
        gaps += [f"### {e['niche_id']} {e['title']}",'',f"[Main bank]({e['main_reading_file']})",'']
        for g in e['open_coverage']:
            gaps.append('- '+(f"**{g['area']}:** {g['next_step']}" if isinstance(g,dict) else str(g)))
        if e['unmapped_starter_checklist']:
            gaps += ['- **Starter mapping review:** '+ '; '.join(f"`{t['id']}` {t['title']}" for t in e['unmapped_starter_checklist'])+'.']
        gaps.append('')
    gaps += ['## Cross-cutting open work','',
        '- Choose exact cases, versions, places, populations, editions and dates where the proposal requires them.',
        '- Continue regional, linguistic, chronological and participant depth only when it creates a distinct question.',
        '- Compare neighboring niches and keep one primary home for the same episode.',
        '- Source discovery, factual verification, source rights, registered-angle scope review, idea readiness, scripts, media and publication remain separate work.','']
    save_bytes(TOPICS/'TOPIC_BANK_OPEN_COVERAGE.md','\n'.join(gaps).encode('utf-8'))
    validation=read(TOPICS/'TOPIC_BANK_VALIDATION.json') if (TOPICS/'TOPIC_BANK_VALIDATION.json').exists() else {}
    preservation=read(TOPICS/'TOPIC_BANK_SOURCE_PRESERVATION.json') if (TOPICS/'TOPIC_BANK_SOURCE_PRESERVATION.json').exists() else {}
    report=['# All-niche topic-bank reconciliation report','',
        '[Read the 550-bank index](ALL_NICHE_TOPIC_BANKS.md) · [Open coverage](TOPIC_BANK_OPEN_COVERAGE.md) · [Maintenance guide](TOPIC_BANK_GUIDE.md) · [Changed-file manifest](TOPIC_BANK_CHANGED_FILES.json)','',
        'Scope: reconcile and expand 001–550 while preserving both the supplied bundle and existing local work. The subsequent scope-based editorial pass is documented in [the editorial review](TOPIC_BANK_EDITORIAL_REVIEW.md); selected later source work is tracked in [follow-up progress](TOPIC_BANK_FOLLOW_UP_PROGRESS.md). Files were written into the existing topics structure; no GitHub push, production project or publication approval was created.','',
        '| Metric | Count |','|---|---:|',f"| Niches with banks | {len(entries)} |",
        f"| Active BANK proposals across 550 | {totals['active_proposals']} |",
        f"| New authored active proposals in 002–550 | {totals['new_authored_active_proposals_this_pass']} |",
        f"| Specific local roadmap proposals reconciled into active BANK records | {totals['reconciled_specific_local_proposals']} |",
        f"| Archived generic local framework records | {totals['archived_generic_local_frameworks']} |",
        f"| Retired local duplicate records, IDs reserved | {totals['retired_duplicate_local_proposals']} |",
        f"| Original ZIP records checked/preserved | {preservation.get('original_records_preserved','Check pending')} |",
        f"| Files in this pass's change manifest | {len(files)} |",'',
        'Counts follow authored coverage; they are not quotas or completeness thresholds. Archived source starters, retired frameworks, queue references and template franchise combinations are not added again to active proposal counts.','',
        '## How the documents connect','',
        'Repository README → all-niche bank index → one main IN_DEPTH_TOPIC_BANK.md per niche → editable JSON, reconciliation, original execution report and registry planning references. Existing roadmap paths remain entry points. Status files keep their original values and add a separate catalog namespace.','',
        'The extensive Ayurveda roadmap body and all original production-report bodies are preserved. Existing CAT Q1–Q42, registered angles, DEPTH plans, CONFIG snapshots, research ledgers and episode production files remain unchanged. The three original niche 001 ideas remain preserved; one linked researching idea was added during follow-up. Banks propose topics; they do not automatically create ready ideas or episodes.','',
        '## Reconciliation and quality decisions','',
        '- Verified ZIP members against the supplied SHA256 manifest and extracted copies before selective import. Neither broad all-niche patch was applied.',
        '- Preserved all imported detailed questions, IDs, scopes and original fields. Same-episode overlaps found in editorial review may be inactive full records with primary-question referrals. Starter maps remain exactly archived, with their original subject headings visible as a coverage checklist.',
        '- Identified repeated local angle templates and kept their wording/allocated IDs inactive. Specific local proposals were retained with source attribution and no claim that their premises were verified.',
        '- Added individually scoped questions, grouped into subject categories and subcategories with explicit learning paths. No topic-by-angle multiplication or botanical franchise multiplication was used as new authored coverage.',
        '- Compared new proposals against existing coverage and removed semantic rewordings found during review. Exact cross-niche collisions are checked globally; a duplicate receives one primary home and a referral, with its old ID reserved.',
        '- Saved per-niche gap notes and source-concept crosswalks. The open-coverage report distinguishes mapping review from demonstrated missing subject coverage.','',
        '## Validation results','',
        f"- Latest structural snapshot: {validation.get('niches_checked','pending')} niches; {len(validation.get('errors',[]))} errors; {len(validation.get('exact_cross_niche_duplicate_questions',{}))} exact cross-niche question collisions; {validation.get('local_links_checked','pending')} local links checked.",
        f"- Independent ZIP comparison: {preservation.get('niches_checked','pending')} niches; {preservation.get('original_records_preserved','pending')} source records preserved; {len(preservation.get('errors',[]))} errors.",
        '- Existing five depth-planning tests pass. Python compilation and negative checks reject duplicate IDs/questions, changed original scopes, changed local status, bad counts and prerequisite cycles.',
        '- Repository-wide validation now passes after the Ayurveda identity/output renderers were reconciled with the existing 281 links; the Ayurveda pages and roadmap were preserved.',
        '- Structural or lexical checks do not prove semantic uniqueness, exhaustive scholarship or factual support. Selected source checks are documented separately in the follow-up progress record; the proposal catalog as a whole is not fact-verified.','',
        '## Current preparation stages','']
    report += [f'- `{stage}`: {count}' for stage,count in sorted(stages.items())]
    report += ['','## Remaining work','',
        'Use [the coverage report](TOPIC_BANK_OPEN_COVERAGE.md) for each niche’s explicit open branches and mapping-review items. Further case, regional, language and evidence work remains open without a numerical topic cap.','',
        'To reproduce checks, run Scripts/manage_all_topic_banks.py check and Scripts/validate_topic_bank_sources.py. To refresh the reading indexes after intentional JSON changes, run the targeted renderer, index command and this summary script.','']
    save_bytes(TOPICS/'ALL_NICHE_RECONCILIATION_REPORT.md','\n'.join(report).encode('utf-8'))
    print(f'Summarized {len(entries)} niches, {totals["active_proposals"]} active proposals and {len(files)} changed files; all coverage remains open to substantive additions.')


if __name__=='__main__':main()
