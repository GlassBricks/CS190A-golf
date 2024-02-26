R=lambda:map(int,input().split())
n,m,c=R()
G=[input()for _ in[0]*m]
*K,=R()
t=2*n*m
Z=range(t+1)
C=[{}for _ in Z]
F=[-~t*[0]for _ in Z]
k=9**9
for i in range(n*m):
    x=i//n;y=i%n;o=i+n*m;v=G[x][y];C[i][o]=C[o][i]=K[ord(v)-97]if v.islower()else k
    if'B'==v:s=i
    for d,c in(-1,y),(1,n+~y),(-n,x),(n,m+~x):j=(t,i+d)[c>0];C[o][j]=k;C[j][o]=0
def D(c,v):
    v|={c}
    for o in C[c]:
        if{o}-v and C[c][o]-F[c][o]>=k and(o==t or D(o,v)):F[c][o]+=k;F[o][c]-=k;return 1
a=0
while k:
    if D(s,{s}):a+=k
    else:k//=2
print((-1,a)[a<3e8])
