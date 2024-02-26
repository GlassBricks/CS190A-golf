R=lambda:map(int,input().split())
n,m,s,t=R()
Z=range(n)
C=[{}for _ in Z]
F=[n*[0]for _ in C]
for m in[0]*m:u,v,c=R();C[u][v]=c;C[v].setdefault(u,0)
k=9**9
def D(c,v):
	v|={c}
	for o in C[c]:
		if{o}-v and C[c][o]-F[c][o]>=k and(o==t or D(o,v)):F[c][o]+=k;F[o][c]-=k;return 1
while k:
	if D(s,{s}):m+=k
	else:k//=2
print(n,m,len(r:=[(i,j,v)for i in Z for j in Z if(v:=F[i][j])>0]))
for i in r:print(*i)
