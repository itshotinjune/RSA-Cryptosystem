'''This module computes hash of any given x'''
from xor import xor

def hashfun(x):
	len_x = len(x)
	hx = '00000000'
	'''Keep performing XOR operation with consecutive bytes of x'''
	for i in xrange(0,len_x-8+1,8):
		hx = xor(hx,x[i:i+8])

	return hx.zfill(32)