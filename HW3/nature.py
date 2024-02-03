from heapq import*
R=lambda:map(int,input().split())
for _ in range(*R()):
	n,m,l,_=R();a,*q=0,;S={*R()}
	for g in[[[]for _ in[0]*-~n]]*m:u,v,c=R();g[u]+=(c+l,v),;g[v]+=(c+l,u),
	def A(x):[o[1]in S or heappush(q,o)for o in g[x]]
	[*map(A,S)]
	while len(S)<n:c,u=heappop(q);u in S or A(u)or(a:=a+c);S.add(u)
	print(a)
