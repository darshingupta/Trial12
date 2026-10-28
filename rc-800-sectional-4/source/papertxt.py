from common import PASSAGES, numbered, L
qs=numbered(); out=[]
for p in PASSAGES:
    out.append(f"\n===== {p['label'].upper()} ({p['kind']}) =====\n")
    for i,t in enumerate(p['text'],1): out.append(f"[{i}] {t}\n")
    for q in [x for x in qs if x['passage']==p['id']]:
        out.append(f"\nQ{q['n']}. {q['stem']}")
        for i,o in enumerate(q['placed']): out.append(f"  ({L[i]}) {o[1]}")
open('paper.txt','w').write("\n".join(out))
