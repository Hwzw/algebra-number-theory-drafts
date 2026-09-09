#!/usr/bin/env python3
"""Verify the five selected artifacts against their audit records.

This checks artifact identity and recorded checks, not mathematical truth.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'selected_papers'
REVIEWS = {
    'P01-lefschetz-classification': 'P01-extension-independent-review.md',
    'P02-recurrence-repair': 'P02-final-manuscript-review.md',
    'P06-stirling-repair': 'P06-final-manuscript-review.md',
    'P09-unique-addition': 'P09-final-manuscript-review.md',
    'P13-nilperiod-rings': 'P13-final-manuscript-review.md',
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

records = []
assert {p.name for p in BASE.glob('P[0-9][0-9]-*') if p.is_dir()} == set(REVIEWS)
conversion_manifest = json.loads((BASE / 'markdown-conversion-manifest.json').read_text())
assert conversion_manifest['paper_count'] == 5
manifest_records = {r['paper']: r for r in conversion_manifest['papers']}
for name, review_name in REVIEWS.items():
    folder = BASE / name
    hashes = {ext: sha(folder / ('manuscript.' + ext)) for ext in ('tex', 'pdf', 'md')}
    qa = json.loads((folder / 'qa/report.json').read_text())
    conversion = json.loads((folder / 'markdown-conversion.json').read_text())
    math = json.loads((folder / 'markdown-math-check.json').read_text())
    assert qa['tex_sha256'] == conversion['source_tex_sha256'] == hashes['tex'], name
    assert qa['pdf_sha256'] == conversion['source_pdf_sha256'] == hashes['pdf'], name
    assert conversion['markdown_sha256'] == hashes['md'], name
    assert qa['rendered'] and qa['visually_reviewed'], name
    assert conversion['roundtrip_content_equal'] and not conversion['warnings'], name
    assert not math['errors'] and math['expressions'] == conversion['markdown_math_expressions'], name
    assert math['markdown_sha256'] == hashes['md'], name
    for key in ('source_tex_sha256', 'source_pdf_sha256', 'markdown_sha256'):
        assert manifest_records[name][key] == conversion[key], (name, key)
    review = ROOT / 'reassessment' / review_name
    assert hashes['tex'] in review.read_text(), (name, 'review does not cover current source')
    assert (folder / 'ASSESSMENT.md').is_file(), name
    log_path = folder / 'manuscript.log'
    if log_path.exists():
        log = log_path.read_text()
        assert not re.search(r'(^!|undefined references|Overfull \\hbox|Overfull \\vbox)', log, re.M | re.I), name
    md = (folder / 'manuscript.md').read_text()
    assert not re.search(r'\\(?:cite|ref|eqref|label)\{', md), name
    records.append({
        'paper': name,
        'files': {f'manuscript.{ext}': digest for ext, digest in hashes.items()},
        'pages': qa['pages'],
        'proof_bodies_preserved': conversion['environments'].get('proof', 0),
        'source_math_expressions_preserved': conversion['source_math_expressions_verified'],
        'markdown_math_expressions_checked': math['expressions'],
        'full_markdown_roundtrip_pass': True,
        'pdf_all_pages_visually_inspected': True,
        'local_build_log_checked': log_path.exists(),
        'final_review': str(review.relative_to(ROOT)),
        'final_review_sha256': sha(review),
        'assessment_sha256': sha(folder / 'ASSESSMENT.md'),
        'human_expert_review': False,
        'github_live_visual_render_inspected': False,
    })
result = {
    'collection': 'Five selected research manuscripts',
    'status': 'Complete manuscripts; internally reviewed AI research, not human peer reviewed',
    'paper_count': len(records),
    'total_pages': sum(r['pages'] for r in records),
    'total_proof_bodies': sum(r['proof_bodies_preserved'] for r in records),
    'total_markdown_math_expressions': sum(r['markdown_math_expressions_checked'] for r in records),
    'mathematical_truth_or_novelty_certified_by_this_script': False,
    'records': records,
}
(BASE / 'manifest.json').write_text(json.dumps(result, indent=2) + '\n')
print(f"PASS: {len(records)} manuscripts; {result['total_pages']} PDF pages; "
      f"{result['total_proof_bodies']} proof bodies; "
      f"{result['total_markdown_math_expressions']} Markdown formulas.")
