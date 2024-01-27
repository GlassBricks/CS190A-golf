R=lambda:[*map(int,input().split())]
m={}
a=0
for _ in[0]*R()[0]:
	I={*R()[1:]};c={R}
	if all(i in c or I>=(o:=m.get(i,{i}))and(c.update(o),)for i in I):
		a+=1
		for i in I:m[i]=I
print(a)
