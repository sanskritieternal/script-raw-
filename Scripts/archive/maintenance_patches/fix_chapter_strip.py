"""
Patch helper to fix chapter stripping in run_batch_production.py
"""
with open("Scripts/run_batch_production.py", "r", encoding="utf-8") as f:
    text = f.read()

old_str = 'chapters = [\n        f"Foundations of {slug.replace(\'_\', \' \').title()[:30]}",'
new_str = 'chapters = [\n        f"Foundations of {slug.replace(\'_\', \' \').title()[:30]}".strip(),'

if old_str in text:
    text = text.replace(old_str, new_str)
    with open("Scripts/run_batch_production.py", "w", encoding="utf-8") as f:
        f.write(text)
    print("Fixed chapter whitespace successfully.")
else:
    print("Target string not found, check syntax.")
