from csp import solve
import sys
B=['E','H','K','M','P','U','W']
WTS=[9,12,16,18,25,27,36]
VARS=B+['w'+b for b in B]
DOM={**{b:list(range(1,8)) for b in B},**{'w'+b:WTS for b in B}}
def at(a,i):
    for b in B:
        if a.get(b)==i: return b
def wat(a,i): return a['w'+at(a,i)]
def wpos(a,w):
    for b in B:
        if a.get('w'+b)==w: return a[b]
W=['w'+b for b in B]
C={}
C[1]=(['E'], lambda a: a['E']==4)
C[2]=(B+W, lambda a: wpos(a,16)==7)
C[4]=(B+['wK','wU','wW','wE','wH','wM','wP'], lambda a: 1<a['K']<7 and a['wK']==wat(a,a['K']-1)+wat(a,a['K']+1))
C[7]=(B+W, lambda a: abs(wpos(a,36)-wpos(a,27))>1)
C[8]=(['wU','wW'], lambda a: a['wU']==2*a['wW'])
C[9]=(['wH','wM','wP'], lambda a: a['wM']>a['wH']>a['wP'])
C[10]=(B+W, lambda a: a['E']>=3 and a['wE']==wat(a,a['E']-1)+wat(a,a['E']-2))
C[11]=(B+W, lambda a: abs(a['P']-wpos(a,27))-1==2)
def run(keys,extra=()):
    return solve(VARS,DOM,[C[k] for k in keys]+list(extra),[B,W])
def show(a): return ' '.join(f"{at(a,i)}{wat(a,i)}" for i in range(1,8))+'  (bottom->top)'
if __name__=='__main__':
    keys=[int(x) for x in sys.argv[1].split(',')]
    S=run(keys); print(len(S))
    for a in S[:15]: print(show(a))
C[12]=(['M','U'], lambda a: a['M']>a['U'])
FINAL=[2,4,8,9,10,11,12]
