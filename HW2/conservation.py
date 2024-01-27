R=lambda:[*map(int,input().split())]
def t(l):
	def A(u):d[u]-=1;d[u]or Q[L[u-1]<2].add(u)
	Q={0},{0};d=[*D]
	while q:=Q[l&1]:[*map(A,c[q.pop()])];l+=not q
	return l
for _ in[0]*R()[0]:
	n,m=R();n+=1;D=[2]*n;c=[[]for _ in D];L=R();c[0]=range(1,n)
	for _ in[0]*m:a,b=R();c[a]+=[b];D[b]+=1
	print(min(t(-2),t(-1)-1))
