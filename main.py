from LargeRandomNumber import get_LargeRandomNumber
from getTwoPrimes import get_TwoPrimes
from getPublicPrivateKey import get_PublicPrivateKey
from inspect import currentframe, getframeinfo
from hashfun import hashfun
from FastExponentiation import FastExponentiation
from getRandomBit import get_RandomBit

length = 32
x = get_LargeRandomNumber(True)

(p_Alice,q_Alice) = get_TwoPrimes(True)
n_Alice = p_Alice*q_Alice
phi_n_Alice = (p_Alice-1)*(q_Alice-1)
(e_Alice,d_Alice) = get_PublicPrivateKey(phi_n_Alice,True)
k = len(bin(n_Alice)[2:])

frameinfo = getframeinfo(currentframe())
print 'line: ',frameinfo.lineno+3
print "Integer:"
print "p_Alice = %d, q_Alice = %d, n_Alice = %d, e_Alice = %d, d_Alice = %d"%(p_Alice,q_Alice,n_Alice,e_Alice,d_Alice)
print "Bits:"
print "p_Alice = "+bin(p_Alice)[2:].zfill(length)
print "q_Alice = "+bin(q_Alice)[2:].zfill(length)
print "n_Alice = "+bin(n_Alice)[2:].zfill(length)
print "e_Alice = "+bin(e_Alice)[2:].zfill(length)
print "d_Alice = "+bin(d_Alice)[2:].zfill(length)+"\n"


(p_Trent, q_Trent) = get_TwoPrimes(False)
n_Trent = p_Trent*q_Trent
phi_n_Trent = (p_Trent-1)*(q_Trent-1)
(e_Trent,d_Trent) = get_PublicPrivateKey(phi_n_Trent,False)

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
print "s = "+s+"\n"

hr_int = int(hr,2)
s_int = int(s,2)
frameinfo = getframeinfo(currentframe())
print 'line: ',frameinfo.lineno+3
print "h(r) = %d"%hr_int
print "s = %d\n"%s_int

list_u = ['0']*length
for i in range(0,length+1-k):
	list_u[i] = '0'
list_u[length+1-k] = '1'
for i in range(length+2-k,length):
	(x,list_u[i]) = get_RandomBit()
u = "".join(list_u)
u_int = int(u,2)
frameinfo = getframeinfo(currentframe())
print 'line: ',frameinfo.lineno+1
print "k = %d, u = %d\n" % (k,u_int)
frameinfo = getframeinfo(currentframe())
print 'line: ',frameinfo.lineno+1
print "u = "+u+"\n"

hu = hashfun(u)
hu_int = int(hu,2)
frameinfo = getframeinfo(currentframe())
print 'line: ',frameinfo.lineno+1
print "u = "+str(u_int)+"("+u+")"
print "h(u) = "+str(hu_int)+"("+hu+")\n"

v = FastExponentiation(hu_int,d_Alice,n_Alice)
Ev = FastExponentiation(v,e_Alice,n_Alice)

frameinfo = getframeinfo(currentframe())
print 'line: ',frameinfo.lineno+1
print "v = D(d,h(u)) = " + str(v) + "(" + bin(v)[2:] + ")"
print "E(e,v) = " + str(Ev) + "(" + bin(Ev)[2:] + ")"

