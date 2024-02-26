def B(b):
    q=[b];P={};v={b}
    while(c:=q.pop())+1:
        for o in C[c]:
            if{o}-v and C[c][o]:v|={o};P[o]=c;q+=o,
    while c-b:p=P[c];C[p][c]-=1;C[c][p]+=1;c=p
U=input
for*I,in[[]]*int(U()):
    K,Y,*C=[{}for _ in[0]*3100]
    for i in range(n:=int(U())):
        l,p,_,*J=U().split();I+=l,;C[i][Y.setdefault(p,len(Y)+n)]=1;C[Y[p]][i]=0
        for j in J:r=K.setdefault(j,len(K)+2*n);C[r][i]=1;C[i][r]=0
    for r in Y:C[Y[r]][-1]=~-len(K)//2;C[-1][Y[r]]=0
    try:[B(K[c])for c in K];[C[K[c]][i]or print(I[i],c)for c in K for i in C[K[c]]]
    except:print("Impossible.")
