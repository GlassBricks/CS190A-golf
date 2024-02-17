D={0:0}
def T(m):[D.update({a+m*i:min(D.get(a+m*i,999),D[a]+1)for a in D})for i in[*map(int,input().split())][1:]]
T(1)
del D[0]
T(-1)
print(D.get(0,"impossible"))
