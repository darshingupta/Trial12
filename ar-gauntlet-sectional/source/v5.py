from p5seat import *
import pickle
TK=['T1','T2','T3']; SK=['S1','S2','S3','S4','S6','S7','S8','S11','S12','S14','S15']
A=run(TK,SK); print('n',len(A))
pickle.dump([(t.__dict__,p,f) for t,p,f in A],open('p5sols.pkl','wb'))
def kr(p,f,x,y):
    for k in range(1,8):
        if R(p,f,x,k)==y: return ('R',k)
        if Lf(p,f,x,k)==y: return ('L',k)
for t,p,f in A:
    print(showseat(t,p,f))
    print(' Q1',[kr(p,f,*o) for o in [('S','B'),('G','K'),('B','S'),('K','G')]])
fem=[x for x in L if all(t.sex[x]=='F' for t,_,_ in A)]; print('Q2 definitely female',fem)
def blood(t,x,y):  # share ancestor or ancestor/descendant
    def anc(z):
        out={z}; st=[z]
        while st:
            q=st.pop()
            for pp in t.par(q):
                if pp not in out: out.add(pp); st.append(pp)
        return out
    return bool(anc(x)&anc(y))
print('Q3',{x:[blood(t,x,'G') for t,_,_ in A] for x in ['D','V','B','J']})
for t,p,f in A:
    aunts=[x for x in L if t.aunt_uncle(x,'F') and t.sex[x]=='F']
    print(' Q4 aunts',aunts,[Lf(p,f,t.spouse_of(a),2) for a in aunts])
for t,p,f in A:
    sil=[x for x in L if t.inlaw_parent('G',x) and t.sex[x]=='M']
    I=all(R(p,f,x,2)=='G' for x in sil)
    gk=[x for x in L if t.gp('K',x)]; II=len({f[x] for x in gk})==1
    mil=[x for x in L if t.inlaw_parent(x,'V') and t.sex[x]=='F']
    III=any(between(p,'V',m)==1 for m in mil)
    print(' Q5',sil,I,gk,II,mil,III)
