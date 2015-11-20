from modulo import modulo

def PrimalityTesting(a,x):
	n = x+1
	x = (bin(x)[2:])[::-1]
	k = len(x)-1
	y = 1

	for i in range(k,-1,-1):
		z = y
		print "xi = ", x[i],
		print " z = ",z,
		y = modulo(y*y,n)
		print " y = ",y,
		if ((y == 1) and (z != 1) and (z != n-1)):
			print '\nn is not a prime'
			return 0
		if x[i] == '1':
			y = modulo(y*a,n)
		print " y = ",y
	

	if y != 1 :
		print 'n is not a prime'
		return 0
	else:
		print 'perhaps a prime'
		return 1