R=lambda:map(int,input().split())
R()
*t,=R()
for n in R():
	t.sort()
	while n:t[-n]-=1;n-=1
print("YNeos"[any(t)::2])
