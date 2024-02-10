R=lambda:eval(input().replace(*" ,"))
x,y=R()
exec("l,u,v=R();y+=(u-l)*(v-1);"*R())
print(x/y)
