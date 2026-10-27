from fam import *
import itertools, sys, pickle, os
def R(pos,face,x,k):  # person k places to x's right, or None
    p=pos[x]+(k if face[x]=='N' else -k)
    for n,q in pos.items():
        if q==p: return n
    return None
def Lf(pos,face,x,k): return R(pos,face,x,-k)
def between(pos,x,y): return abs(pos[x]-pos[y])-1
def at(pos,i):
    for n,q in pos.items():
        if q==i: return n
TC={
 'T1': lambda t: sum(t.inlaw_parent('K',y) for y in L)==2 and t.sex['K']=='F',
 'T2': lambda t: t.sib('J','F') and t.sex['J']=='F',
 'T3': lambda t: t.aunt_uncle('S','J') and t.sex['S']=='F',
 'T4': lambda t: not t.kids('B'),
 'T5': lambda t: t.gp('G','F') and t.sex['G']=='M',
}
def filt_trees(keys):
    ts=[T(d) for d in trees()]
    return [t for t in ts if all(TC[k](t) for k in keys)]
if __name__=='__main__':
    ks=sys.argv[1].split(',')
    ts=filt_trees(ks); print(len(ts))
    for t in ts[:10]:
        print({x:(t.sex[x],t.gen[x],t.spouse_of(x),t.par(x)) for x in L})
