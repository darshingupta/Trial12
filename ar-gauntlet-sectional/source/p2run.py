from p2 import *
import sys
C={
 1:(['Kabir','Rhea'], lambda s: s.R('Kabir',1)=='Rhea'),
 2:(['Rhea','Pari'], lambda s: s.R('Pari',2)==s.F('Rhea')),
 3:(['Omkar','Mohan'], lambda s: s.F('Omkar')==s.L('Mohan',1)),
 4:(['Vani','Naina'], lambda s: (s.gap('Vani','Naina') or set())>={1} and 1 in s.gap('Vani','Naina')),
 6:(['Leela','Pari'], lambda s: s.L('Pari',2)=='Leela' and not s.inner('Leela')),
 7:(['Tara','Rhea'], lambda s: s.F('Tara')==s.L('Rhea',1)),
 8:(['Qadir','Omkar'], lambda s: s.F('Qadir')==s.R('Omkar',2)),
 9:(['Uday','Pari','Naina'], lambda s: s.F('Naina') not in ('Uday','Pari')),
}
def run(keys):
    return solve([C[k] for k in keys])
if __name__=='__main__':
    keys=[int(x) for x in sys.argv[1].split(',')]
    S=run(keys); print(len(S))
    for a in S[:10]: print(show(a))
def opp_in_circle(s,x):
    c,i=s.a[x]; return s.inv[(c,(i+3)%6)]
C[10]=(['Vani','Tara'], lambda s: s.F('Vani')==opp_in_circle(s,'Tara'))
FINAL=[1,2,3,4,6,7,8,9,10]
