import itertools
L=['B','D','F','G','J','K','S','V']
# tree: gf,gm couple; children c1,c2 each married to s1,s2; two grandchildren g1,g2 with parent couple index
def trees():
    out=[]
    for perm in itertools.permutations(L):
        gf,gm,c1,c2,s1,s2,g1,g2=perm
        if c1>c2 or g1>g2: continue  # symmetry
        for gc1 in 'MF':
            for gc2 in 'MF':
                for pidx in (0,1):
                    for gg1 in 'MF':
                        for gg2 in 'MF':
                            sex={gf:'M',gm:'F',c1:gc1,c2:gc2,s1:'F' if gc1=='M' else 'M',s2:'F' if gc2=='M' else 'M',g1:gg1,g2:gg2}
                            spouse={gf:gm,gm:gf,c1:s1,s1:c1,c2:s2,s2:c2}
                            parents={c1:(gf,gm),c2:(gf,gm)}
                            pc=(c1,s1) if pidx==0 else (c2,s2)
                            parents[g1]=pc; parents[g2]=pc
                            out.append({'sex':sex,'spouse':spouse,'parents':parents,'gen':{gf:1,gm:1,c1:2,c2:2,s1:2,s2:2,g1:3,g2:3}})
    return out
class T:
    def __init__(t,d): t.__dict__.update(d)
    def par(t,x): return t.parents.get(x,())
    def kids(t,x): return [c for c,p in t.parents.items() if x in p]
    def sib(t,x,y): return x!=y and t.par(x) and t.par(x)==t.par(y)
    def father(t,x,y): return x in t.par(y) and t.sex[x]=='M'
    def mother(t,x,y): return x in t.par(y) and t.sex[x]=='F'
    def parent(t,x,y): return x in t.par(y)
    def spouse_of(t,x): return t.spouse.get(x)
    def gp(t,x,y): return any(x in t.par(p) for p in t.par(y))
    def inlaw_parent(t,x,y): s=t.spouse_of(y); return s is not None and x in t.par(s)
    def sib_inlaw(t,x,y):
        s=t.spouse_of(y)
        if s and t.sib(x,s): return True
        sx=t.spouse_of(x)
        return sx is not None and t.sib(sx,y)
    def aunt_uncle(t,x,y):
        return any(t.sib(x,p) for p in t.par(y)) or any(t.spouse_of(x) is not None and t.sib(t.spouse_of(x),p) for p in t.par(y))
    def cousin(t,x,y): return any(t.sib(a,b) for a in t.par(x) for b in t.par(y))
