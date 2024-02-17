R=lambda:map(int,input().split())
n,I=R()
d=[0]*-~n
a=[0,1]+d
g=[[]for _ in d]
for b in[[[]for _ in d]]*I:x,y=R();g[x]+=y,;b[y]+=x,
for c,*q in(g,1),(b,2):
	O=I;I={0}
	while q:v=q.pop();q+=c[v]*len({v}-I);I|={v}
for i in I&O:
	for j in g[i]:d[j]+=1
q={1}
while q:
	v=q.pop()
	for u in g[v]:a[u]+=a[v];d[u]-=1;d[u]or q.add(u)
print((str(a[2])[-9:],'inf')[any(d[i]for i in I)])
