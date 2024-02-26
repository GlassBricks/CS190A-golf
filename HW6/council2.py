def B(b):
	q=[b];P={};v={b}
	while c:=q.pop():
		for o in C[c]:
			if(o in v)^1and C[c][o]:
				v.add(o);P[o]=c;q+=o,
	while c!=b:p=P[c];C[p][c]-=1;C[c][p]+=1;c=p
U=input
from collections import*
for _ in[0]*int(U()):
	C=defaultdict(dict);P=set()
	for K in[set()]*int(U()):
		l,p,_,*J=U().split();C[l][p]=1;C[p][l]=0;P.add(p)
		for k in J:C[k][l]=1;C[l][k]=0;K.add(k)
	for p in P:C[p][0]=~-len(K)//2;C[0][p]=0
	try:
		for c in K:B(c)
		for c in K:
			for l in C[c]:C[c][l]or print(l,c)
	except:print('Impossible.')
