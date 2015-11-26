from modulo import modulo

def PrimalityTesting(a,x,disp):
	n = x+1
	x = (bin(x)[2:])[::-1]
	k = len(x)-1
	y = 1

	template = "{0:2}|{1:3}|{2:4}|{3:4}|{4:4}" # column widths: 8, 10, 15, 7, 10
	if disp:
		print ("--------------------")
		print template.format("i", "xi", "z", "y", "y")
		print ("--------------------")

	for i in range(k,-1,-1):
		z = y
		y = modulo(y*y,n)
		y1=y

		if ((y == 1) and (z != 1) and (z != n-1)):
			if disp:
				print "%d is not a prime because %d^2 mod %d = 1 and %d != 1 and %d != %d - 1\n" %(n,z,n,z,z,n)
			return (a,False)
		if x[i] == '1':
			y = modulo(y*a,n)
		y2=y

		if disp:
			print template.format(str(i),str(x[i]),str(z),str(y1),str(y2))
	

	if y != 1 :
		if disp:
			print "%d is not a prime because %d^%d mod %d != 1\n"  % (n,a,n-1,n)
		return (a,False)
	else:
		if disp:
			print 'perhaps a prime'
		return (a,True)