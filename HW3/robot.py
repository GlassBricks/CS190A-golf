R=lambda:map(int,input().split())
n,m=R()
g={i:[i]for i in range(-n,n+1)}
for v in[{0}]*m:a,b=R();g[a]+=b,
V=lambda c,b=0:c<1or(c in v)^1and(V(g[-c][v.add(c)or-1],b)+(b and sum(map(V,g[c]))))
print(V(1,1))
