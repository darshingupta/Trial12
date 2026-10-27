from csp import solve
import sys
PEOPLE=['Ishaan','Juhi','Lalit','Meher','Nikhil','Ojas','Prisha','Ruhi']
SPORTS=['Polo','Squash','Tennis','Kabaddi','Rugby','Chess','Hockey','Archery']
FLATS=[(f,s) for f in range(1,6) for s in 'WE']
def flr(a,x): return a[a[x]][0] if x in SPORTS else a[x][0]
def pos(a,x): return a[a[x]] if x in SPORTS else a[x]
def side(a,x): return pos(a,x)[1]
def vacant(a):
    used={a[p] for p in PEOPLE}; return [fl for fl in FLATS if fl not in used]
def above(a,x,y): px,py=pos(a,x),pos(a,y); return px[1]==py[1] and px[0]==py[0]+1
def person_at(a,fl):
    for p in PEOPLE:
        if a[p]==fl: return p
def sport_of(a,p):
    for s in SPORTS:
        if a.get(s)==p: return s
VARS=PEOPLE+SPORTS
DOM={**{p:FLATS for p in PEOPLE},**{s:PEOPLE for s in SPORTS}}
AD=[PEOPLE,SPORTS]
P=PEOPLE
C={}
C[1]=(P, lambda a: len({v[0] for v in vacant(a)})==2 and all(v[0]!=1 for v in vacant(a)))
C[2]=(P+['Polo'], lambda a: above(a,'Lalit','Polo'))
C[3]=(P+['Archery'], lambda a: abs(flr(a,'Archery')-flr(a,'Prisha'))==2)
C[4]=(P+['Squash'], lambda a: side(a,'Squash')=='W' and all(v[0]!=flr(a,'Squash') for v in vacant(a)))
C[5]=(['Nikhil','Ruhi'], lambda a: above(a,'Ruhi','Nikhil') and a['Ruhi'][1]=='W')
C[6]=(['Meher','Ishaan'], lambda a: flr(a,'Meher')<flr(a,'Ishaan'))
C[7]=(P+['Tennis','Kabaddi'], lambda a: flr(a,'Tennis')==flr(a,'Kabaddi'))
C[8]=(P+['Chess','Kabaddi'], lambda a: side(a,'Chess')==side(a,'Kabaddi') and flr(a,'Chess')-flr(a,'Kabaddi')>=2)
C[9]=(P, lambda a: sum(a[p][1]=='W' for p in P)==4)
def c10(a):
    h=pos(a,'Hockey')
    if h[1]!='E': return False
    up=person_at(a,(h[0]+1,'E'))
    return up is not None and up not in (a['Tennis'],a['Squash'])
C[10]=(P+['Hockey','Tennis','Squash'], c10)
C[11]=(P+['Rugby','Tennis'], lambda a: flr(a,'Rugby')+1==flr(a,'Tennis'))
C[12]=(P, lambda a: all(flr(a,p)!=flr(a,'Juhi') for p in P if p!='Juhi'))
C[13]=(['Ojas','Juhi'], lambda a: above(a,'Juhi','Ojas'))
def run(keys, limit=None, extra=()):
    return solve(VARS,DOM,[C[k] for k in keys]+list(extra),AD,limit)
def show(a):
    rows=[]
    for f in range(5,0,-1):
        r=[]
        for s in 'WE':
            o=person_at(a,(f,s))
            r.append(f"{o}({sport_of(a,o)})" if o else '--vacant--')
        rows.append(f"F{f}: "+' | '.join(r))
    return '\n'.join(rows)
if __name__=='__main__':
    keys=[int(x) for x in sys.argv[1].split(',')]
    S=run(keys); print(len(S))
    for a in S[:6]: print(show(a)); print()
C[14]=(P, lambda a: (lambda v: abs(v[0][0]-v[1][0])==2)(vacant(a)))
C[15]=(['Juhi'], lambda a: a['Juhi'][1]=='W')
