'''This module returns two randomly generated prime numbers'''

from LargeRandomNumber import get_LargeRandomNumber
from IsPrime import IsPrime
from MillerRabin import PrimalityTesting
from random import randint
from inspect import currentframe, getframeinfo


def get_TwoPrimes(disp):
	
	isPrime_p = False
	isPrime_q = False
	isPrime_x = True
	dec_p = 0
	dec_q = 0

	'''Keep trying until we find the first prime p'''
	while(not isPrime_p):
		'''Get some random large number'''
		p = get_LargeRandomNumber(False)
		dec_p = int(p,2)
		'''Check if it's prime'''
		(a_p,isPrime_p) = IsPrime(dec_p,False)

	'''Keep trying until we find the second prime q which is not equal to p'''
	while(dec_q != dec_p and not isPrime_q):
		'''Get some random large number'''
		q = get_LargeRandomNumber(False)
		'''Check if it's prime'''
		dec_q = int(q,2)
		(a_q,isPrime_q) =  IsPrime(dec_q,False)

	'''Generate some random even number and check if it's prime
	   The PrimalityTesting algorithm should output not a prime for
	   20 different values of a'''
	while isPrime_x:
		x = 2*randint(1,64)
		(a_x, isPrime_x) = IsPrime(x,False)

	'''Print the trace'''
	if disp:
		frameinfo = getframeinfo(currentframe())
		print 'line: ',frameinfo.lineno+3, 'file:', frameinfo.filename
		print "Trace: n = %d, a = %d" %(x,a_x)
	(a_x,isPrime_x) = PrimalityTesting(a_x,x-1,disp)

	'''Print the trace for p we got from above'''
	if disp:
		frameinfo = getframeinfo(currentframe())
		print 'line: ',frameinfo.lineno+3, 'file:', frameinfo.filename
		print "Trace: n = %d, a = %d" %(dec_p,a_p)
	(a_p,isPrime_p) = PrimalityTesting(a_p,dec_p-1,disp)
	return (dec_p,dec_q)


'''x = get_LargeRandomNumber(True)	
(p,q) = get_TwoPrimes()'''