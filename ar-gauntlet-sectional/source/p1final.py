from p1 import *
def gapclue(s):
    d=(s['pos']['Bharat']-s['pos']['Dev'])%8
    if d==2: m=s['at'][(s['pos']['Dev']+1)%8]
    elif d==6: m=s['at'][(s['pos']['Dev']-1)%8]
    else: return False
    return s['face'][m]==s['face']['Anvi']
POS={
 1: lambda s: L(s,'Gia',3)=='Charu',
 2: lambda s: sum(v=='in' for v in s['face'].values())==4,
 3: lambda s: R(s,'Faiz',1)=='Esha' and R(s,'Esha',1)=='Faiz',
 4: gapclue,
 5: lambda s: s['face']['Dev']=='out',
 6: lambda s: all(s['face'][n]!=s['face']['Faiz'] for n in nb(s,'Faiz')),
 7: lambda s: sum(s['face'][n]==s['face']['Bharat'] for n in nb(s,'Bharat'))==1,
 8: lambda s: L(s,'Gia',2)=='Hari',
}
PROFC={
 9: lambda s: s['prof'][opp(s,[n for n in P if s['prof'][n]=='J'][0])]=='J',
 10: lambda s: any(s['prof'][n]=='C' and s['face'][n]=='in' for n in nb(s,'Faiz')) and any(s['prof'][n]=='P' for n in nb(s,'Faiz')),
 11: lambda s: s['prof'][L(s,'Hari',2)]=='A',
 12: lambda s: s['prof']['Bharat']==s['prof']['Esha'],
 13: lambda s: s['prof']['Dev']!='P',
 14: lambda s: all(s['prof'][m]!='J' for n in P if s['prof'][n]=='A' for m in nb(s,n)),
}
def run(drop=()):
    return sols({'pos':[c for k,c in POS.items() if k not in drop],'prof':[c for k,c in PROFC.items() if k not in drop]})
if __name__=='__main__':
    S=run(); print(len(S)); [print(show(s)) for s in S]
    for k in list(POS)+list(PROFC):
        S2=run((k,)); print('drop',k,len(S2))
