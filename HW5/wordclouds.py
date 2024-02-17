R=lambda:map(int,input().split())
n,c=R()
Z=range(n)
P=[[0,*R()]for i in Z]
for k in Z:H=W=0;P[-~k%n][0]=min(m+(H:=max(H,h))for m,w,h in P[k::-1]if(W:=W+w)<=c)
print(P[0][0])

# Michael beat me using:
# partial sum shenanigans
# input fun
