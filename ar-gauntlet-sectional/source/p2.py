# concentric circles: slot=(c,i) c=0 inner facing out, c=1 outer facing in
P=['Kabir','Leela','Mohan','Naina','Omkar','Pari','Qadir','Rhea','Sahil','Tara','Uday','Vani']
SLOTS=[(c,i) for c in (0,1) for i in range(6)]
class S:
    def __init__(s,a): s.a=a; s.inv={v:k for k,v in a.items()}
    def R(s,x,k):
        c,i=s.a[x]; return s.inv[(c,(i+k)%6 if c==0 else (i-k)%6)]
    def L(s,x,k): return s.R(x,-k)
    def F(s,x): c,i=s.a[x]; return s.inv[(1-c,i)]
    def inner(s,x): return s.a[x][0]==0
    def gap(s,x,y):  # people between along each arc, same circle only
        (c1,i1),(c2,i2)=s.a[x],s.a[y]
        if c1!=c2: return None
        d=(i2-i1)%6; return {d-1,6-d-1}
def solve(clues, order=None):
    """clues: list of (scope_names, fn(S)->bool). backtracking assignment."""
    order=order or P
    sols=[]; a={}
    used=set()
    def check():
        st=S(a)
        for scope,fn in clues:
            if all(n in a for n in scope):
                try:
                    if not fn(st): return False
                except KeyError: pass  # refers to slot unassigned; treat as unknown
        return True
    def rec(k):
        if k==len(order):
            st=S(dict(a))
            if all(fn(st) for _,fn in clues): sols.append(dict(a))
            return
        x=order[k]
        doms=[(0,0),(1,0)] if k==0 else SLOTS
        for sl in doms:
            if sl in used: continue
            a[x]=sl; used.add(sl)
            if check(): rec(k+1)
            del a[x]; used.discard(sl)
    rec(0)
    return sols
def show(a):
    inv={v:k for k,v in a.items()}
    return 'IN:'+' '.join(inv[(0,i)][:2] for i in range(6))+' | OUT:'+' '.join(inv[(1,i)][:2] for i in range(6))
