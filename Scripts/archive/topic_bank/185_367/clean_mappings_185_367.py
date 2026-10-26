from pathlib import Path
p=(Path(__file__).resolve().parents[3] / 'manual_concepts_185_367.txt')
r={}
for line in p.read_text(encoding='utf-8-sig').splitlines():
 if not line:continue
 n,i,q=line.split('|');r[(n,i)]=q
r[('261','009')]='original carving from a later replacement'
# The existing question says: How do restorers distinguish original carving from a later replacement?
# Source261 is stone conservation; the wood-restoration question belongs262. Use stone-specific intervention record.
r[('261','009')]='cleaning a stone carving'
p.write_text('\n'.join('|'.join([n,i,q]) for (n,i),q in r.items())+'\n',encoding='utf-8')
