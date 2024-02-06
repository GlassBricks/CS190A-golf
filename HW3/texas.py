n=int(input())
D=[(1e9,0)]*-~n+[(0,0)]
Z={*range(n+2)}
P=[complex(*map(int,input().split()))for _ in D]
while Z:
	d,c=min((D[i][0],i)for i in Z);Z-={c}
	for i in Z:D[i]=min(D[i],(d+abs(P[i]-P[c])**2,c))
c=n
D[c][1]>c==exit(print('-'))
while(c:=D[c][1])<n:print(c)
