from LargeRandomNumber import get_LargeRandomNumber
from IsPrime import IsPrime
from MillerRabin import PrimalityTesting
from random import randint
from inspect import currentframe, getframeinfo


def get_TwoPrimes():
	
	isPrime_p = False
	isPrime_q = False
	isPrime_x = True

	while(not isPrime_p):
		p = get_LargeRandomNumber(False)
		dec_p = int(p,2)
		(a_p,isPrime_p) = IsPrime(dec_p,False)

	while(not isPrime_q):
		q = get_LargeRandomNumber(False)
		dec_q = int(q,2)
		(a_q,isPrime_q) =  IsPrime(dec_q,False)

	while isPrime_x:
		x = 2*randint(1,64)
		(a_x, isPrime_x) = IsPrime(x,False)

	frameinfo = getframeinfo(currentframe())
	print 'line: ',frameinfo.lineno+3
	print "Trace: n = %d, a = %d" %(x,a_x)
	(a_x,isPrime_x) = PrimalityTesting(a_x,x-1,True)

	frameinfo = getframeinfo(currentframe())
	print 'line: ',frameinfo.lineno+3
	print "Trace: n = %d, a = %d" %(dec_p,a_p)
	(a_p,isPrime_p) = PrimalityTesting(a_p,dec_p-1,True)


x = get_LargeRandomNumber(True)	
get_TwoPrimes()