import re, json, collections
from passages import PASSAGES
from questions import Q
L="abcd"
PT={p['id']:" ".join(p['text']).lower() for p in PASSAGES}
ABS=r"\b(only|any|all|every|never|always|no|none|solely|most|must|cannot|can never|entirely|wholly|merely|clearly|prove|whenever|whatever)\b"
HEDGE=r"\b(may|might|can|could|tends?|often|seldom|rarely|some|generally|usually|largely|probably|perhaps)\b"
CONTRAST=r"\b(though|but|while|yet|although|whereas|rather than)\b"
def words(s): return re.findall(r"[a-z'’]+", s.lower())
def ngr(ws,n=3): return set(tuple(ws[i:i+n]) for i in range(len(ws)-n+1))
def echo(opt,pid):
    pw=words(PT[pid]); og=ngr(words(opt)); 
    return len(og & ngr(pw))/max(1,len(og))
def place(qq):
    t=L.index(qq['target']); ds=[o for o in qq['opts'] if o[0]!="K"]; k=[o for o in qq['opts'] if o[0]=="K"][0]
    out=[None]*4; out[t]=k; it=iter(ds)
    for i in range(4):
        if out[i] is None: out[i]=next(it)
    return out
keys="".join(qq['target'] for qq in Q)
print("KEY:",keys, collections.Counter(keys))
runs=[i for i in range(1,24) if keys[i]==keys[i-1]]; triples=[i for i in range(2,24) if keys[i]==keys[i-1]==keys[i-2]]
print("back-to-back repeats at",[r+1 for r in runs],"triples",triples)
for i in range(4): print(" passage",i+1,keys[i*6:i*6+6],"distinct",len(set(keys[i*6:i*6+6])))
rank=collections.Counter(); rows=[]
st=dict(kabs=0,dabs=0,khed=0,dhed=0,kcon=0,dcon=0,kbec=0,dbec=0,kecho=[],decho=[])
fam=collections.Counter()
for n,qq in enumerate(Q,1):
    opts=place(qq); lens=[len(o[1]) for o in opts]; wl=[len(o[1].split()) for o in opts]
    t=L.index(qq['target']); order=sorted(range(4),key=lambda i:-lens[i]); r=order.index(t)+1
    if qq['type']!="Grammar": rank[r]+=1
    ratio=max(lens)/min(lens)
    for i,o in enumerate(opts):
        tx=o[1].lower(); isk=o[0]=="K"; pre="k" if isk else "d"
        st[pre+"abs"]+=len(re.findall(ABS,tx)); st[pre+"hed"]+=len(re.findall(HEDGE,tx))
        st[pre+"con"]+=len(re.findall(CONTRAST,tx)); st[pre+"bec"]+=len(re.findall(r"\bbecause\b|\bsince\b",tx))
        st[pre+"echo"].append(echo(o[1],qq['passage']))
        if not isk: fam[o[0]]+=1
    flag=" <-- spread" if ratio>1.18 and qq['type']!="Grammar" else ""
    print(f"Q{n:2} {qq['target']} {qq['type'][:22]:22} words {wl} chars {lens} keyrank {r} ratio {ratio:.2f}{flag}")
print("key length rank (1=longest), excl. grammar:",dict(sorted(rank.items())))
nk=24; nd=72
print(f"absolutes per option: key {st['kabs']/nk:.2f} distractor {st['dabs']/nd:.2f}")
print(f"hedges per option:    key {st['khed']/nk:.2f} distractor {st['dhed']/nd:.2f}")
print(f"contrast per option:  key {st['kcon']/nk:.2f} distractor {st['dcon']/nd:.2f}")
print(f"because/since per opt: key {st['kbec']/nk:.2f} distractor {st['dbec']/nd:.2f}")
print(f"echo (3-gram overlap): key {sum(st['kecho'])/nk:.3f} distractor {sum(st['decho'])/nd:.3f}")
print("trap families:",dict(sorted(fam.items())))
