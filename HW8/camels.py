(n,),*A=[[*map(int,l.split())]for l in open(0)]
a=-n*~-n//2
for I in 1,0,2:
	M={A[I-1][i]:i for i in range(n)};T=[0]*n
	for h in A[I]:
		i=j=M[h]
		while~i:a+=T[i];i-=-~i&~i
		while j<n:T[j]+=1;j|=j+1
print(a//2)
