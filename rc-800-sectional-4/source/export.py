import json
from common import PASSAGES, numbered, L
from codes import CODES
qs=numbered(); out=dict(codes=CODES, passages=[])
for p in PASSAGES:
    pp=dict(id=p['id'],label=p['label'],kind=p['kind'],text=p['text'],qs=[])
    for q in [x for x in qs if x['passage']==p['id']]:
        parts=q['stem'].split("\n")
        pp['qs'].append(dict(n=q['n'],type=q['type'],stem=parts[0],quote=parts[1] if len(parts)>1 else None,after=parts[2] if len(parts)>2 else None,
            opts=[o[1] for o in q['placed']], codes=[o[0] for o in q['placed']], reasons=[o[2] for o in q['placed']],
            key=q['target'], why=q['why'], src=q['src']))
    out['passages'].append(pp)
json.dump(out,open('content.json','w'),ensure_ascii=False,indent=1)
print("ok")
