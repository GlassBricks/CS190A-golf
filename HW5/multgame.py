for n in map(int,open(0)):
	n-=1
	while n>17:n//=18
	print("OSltlaine"[n<9::2],"wins.")

# Michael beat me: by changing some constants you can avoid n-=1
