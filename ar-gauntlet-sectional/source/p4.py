from csp import solve
import sys
P=['Tanay','Urvi','Vihaan','Waseem','Xenia','Yash','Zoya','Sana']
MONTHS=['Feb','Apr','May','Jul','Sep','Nov']; DAYS={'Feb':28,'Apr':30,'May':31,'Jul':31,'Sep':30,'Nov':30}
SLOTS=[(m,d) for m in range(6) for d in (8,23)]
MODE=['m_'+p for p in P]
VARS=P+MODE
DOM={**{p:SLOTS for p in P},**{m:['On','Off'] for m in MODE}}
def idx(s): return s[0]*2+(0 if s[1]==8 else 1)
def order(a): return sorted(P,key=lambda p: idx(a[p]))
def nbetween(a,x,y):
    i,j=sorted((idx(a[x]),idx(a[y]))); return sum(1 for p in P if i<idx(a[p])<j)
def mon(a,p): return MONTHS[a[p][0]]
C={}
C[1]=(P, lambda a: sum(DAYS[mon(a,p)]==31 for p in P)==2)
C[2]=(P, lambda a: sorted([sum(a[p][0]==m for p in P) for m in range(6)])==[1,1,1,1,2,2])
C[3]=(['Sana','Zoya'], lambda a: nbetween(a,'Sana','Zoya')==2 if all(q in a for q in P) else True)
C[4]=(['Tanay','Yash'], lambda a: a['Tanay'][0]==a['Yash'][0]+1)
C[5]=(P, lambda a: order(a)[-1]=='Waseem')
C[6]=(['Xenia','Vihaan'], lambda a: a['Xenia'][0]==a['Vihaan'][0] and a['Xenia'][1]<a['Vihaan'][1])
C[7]=(['Urvi'], lambda a: DAYS[mon(a,'Urvi')]<30)
C[8]=(VARS, lambda a: all(a['m_'+x]!=a['m_'+y] for x,y in zip(order(a),order(a)[1:])))
C[9]=(VARS, lambda a: a['m_'+order(a)[0]]=='On')
# fix C3 scope: needs all P
C[3]=(P, lambda a: nbetween(a,'Sana','Zoya')==2)
def run(keys,limit=None,extra=()):
    return solve(VARS,DOM,[C[k] for k in keys]+list(extra),[P],limit)
def show(a):
    out=[]
    for s in SLOTS:
        o=[p for p in P if a[p]==s]
        out.append(f"{MONTHS[s[0]]}{s[1]}:{(o[0]+'/'+a['m_'+o[0]]) if o else '-'}")
    return ' '.join(out)
if __name__=='__main__':
    keys=[int(x) for x in sys.argv[1].split(',')]
    S=run(keys); print(len(S))
    for a in S[:12]: print(show(a))
def empties(a): used={a[p] for p in P}; return [s for s in SLOTS if s not in used]
C[10]=(['Tanay'], lambda a: a['Tanay'][1]==23)
C[11]=(P, lambda a: sum(idx(e)<idx(a['Tanay']) for e in empties(a))==sum(idx(e)>idx(a['Zoya']) for e in empties(a)))
C[12]=(P, lambda a: sum(a[p][0]==a['Urvi'][0] for p in P)==1)
def c4cal(a):
    m={'Feb':2,'Apr':4,'May':5,'Jul':7,'Sep':9,'Nov':11}
    return m[mon(a,'Tanay')]==m[mon(a,'Yash')]+1
C[4]=(['Tanay','Yash'], c4cal)
FINAL=[1,3,4,5,6,7,8,9,10,11,12]
