R=lambda:[*map(int,input().split())]
p,P=R()
p-=P
t=m=M=0
c={*R()[1:]};C={*R()[1:]}
while t<1e7:t+=1;p+=m-M;m^=t in c;M^=t in C;-5<p<5==exit(print("bumper tap at time",t))
print("safe and sound")
