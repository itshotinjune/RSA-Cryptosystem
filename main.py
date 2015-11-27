from LargeRandomNumber import get_LargeRandomNumber
from getTwoPrimes import get_TwoPrimes
from getPublicPrivateKey import get_PublicPrivateKey
from inspect import currentframe, getframeinfo
from hashfun import hashfun
from FastExponentiation import FastExponentiation

length = 32
x = get_LargeRandomNumber(True)

(p_Alice,q_Alice) = get_TwoPrimes(True)
'''print "First prime is - ",p
print "Second prime is - ",q'''
n_Alice = p_Alice*q_Alice
'''print "n = ",n'''
phi_n_Alice = (p_Alice-1)*(q_Alice-1)
'''print "phi_n - ",phi_n'''

(e_Alice,d_Alice) = get_PublicPrivateKey(phi_n_Alice,True)
'''print "public key - ",e
print "private key - ",d'''

frameinfo = getframeinfo(currentframe())
print 'line: ',frameinfo.lineno+3
print "Integer:"
print "p_Alice = %d, q_Alice = %d, n_Alice = %d, e_Alice = %d, d_Alice = %d"%(p_Alice,q_Alice,n_Alice,e_Alice,d_Alice)
print "Bits:"
print "p_Alice = "+bin(p_Alice)[2:].zfill(length)
print "q_Alice = "+bin(q_Alice)[2:].zfill(length)
print "n_Alice = "+bin(n_Alice)[2:].zfill(length)
print "e_Alice = "+bin(e_Alice)[2:].zfill(length)
print "d_Alice = "+bin(d_Alice)[2:].zfill(length)
print "\n"


(p_Trent, q_Trent) = get_TwoPrimes(False)
n_Trent = p_Trent*q_Trent
phi_n_Trent = (p_Trent-1)*(q_Trent-1)
(e_Trent,d_Trent) = get_PublicPrivateKey(phi_n_Trent,False)
'''print "p = %d, q = %d, n = %d, e = %d, d = %d"%(p_Trent,q_Trent,n_Trent,e_Trent,d_Trent)'''

'''Creating certificate'''
length_r = 112
list_r = ['0']*length_r
list_r[0:48] = ['0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','1','0','1','1','0','1','1',
'0','0','0','1','1','0','1','0','0','1','0','1','1','0','0','0','1','1','0','1','1','0','0','1','0','1']
list_r[48:80] = list(bin(n_Alice)[2:].zfill(length))
list_r[80:112] = list(bin(e_Alice)[2:].zfill(length))
r = "".join(list_r)
hr = hashfun(r)
s = FastExponentiation(int(hr),d_Trent,n_Trent)
s = bin(s)[2:].zfill(length)
frameinfo = getframeinfo(currentframe())
print 'line: ',frameinfo.lineno+3
print "r = "+r
print "h(r) = "+hr
print "s = "+s
