from modulo import modulo

def FastExponentiation(a,x,n):
	x = (bin(x)[2:])[::-1]
	k = len(x)-1
	y = 1
	for i in range(k,-1,-1):
		y = modulo(y*y,n)
		if x[i] == '1':
			y = modulo(a*y,n)
	return y
	
FastExponentiation(17,22,21)