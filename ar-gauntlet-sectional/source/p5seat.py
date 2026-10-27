from p5 import *
def find_role(t,pred):
    return [y for y in L if pred(y)]
SC={  # (needs_face, fn(t,pos,face))
 'S1': (True, lambda t,p,f: f[at(p,1)]!=f[at(p,8)]),
 'S2': (True, lambda t,p,f: sum(v=='N' for v in f.values())==4),
 'S3': (True, lambda t,p,f: (lambda x: x is not None and t.gp(x,'J') and t.sex[x]=='F')(Lf(p,f,'J',1))),
 'S4': (True, lambda t,p,f: (lambda x: x is not None and t.inlaw_parent('G',x) and t.sex[x]=='M')(R(p,f,'G',-0) if False else R(p,f,[y for y in L if y!='G'][0],0)) if False else any(t.inlaw_parent('G',x) and t.sex[x]=='M' and R(p,f,x,2)=='G' for x in L)),
 'S6': (False, lambda t,p,f: between(p,'D',t.spouse_of('D'))==3),
 'S7': (True, lambda t,p,f: p['F'] in (1,8) and any(t.gp(x,'F') and t.sex[x]=='M' and f[x]==f['F'] for x in L)),
 'S8': (True, lambda t,p,f: (lambda x: x is not None and t.gp('K',x))(R(p,f,'S',1))),
 'S9': (True, lambda t,p,f: (lambda x: x is not None and f[x]==f['K'])(R(p,f,'K',1))),
}
def seat(t, keys):
    res=[]
    pos_only=[SC[k][1] for k in keys if not SC[k][0]]
    with_face=[SC[k][1] for k in keys if SC[k][0]]
    for perm in itertools.permutations(range(1,9)):
        p=dict(zip(L,perm))
        if not all(fn(t,p,None) for fn in pos_only): continue
        for fb in range(256):
            f={x:('N' if fb>>i&1 else 'S') for i,x in enumerate(L)}
            if all(fn(t,p,f) for fn in with_face): res.append((p,f))
    return res
def showseat(t,p,f):
    return ' '.join(f"{at(p,i)}{f[at(p,i)]}" for i in range(1,9))
def run(tk,sk):
    out=[]
    for t in filt_trees(tk):
        for p,f in seat(t,sk): out.append((t,p,f))
    return out
if __name__=='__main__':
    tk=sys.argv[1].split(','); sk=sys.argv[2].split(',')
    out=run(tk,sk); print(len(out))
    for t,p,f in out[:12]:
        print(showseat(t,p,f), {x:t.sex[x]+str(t.gen[x]) for x in L}, 'Dpar',t.par('D'),'Fsex',t.sex['F'])
SC['S10']=(False, lambda t,p,f: all(abs(p[x]-p[t.spouse_of(x)])!=1 for x in L if t.spouse_of(x)))
SC['S11']=(True, lambda t,p,f: Lf(p,f,'J',3)=='V')
SC['S12']=(True, lambda t,p,f: R(p,f,'G',3)==t.spouse_of('G'))
SC['S13']=(False, lambda t,p,f: p['D'] in (1,8))
SC['S14']=(False, lambda t,p,f: t.gen[at(p,1)]==3)
SC['S15']=(True, lambda t,p,f: any(t.parent(x,'F') and t.sex[x]=='F' and f[x]==f['F'] for x in L))
