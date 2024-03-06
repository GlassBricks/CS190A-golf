R=[[*map(int,l.split())]for l in open(0)]
n,m,r=R[0]
P=R[1:n+1]
L=R[-m:]
print("yneos"[n!=m+1+sum(abs(y*c-b*z+(a*z-x*c)*1j)/r<abs(a*y-x*b)for a,b,c in L for x,y,z in L)/2or len({(*(a*x+b*y<-c for a,b,c in L),)for x,y in P})<n::2])


R=[[*map(int,l.split())]for l in open(0)] # read everything
n,m,r = R[0]
points = R[1:n+1]
lines = R[-m:]

print("yneos"[ # prints yes or no, depending on result in brackets (due to ::2 far below)
# check that there are as many points as sections
# n should equal m+1+intersections
n!=m+1+
# count of line intersections
sum(
	abs(y*c-b*z+(a*z-x*c)*1j)/r<abs(a*y-x*b)  # true if lines intersect inside radius r; rearranged equation of sqrt(x*x + y*y) < r
	for a,b,c in lines
	for x,y,z in lines
)/2 # since we double count every intersection
# if true, print no; else continue:
	or
# check that every point is in unique section; e.g. they all have the same "line-sideness"
	len({
		(*(
			a*x+b*y<-c for a,b,c in lines  # a tuple of booleans, for the line-sideness of each point
		),)
		for x,y in points
	} # collect into a set
	)<n  # size of set should be n (all unique)
	::2
])
