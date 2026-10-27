import itertools, collections
N=8
P=['Anvi','Bharat','Charu','Dev','Esha','Faiz','Gia','Hari']
PROF=['J','J','A','A','P','P','C','C']
def sols(clues, verbose=False):
    out=[]
    others=P[1:]
    for perm in itertools.permutations(others):
        order=['Anvi']+list(perm)
        pos={n:i for i,n in enumerate(order)}
        for fb in range(256):
            face={n:('in' if fb>>i &1 else 'out') for i,n in enumerate(order)}
            s={'pos':pos,'face':face,'at':order}
            if not all(c(s) for c in clues['pos']): continue
            for pa in set(itertools.permutations(PROF)):
                prof=dict(zip(P,pa))
                s2=dict(s,prof=prof)
                if all(c(s2) for c in clues['prof']):
                    out.append(s2)
    return out
def R(s,x,k): return s['at'][(s['pos'][x]+(-k if s['face'][x]=='in' else k))%N]
def L(s,x,k): return R(s,x,-k)
def nb(s,x): p=s['pos'][x]; return {s['at'][(p+1)%N], s['at'][(p-1)%N]}
def opp(s,x): return s['at'][(s['pos'][x]+4)%N]
def arcs(s,x,y):
    d=(s['pos'][y]-s['pos'][x])%N; return {d-1, N-d-1}
def show(s): return ' '.join(f"{n}({s['face'][n][0]},{s['prof'][n]})" for n in s['at'])
