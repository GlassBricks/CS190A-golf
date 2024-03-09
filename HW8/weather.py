from bisect import*
A=lambda:[*map(int,input().split())]
I=2e9
while n:=A()[0]:
	E=[-I]*n
	for R in[[*E]]*n:e,r=A();E+=e,;R+=r,
	for i in range(n)[::-1]:R[i]=max(R[i*2],R[i*2+1])
	for M in[0]*A()[0]:
		(Y,y,u,s),(X,x,v,t)=[(v,k:=bisect_left(E,v),E[k-2*n]==v,R[k-n-n])for v in A()];l=y+u;r=x
		while(v|u)*r>l:M=max(M,l%2*R[l],r%2*R[r-1]);l=-~l>>1;r>>=1
		print("mftaarylubseee"[v*u*t>s or M>=(s,t)[v]or(v*u*x+Y>=X+y)*2::3])
	A()
