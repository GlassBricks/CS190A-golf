R=lambda:[*map(int,input().split())]
def t(l):
	Q={0},{0};*d,=D
	while q:=Q[l&1]:
		for u in c[q.pop()]:d[u]-=1;d[u]or Q[L[u-1]<2].add(u)
		l+=not q
	return l
for _ in[0]*R()[0]:
	n,m=R();D=[2]*-~n;L=R();c=[range(1,-~n)]+[[]for _ in D]
	for _ in[0]*m:a,b=R();c[a]+=b,;D[b]+=1
	print(min(t(-2),t(-1)-1))
