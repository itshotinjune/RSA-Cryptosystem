from modulo import modulo

def FastExponentiation(a,x,n,disp):

	template = "{0:2}|{1:3}|{2:6}|{3:4}"
	if disp:
		print ("--------------------")
		print template.format("i","xi","y","y")
		print ("--------------------")
	x = (bin(x)[2:])[::-1]
	k = len(x)-1
	y = 1
	for i in range(k,-1,-1):
		y = modulo(y*y,n)
		y1 = y
		if x[i] == '1':
			y = modulo(a*y,n)
		y2 = y
		if disp:
			print template.format(str(i),str(x[i]),str(y1),str(y2))
	if disp:
		print ("--------------------")
	return y