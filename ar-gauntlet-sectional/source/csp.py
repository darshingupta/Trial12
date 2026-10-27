class Sol(dict):
    __getattr__=dict.__getitem__
def solve(variables, domains, constraints, alldiff_groups=(), limit=None):
    """variables: list; domains: dict var->list; constraints: list of (scope, fn(asg)->bool).
    alldiff_groups: list of lists of vars whose values must be distinct."""
    sols=[]; asg={}
    by_var={v:[] for v in variables}
    for sc,fn in constraints:
        last=max(variables.index(v) for v in sc)
        by_var[variables[last]].append((sc,fn))
    ad_of={v:[g for g in alldiff_groups if v in g] for v in variables}
    def rec(k):
        if limit and len(sols)>=limit: return
        if k==len(variables):
            sols.append(Sol(asg)); return
        v=variables[k]
        for val in domains[v]:
            if any(asg.get(u)==val for g in ad_of[v] for u in g if u!=v and u in asg): continue
            asg[v]=val
            if all(fn(asg) for sc,fn in by_var[v]): rec(k+1)
            del asg[v]
    rec(0)
    return sols
