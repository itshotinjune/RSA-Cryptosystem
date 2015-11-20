from modulo import modulo

def FastExponentiation(a,x,n):
	x = (bin(x)[2:])[::-1]
	k = len(x)-1
	y = 1
	for i in range(k,-1,-1):
		print " i = " + str(i) + " x = " + str(x[i]),
		y = modulo(y*y,n)
		print " y = " + str(y), 
		if x[i] == '1':
			y = modulo(a*y,n)
		print " y = " + str(y)

FastExponentiation(17,22,21)