o=lambda a,b,c,d,e,f:((k:=(e-c)*(d-b)-(f-d)*(c-a))>0)-(k<0)
while S:=[(i,*map(eval,input().split()))for i in range(int(input()))]:H=[{j for j,*W in S if-1>o(*A,*W[:2])*o(*A,*W[2:])+o(*W,*A[:2])*o(*W,*A[2:])}for i,*A in S];print(sum(len(H[j]&s)for s in H for j in s)//6)
