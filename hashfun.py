from xor import xor

def hashfun(x):
	len_x = len(x)
	hx = '00000000'
	for i in xrange(0,len_x-8+1,8):
		hx = xor(hx,x[i:i+8])

	return hx.zfill(32)