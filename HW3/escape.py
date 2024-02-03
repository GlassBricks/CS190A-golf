R=lambda:[*map(int,input().split())]
n,m,_=R()
n+=1
D=[[160]]*n
for g in[[{}for _ in D]]*m:u,v,c=R();g[u][v]=g[v][u]=c
e=R()
for s in R()[::-1]:
	O=D;D=[(1e9,)*2]*n;D[s]=1e-9,0;Z={*range(n)}
	while Z:
		s,d,u=min((*D[i],i)for i in Z);Z-={u}
		for o in g[u]:l=d+g[u][o];D[o]=min(D[o],(max(s,l/O[o][0]),l))
print(("IMPOSSIBLE",r:=min(D[i][0]for i in e))[r<1e9])
