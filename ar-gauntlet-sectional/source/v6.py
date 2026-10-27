from p6 import *
A=run(FINAL); assert len(A)==1; a=A[0]; print(show(a))
pos={b:a[b] for b in B}; wt={b:a['w'+b] for b in B}
for o in [('K','U','W'),('E','W','K'),('M','W','H'),('E','H','M')]:
    ps=[pos[x] for x in o]
    print('Q1',o,'first=sum',wt[o[0]]==wt[o[1]]+wt[o[2]], wt[o[0]],wt[o[1]]+wt[o[2]],'consec',max(ps)-min(ps)==2,'firstbetween',min(ps[1:])<ps[0]<max(ps[1:]))
u=[b for b in B if wt[b]==2*wt['W']][0]; ab=at(a,pos[u]+1); print('Q2',u,ab,sum(wt[b]>wt[ab] for b in B))
sw=dict(a); sw['M'],sw['U']=a['U'],a['M']
print('Q3 violated',[k for k in FINAL if not C[k][1](sw)])
top3=sum(wat(a,i) for i in (5,6,7)); bot3=sum(wat(a,i) for i in (1,2,3))
sq={9,16,25,36}
II=all(pos[x]>pos[y] for x in B if wt[x] in sq for y in B if wt[y] not in sq)
print('Q5',top3,bot3,top3>bot3,II,wat(a,4)==max(wt.values()))
