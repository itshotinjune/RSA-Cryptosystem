'''This module generates a random large number possibly a prime'''

from inspect import currentframe, getframeinfo
from getRandomBit import get_RandomBit
from MillerRabin import PrimalityTesting
from getRandomNumber import get_RandomNumberlessThan

lengthPrime = 7
bitInteger = 32

def get_LargeRandomNumber(disp):

	'''Initially set all the bits to 0'''
	p = '0'*(bitInteger)
	list_p = list(p)

	'''Set the last bit to 1 to ensure that the number is odd thus a possible prime'''
	list_p[bitInteger-1] = '1'

	'''Set the first bit (or 25th bit) to 1 ensure that the number is large'''
	list_p[bitInteger-lengthPrime] = '1'

	frameinfo = getframeinfo(currentframe())
	if disp:
		print 'line: ',frameinfo.lineno+3, 'file:', frameinfo.filename
		print "Bit: 0 set as 1"

	'''Randomly pick the other bits from 2-6' to be 0 or 1'''
	for i in range(bitInteger-lengthPrime+1, bitInteger-1):
		'''num is the psuedorandom number generated
		and list_p[i] is the LSB of num'''
		(num, list_p[i]) =  get_RandomBit()
		
		if disp:
			print "Bit:",(i-(bitInteger-lengthPrime)), "number ", num, "extracts ", list_p[i]
		
	p = "".join(list_p)
	if disp:
		print "Bit: 6 set as 1"
		print "Number is ",int(p[bitInteger-lengthPrime:],2), "-",p,'\n'
	return p