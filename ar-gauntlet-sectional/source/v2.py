from p2run import *
C[11]=(['Uday','Kabir','Sahil','Pari'], lambda s: (s.inner('Uday')!=s.inner('Kabir') or s.L('Kabir',1)!='Uday' and s.R('Kabir',1)!='Uday') and s.F('Sahil')!='Pari')
FIN=[1,3,4,6,7,8,10,11]
A=[S(a) for a in solve([C[k] for k in FIN])]
print("n",len(A))
def kr(s,x,y):
    for k in range(1,6):
        if s.R(x,k)==y: return k
# Q1
for o in [('Kabir','Tara','Qadir'),('Pari','Vani','Naina'),('Rhea','Mohan','Leela'),('Mohan','Rhea','Naina')]:
    print('Q1',o,[(s.F(o[0])==o[1], kr(s,o[1],o[2])) for s in A])
# Q2
print('Q2',[s.L(s.F(s.R('Pari',1)),2) for s in A])
# Q3
print('Q3',sum(all(s.a[p]==A[0].a[p] for s in A) for p in P))
# Q4
def gap1(s,x,y): g=s.gap(x,y); return g is not None and 1 in g
q4={'a':lambda s: s.F('Uday')=='Omkar','b':lambda s: s.F('Qadir')==s.R('Vani',1),
    'c':lambda s: s.L('Kabir',2)=='Sahil','d':lambda s: gap1(s,'Tara','Uday')}
print('Q4',{k:[f(s) for s in A] for k,f in q4.items()})
# Q5
def nextto(s,x,y): return s.inner(x)==s.inner(y) and (s.R(x,1)==y or s.L(x,1)==y)
q5={'a':lambda s: s.inner('Sahil')!=s.inner('Uday'),'b':lambda s: (not s.inner('Sahil')) or (not s.inner('Uday')),
    'c':lambda s: s.F('Uday')==s.L('Vani',1),'d':lambda s: not nextto(s,'Sahil','Tara') and not nextto(s,'Uday','Tara')}
print('Q5',{k:[f(s) for s in A] for k,f in q5.items()})
