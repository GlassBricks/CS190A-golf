*A,=map(R:=lambda _:eval(input().replace(*" ,")),[0]*R(0))
l,_=max(A)
T=lambda m:max(V:=[v*(l+m-t)for t,v in A])-min(V)
e=l*l
while e>1e-8:l+=(T(e:=e*.7)>T(2*e))*e
print(T(e))
