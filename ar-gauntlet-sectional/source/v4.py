from p4 import *
FIN=[3,4,5,6,7,8,9,10,11,12]
A=run(FIN); print('n',len(A)); [print(show(a)) for a in A]
DOY={(0,8):39,(0,23):54,(1,8):98,(1,23):113,(2,8):128,(2,23):143,(3,8):189,(3,23):204,(4,8):251,(4,23):266,(5,8):312,(5,23):327}
for a in A:
    o=order(a)
    first_off=[p for p in o if a['m_'+p]=='Off'][0]
    after_z=o[o.index('Zoya')+1]
    off31=[p for p in P if a['m_'+p]=='Off' and DAYS[mon(a,p)]==31]
    b46=[p for p in P if DOY[a['Zoya']]-DOY[a[p]]==46]
    print('Q1 descriptors',first_off,after_z,off31,b46,
          [nbetween(a,x,y) for x,y in [(first_off,'Zoya'),('Yash',after_z),(off31[0],'Vihaan'),('Zoya',b46[0])]])
# Q2
for a in A:
    print('Q2',a['Urvi'],a['Waseem'],DOY[a['Sana']]-DOY[a['Urvi']],DOY[a['Waseem']]-DOY[a['Vihaan']],
          DOY[a['Sana']]-DOY[a['Urvi']]>DOY[a['Waseem']]-DOY[a['Vihaan']])
# Q3
def q3b(a):
    o=order(a); t=o.index('Tanay'); z=o.index('Zoya')
    return sum(a['m_'+p]=='On' for p in o[:t])==sum(a['m_'+p]=='Off' for p in o[z+1:])
q3={'a':lambda a: idx(a['Sana'])-idx(a['Urvi'])-1-nbetween(a,'Urvi','Sana')==1,'b':q3b,
    'c':lambda a: DOY[a['Waseem']]-DOY[a['Vihaan']]==46,'d':lambda a: idx(max(empties(a),key=idx))>idx(a['Waseem'])}
print('Q3',{k:[f(a) for a in A] for k,f in q3.items()})
# Q4 drop condition 12 (Urvi alone)
B=run([k for k in FIN if k!=12]); print('Q4 n',len(B))
q4={'a':lambda a: a['Sana']==(0,23),'b':lambda a: a['Urvi']==(0,23) and a['Yash']==(1,8),
    'c':lambda a: any(e[0]==1 for e in empties(a)),'d':lambda a: a['Urvi'][1]==8 and a['Waseem'][1]==8}
print('Q4',{k:any(f(a) for a in B) for k,f in q4.items()})
# Q5
could=set()
for a in A:
    E={DOY[e] for e in empties(a)}
    for p in P:
        if DOY[a[p]]-15 in E: could.add(p)
print('Q5',could)
