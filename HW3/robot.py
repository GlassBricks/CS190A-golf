R=lambda:map(int,input().split())
n,m=R()
g={i-n:[R]for i in range(3*n)}
for v in[{0}]*m:a,b=R();g[a]+=b,
V=lambda c,b=0:c==R or(c in v)^1and(v.add(c)or V(g[-c][-1],b)+(b and sum(map(V,g[c][1:]))))
print(V(1,1))
