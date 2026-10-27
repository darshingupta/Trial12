from p1final import *
import copy
S=run(); assert len(S)==1; s=S[0]
def kr(X,Y):
    for k in range(1,8):
        if R(s,X,k)==Y: return k
# Q1 odd one out: relation of Y wrt X
opts=[('Anvi','Charu'),('Bharat','Faiz'),('Esha','Gia'),('Dev','Hari')]
print('Q1 rel', [kr(*o) for o in opts])
# Q2
clerk_out=[n for n in P if s['prof'][n]=='C' and s['face'][n]=='out']; assert len(clerk_out)==1
x=L(s,clerk_out[0],1); print('Q2', R(s,x,2))
# Q3
profs=[n for n in P if s['prof'][n]=='P']; I=arcs(s,*profs)=={3}
II=all(any(R(s,a,1)==c for a in P if s['prof'][a]=='A') for c in P if s['prof'][c]=='C')
III=all(any(s['prof'][m]=='C' for m in nb(s,j)) for j in P if s['prof'][j]=='J')
print('Q3',I,II,III)
# Q4
base=(tuple(s['at']),tuple(sorted(s['face'].items())))
for k in [2,7,10,11]:
    alts=run((k,)); same=all((tuple(a['at']),tuple(sorted(a['face'].items())))==base for a in alts)
    print('Q4 drop',k,len(alts),'seats+facing unchanged' if same else 'changes')
# Q5 flip
t=copy.deepcopy(s); t['face']={k:('out' if v=='in' else 'in') for k,v in s['face'].items()}
print('Q5', R(t,L(t,'Gia',2),1))
