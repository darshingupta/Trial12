from p3 import *
FIN=[2,3,4,5,6,7,8,10,11,12,13,14,15]
A=run(FIN); print('n',len(A)); [print(show(a),'\n') for a in A]
def diag(a,x,y): px,py=pos(a,x),pos(a,y); return px[0]==py[0]+1 and px[1]!=py[1]
for o in [('Juhi','Chess'),('Prisha','Tennis'),('Squash','Prisha'),('Chess','Ruhi')]:
    print('Q1',o,[(pos(a,o[0]),pos(a,o[1]),diag(a,*o)) for a in A])
I=len({a['Lalit'][0] for a in A})==1
II=len({sport_of(a,person_at(a,(pos(a,'Chess')[0]-1,pos(a,'Chess')[1]))) for a in A})==1
III=len({person_at(a,(pos(a,'Kabaddi')[0]+1,pos(a,'Kabaddi')[1])) for a in A})==1
print('Q2',I,II,III)
B=[a for a in A if a['Kabaddi']=='Lalit']; print('Q3 cases',len(B))
q3={'a':lambda a: a['Hockey']=='Prisha','b':lambda a: above(a,'Ishaan','Prisha'),'c':lambda a: above(a,'Kabaddi','Meher'),
    'd':lambda a: any(v[0]==flr(a,'Polo') for v in vacant(a))}
print('Q3',{k:[f(a) for a in B] for k,f in q3.items()})
print('Q4',sum(len({(a[p],sport_of(a,p)) for a in A})==1 for p in PEOPLE))
q5={'a':lambda a: a['Lalit'][1]==a['Ishaan'][1],'b':lambda a: a['Lalit'][0]%2==0 and a['Ishaan'][0]%2==0,
    'c':lambda a: above(a,'Kabaddi','Polo'),'d':lambda a: flr(a,'Hockey')<flr(a,'Chess')}
print('Q5',{k:[f(a) for a in A] for k,f in q5.items()})
