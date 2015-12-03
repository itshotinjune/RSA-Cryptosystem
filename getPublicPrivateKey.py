'''This module returns a public and private key pair that are multiplicative inverses
of each other under modulo phin'''

from getTwoPrimes import get_TwoPrimes
from ExtendedEucledian import gcd
from inspect import currentframe, getframeinfo
from modulo import modulo


def get_PublicPrivateKey(phi_n,disp):

	if disp:
		frameinfo = getframeinfo(currentframe())
		print 'line: ',frameinfo.lineno+3, 'file:', frameinfo.filename

	'''Starting from 3 keep trying until we find a number that is co-prime with phi_n'''
	for e in range(3,phi_n):
		if disp:
			print "Trace: try e = %d" %(e)

		'''Calcuate the values of s,t and gcd of e and phi_n using Extended Eucledian algorithm'''
		(g,t,s) = gcd(e,phi_n,disp)

		'''If gcd is 1 then break we found the required e and compute respective d using the values of s and t'''
		if g == 1:
			break

	frameinfo = getframeinfo(currentframe())
	if disp:
		print 'line: ',frameinfo.lineno+2, 'file:', frameinfo.filename

	'''Nomalize d so that it is lesser than phi_n and also positive'''
	d = modulo((modulo(t,phi_n)+phi_n),phi_n)
	
	if disp:
		print "d = %d\n"%d
	return (e,d)