R=lambda:map(int,input().split())
n,I=R()
d=[0,0]*n
a=[0,1]+d
g=[[]for _ in d]
b=[[]for _ in d]
for _ in[0]*I:x,y=R();g[x]+=y,;b[y]+=x,
for s,c in(1,g),(2,b):
	q={s};O=I;I={0}
	while q:v=q.pop();I&{v}or[*map(q.add,c[v])];I|={v}
for i in I&O:
	for j in g[i]:d[j]+=1
q={1}
while q:
	v=q.pop()
	for u in g[v]:a[u]+=a[v];d[u]-=1;d[u]or q.add(u)
print((str(a[2])[-9:],'inf')[any(d[i]for i in I)])
