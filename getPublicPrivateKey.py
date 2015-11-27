from getTwoPrimes import get_TwoPrimes
from ExtendedEucledian import gcd
from inspect import currentframe, getframeinfo
from modulo import modulo


def get_PublicPrivateKey(phi_n,disp):

	if disp:
		frameinfo = getframeinfo(currentframe())
		print 'line: ',frameinfo.lineno+3
	for e in range(3,phi_n):
		if disp:
			print "Trace: try e = %d" %(e)
		(g,t,s) = gcd(e,phi_n,disp)
		if g == 1:
			break

	frameinfo = getframeinfo(currentframe())
	if disp:
		print 'line: ',frameinfo.lineno+2
	d = modulo((modulo(t,phi_n)+phi_n),phi_n)
	if disp:
		print "d = %d\n"%d
	return (e,d)