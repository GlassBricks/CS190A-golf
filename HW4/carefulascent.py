R=lambda:eval(input().replace(*" ,"))
x,y=R()
exec("l,u,v=R();u-=l;y+=u*v-u;"*R())
print(x/y)
