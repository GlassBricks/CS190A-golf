while 1:
	n,*L=map(int,input().split());l=1,0;P=[L.pop(0)+1j*L.pop(0)for _ in[0]*n]or exit()
	while(e:=max((abs(b:=P[i+1-n]-P[i])/abs(a:=P[i-1]-P[i])*(a/b).real,i)for i in range(n)))<l:*O,=P;P.pop(e[1]);l=e;n-=1
	print(n+1,*(int(i)for a in O for i in(a.real,a.imag)))


while 1:
	# get n, inputs
	n, *Line= map(int, input().split())
	last=1,0 # last point removed; initialized to -cos(180)
	P=[Line.pop(0)+1j*Line.pop(0) for _ in [0]*n] or exit() # turn input into list of complex numbers; exit if empty
	while 1:
		entry = max(
			(
				abs(b:=P[i+1-n]-P[i])/abs(a:=P[i-1]-P[i])*(a/b).real # this gets dot product of P[i], P[i-1], P[i+1]
			, i)
			for i in range(n)
		)
		if not entry < last: break # if the last corner we cut made it sharper, we're done
		# note that with 3 points left, cutting makes a new "infinitely" sharp corner, so that case is handled for feree
		*Old, = P # save the old list (to easily undo the last cut)
		P.pop(entry[1]) # cut the point
		# update values
		last = entry; n-=1
	print(n+1, *(int(i) for a in Old for i in (a.real, a.imag))) # print the number of corners, then corners themselves
