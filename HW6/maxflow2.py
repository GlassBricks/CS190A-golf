R=lambda:map(int,input().split())
n,m,s,t=R()
cap=[{}for _ in [0]*n]
# cap is also residuals
flow=[{}for _ in [0]*n]
for _ in [0]*m:
	u,v,c=R()
	cap[u][v]=c
	cap[v][u]=cap[v].get(u,0)
	flow[u][v]=0
	flow[v][u]=0

from heapq import *
def edKarp():
	q=[(-1e9,s)]
	vis=[0]*n
	prev=[-1]*n
	amt=[0]*n
	while q:
		nf,u=heappop(q)
		f=-nf
		if vis[u]: continue
		vis[u]=1
		if u==t:
			break
		for o in cap[u]:
			if vis[o]: continue
			newFlow=min(f,cap[u][o]-flow[u][o])
			if newFlow>amt[o]:
				amt[o]=newFlow
				heappush(q,(-amt[o],o))
				prev[o]=u
	else: return 0

	cur=t
	while cur!=s:
		p=prev[cur]
		flow[p][cur]+=f
		flow[cur][p]-=f
		cur=p
	return f
f=0
while x:=edKarp():
	# print(x)
	f+=x

edges=[]
for i in range(n):
	for j in flow[i]:
		if flow[i][j]>0:
			edges.append((i,j,flow[i][j]))
print(n,f,len(edges))
for u,v,c in edges:
	print(u,v,c)
