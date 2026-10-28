import json, base64
from common import PASSAGES, numbered, L
from codes import CODES
qs=numbered()
def split_stem(stem):
    parts=stem.split("\n")
    if len(parts)==1: return dict(stem=stem)
    if len(parts)==2: return dict(stem=parts[0], quote=parts[1])
    return dict(stem=parts[0], quote=parts[1], after=parts[2])
data=dict(codes=CODES, passages=[])
rev=dict(key=[],traps=[],why=[],reasons=[],src=[],type=[])
for p in PASSAGES:
    pp=dict(id=p['id'],label=p['label'],kind=p['kind'],text=p['text'],qs=[])
    for q in [x for x in qs if x['passage']==p['id']]:
        d=split_stem(q['stem']); d['o']=[o[1] for o in q['placed']]
        pp['qs'].append(d)
        rev['key'].append(q['target'])
        rev['traps'].append({L[i]:(o[0] if o[0]!="K" else None) for i,o in enumerate(q['placed'])})
        rev['reasons'].append({L[i]:o[2] for i,o in enumerate(q['placed'])})
        rev['why'].append(q['why']); rev['src'].append(q['src']); rev['type'].append(q['type'])
    data['passages'].append(pp)
raw=json.dumps(rev,ensure_ascii=False).encode('utf-8'); k="rc800-sectional-4"
enc=bytes(b^((ord(k[i%len(k)])+i*7)%256) for i,b in enumerate(raw))
seal=base64.b64encode(enc).decode()
html=open('template.html').read().replace("__DATA__",json.dumps(data,ensure_ascii=False)).replace("__SEAL__",seal)
open('../rc_800_sectional_4.html','w').write(html)
print(len(html),"bytes")
