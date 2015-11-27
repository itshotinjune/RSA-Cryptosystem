from LargeRandomNumber import get_LargeRandomNumber
from getTwoPrimes import get_TwoPrimes
from getPublicPrivateKey import get_PublicPrivateKey
from inspect import currentframe, getframeinfo

length = 32
x = get_LargeRandomNumber(True)

(p,q) = get_TwoPrimes()
'''print "First prime is - ",p
print "Second prime is - ",q'''
n = p*q
'''print "n = ",n'''
phi_n = (p-1)*(q-1)
'''print "phi_n - ",phi_n'''

(e,d) = get_PublicPrivateKey(phi_n)
'''print "public key - ",e
print "private key - ",d'''

frameinfo = getframeinfo(currentframe())
print 'line: ',frameinfo.lineno+3
print "Integer:"
print "p = %d, q = %d, n = %d, e = %d, d = %d"%(p,q,n,e,d)
print "Bits:"
print "p = "+bin(p)[2:].zfill(length)
print "q = "+bin(q)[2:].zfill(length)
print "n = "+bin(n)[2:].zfill(length)
print "e = "+bin(e)[2:].zfill(length)
print "d = "+bin(d)[2:].zfill(length)