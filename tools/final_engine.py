"""Boolean engine for the final-exam site: prime implicants, minimal and hazard-free covers, JK design."""
import itertools
def primes(nv, ones, dc=()):
    allowed=set(ones)|set(dc); N=1<<nv; out=[]
    cubes=[]
    for mask in range(N):
        for val in range(N):
            if val&~mask: continue
            cov=frozenset(m for m in range(N) if (m&mask)==val)
            if cov<=allowed: cubes.append((mask,val,cov))
    for c in cubes:
        if not any(c[2]<d[2] for d in cubes) and c[2]&set(ones): out.append(c)
    return out
def tname(mask,val,names,nv):
    s=""
    for i in range(nv):
        bit=1<<(nv-1-i)
        if mask&bit: s+=names[i]+("" if val&bit else "'")
    return s or "1"
def mincover(nv, ones, dc=(), hazard_free=False):
    ones=set(ones)
    if not ones: return []
    P=primes(nv,ones,dc)
    need=[frozenset([m]) for m in ones]
    if hazard_free:
        for m in ones:
            for b in range(nv):
                n=m^(1<<b)
                if n in ones and m<n: need.append(frozenset([m,n]))
    best=None
    for k in range(1,len(P)+1):
        for combo in itertools.combinations(P,k):
            if all(any(nd<=c[2] for c in combo) for nd in need):
                cost=sum(bin(c[0]).count('1') for c in combo)
                if best is None or cost<best[0]: best=(cost,combo)
        if best: break
    return list(best[1])
def sop(nv,ones,dc,names,hazard_free=False):
    if not set(ones): return "0"
    c=mincover(nv,ones,dc,hazard_free)
    return " + ".join(tname(m,v,names,nv) for m,v,_ in c)
def ev(expr, env):
    # python-style expression eval with ' as postfix not: use custom parser
    import re
    toks=re.findall(r"[A-Za-z][0-9]*|[()'+^]|[01]",expr.replace(" ",""))
    pos=0
    def peek(): return toks[pos] if pos<len(toks) else None
    def atom():
        nonlocal pos
        t=toks[pos]; pos+=1
        if t=="(":
            v=orx(); pos+=1
        elif t in "01": v=int(t)
        else: v=env[t]
        while peek()=="'": pos+=1; v=1-v
        return v
    def andx():
        v=atom()
        while peek() is not None and peek() not in "+)^": v&=atom()
        return v
    def xorx():
        v=andx()
        while peek()=="^":
            nonlocal pos; pos+=1; v^=andx()
        return v
    def orx():
        nonlocal pos
        v=xorx()
        while peek()=="+": pos+=1; v|=xorx()
        return v
    return orx()
def minterms(expr,names):
    nv=len(names); r=[]
    for m in range(1<<nv):
        env={names[i]:(m>>(nv-1-i))&1 for i in range(nv)}
        if ev(expr,env): r.append(m)
    return r
def jk_design(nxt, nb, names, dc=()):
    res={}
    for b in range(nb):
        bit=nb-1-b; J=[];Jd=[];K=[];Kd=[]
        for m,n in nxt.items():
            q=(m>>bit)&1; qn=(n>>bit)&1
            if q==0:
                Kd.append(m)
                if qn: J.append(m)
            else:
                Jd.append(m)
                if not qn: K.append(m)
        res["J"+names[b]]=(J,Jd+list(dc)); res["K"+names[b]]=(K,Kd+list(dc))
    return res
