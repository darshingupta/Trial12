from passages import PASSAGES
from questions import Q
L="abcd"
def placed(q):
    t=L.index(q['target']); ds=[o for o in q['opts'] if o[0]!="K"]; k=[o for o in q['opts'] if o[0]=="K"][0]
    out=[None]*4; out[t]=k; it=iter(ds)
    for i in range(4):
        if out[i] is None: out[i]=next(it)
    return out
def numbered():
    out=[]
    for n,q in enumerate(Q,1):
        d=dict(q); d['n']=n; d['placed']=placed(q); out.append(d)
    return out
