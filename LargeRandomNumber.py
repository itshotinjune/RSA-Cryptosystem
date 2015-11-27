from inspect import currentframe, getframeinfo
from getRandomBit import get_RandomBit
from MillerRabin import PrimalityTesting
from getRandomNumber import get_RandomNumberlessThan

lengthPrime = 7
bitInteger = 32

def get_LargeRandomNumber(disp):

	p = '0'*(bitInteger)
	list_p = list(p)
	list_p[bitInteger-1] = '1'
	list_p[bitInteger-lengthPrime] = '1'

	frameinfo = getframeinfo(currentframe())
	if disp:
		print 'line: ',frameinfo.lineno+3
		print "Bit: 0 set as 1"
	for i in range(bitInteger-lengthPrime+1, bitInteger-1):
		(num, list_p[i]) =  get_RandomBit()
		if disp:
			print "Bit:",(i-(bitInteger-lengthPrime)), "number ", num, "extracts ", list_p[i]
		
	p = "".join(list_p)
	if disp:
		print "Bit: 6 set as 1"
		print "Number is ",int(p[bitInteger-lengthPrime:],2), "-",p,'\n'
	return p