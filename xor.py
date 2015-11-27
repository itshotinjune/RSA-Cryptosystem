def xor(a,b):
	length = len(a)
	c = ['0']*length
	for i in range(0, length):
		if a[i] == '0' and b[i] == '0':
			c[i] = '0'
		elif a[i] == '1' and b[i] == '0':
			c[i] = '1'
		elif a[i] == '0' and b[i] == '1' :
			c[i] = '1'
		elif a[i]== '1' and b[i] == '1':
			c[i] = '0'

	return "".join(c)