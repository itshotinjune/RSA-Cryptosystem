'''This file is the main file to be exexcuted'''

from LargeRandomNumber import get_LargeRandomNumber
from getTwoPrimes import get_TwoPrimes
from getPublicPrivateKey import get_PublicPrivateKey
from inspect import currentframe, getframeinfo
from hashfun import hashfun
from FastExponentiation import FastExponentiation
from getRandomBit import get_RandomBit

length = 32
'''Get some large random number and show the trace how each bit is selected'''
x = get_LargeRandomNumber(True)

'''Get the two prime numbers for Alice'''
(p_Alice,q_Alice) = get_TwoPrimes(True)

'''Calculate the value of n for Alice'''
n_Alice = p_Alice*q_Alice

'''Calculate the value of phin'''
phi_n_Alice = (p_Alice-1)*(q_Alice-1)

'''Calculate the public and private key pair of Alice which are multiplicative inverses of each other'''
(e_Alice,d_Alice) = get_PublicPrivateKey(phi_n_Alice,True)

'''The position at which first 1 occurs in n'''
k = len(bin(n_Alice)[2:])


'''Print all the values obtained until now'''
frameinfo = getframeinfo(currentframe())
print 'line: ',frameinfo.lineno+3, 'file:', frameinfo.filename
print "Integer:"
print "p_Alice = %d, q_Alice = %d, n_Alice = %d, e_Alice = %d, d_Alice = %d"%(p_Alice,q_Alice,n_Alice,e_Alice,d_Alice)
print "Bits:"
print "p_Alice = "+bin(p_Alice)[2:].zfill(length)
print "q_Alice = "+bin(q_Alice)[2:].zfill(length)
print "n_Alice = "+bin(n_Alice)[2:].zfill(length)
print "e_Alice = "+bin(e_Alice)[2:].zfill(length)
print "d_Alice = "+bin(d_Alice)[2:].zfill(length)+"\n"


'''Get two prime numbers for Trent'''
(p_Trent, q_Trent) = get_TwoPrimes(False)

'''Calculate the value of n for Trent'''
n_Trent = p_Trent*q_Trent

'''Calculate the value of phin'''
phi_n_Trent = (p_Trent-1)*(q_Trent-1)

'''Calculate the public and private key pair of Trent which are multiplicative inverses of each other'''
(e_Trent,d_Trent) = get_PublicPrivateKey(phi_n_Trent,False)

'''r is of 14 bytes'''
length_r = 112
list_r = ['0']*length_r

'''Set 1-6 bytes of r i.e hardcode the byte representation of Alice'''
list_r[0:48] = ['0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','1','0','1','1','0','1','1',
'0','0','0','1','1','0','1','0','0','1','0','1','1','0','0','0','1','1','0','1','1','0','0','1','0','1']

'''Set the next 7-10 bytes of r which is n'''
list_r[48:80] = list(bin(n_Alice)[2:].zfill(length))

'''Set the next 11-14 bytes of r which is the e of Alice'''
list_r[80:112] = list(bin(e_Alice)[2:].zfill(length))

r = "".join(list_r)

'''Compute hash of r'''
hr = hashfun(r)

'''Decrypt hash of r using Trent's private key'''
s = FastExponentiation(int(hr),d_Trent,n_Trent,False)
s = bin(s)[2:].zfill(length)

'''Print all the values computed until now'''
frameinfo = getframeinfo(currentframe())
print 'line: ',frameinfo.lineno+3, 'file:', frameinfo.filename
print "r = "+r
print "h(r) = "+hr
print "s = "+s+"\n"
hr_int = int(hr,2)
s_int = int(s,2)
frameinfo = getframeinfo(currentframe())
print 'line: ',frameinfo.lineno+3, 'file:', frameinfo.filename
print "h(r) = %d"%hr_int
print "s = %d\n"%s_int

'''Now Alice and Bob cooperatively pick a random number u'''
'''Set all the bits of u until k to 0'''
list_u = ['0']*length
for i in range(0,length+1-k):
	list_u[i] = '0'

'''Set the k+1 bit of u to 1'''
list_u[length+1-k] = '1'

'''Generate random bits for the rest of the remaning bits in u'''
for i in range(length+2-k,length):
	(x,list_u[i]) = get_RandomBit()
u = "".join(list_u)

'''Computing the decimal value of u'''
u_int = int(u,2)

'''Printing all the values computed until now'''
frameinfo = getframeinfo(currentframe())
print 'line: ',frameinfo.lineno+1, 'file:', frameinfo.filename
print "k = %d, u = %d\n" % (k,u_int)
frameinfo = getframeinfo(currentframe())
print 'line: ',frameinfo.lineno+1, 'file:', frameinfo.filename
print "u = "+u+"\n"

'''Both Alice and Bob compute hash of u'''
hu = hashfun(u)
hu_int = int(hu,2)

'''Print u and hash of u'''
frameinfo = getframeinfo(currentframe())
print 'line: ',frameinfo.lineno+1, 'file:', frameinfo.filename
print "u = "+str(u_int)+"("+u+")"
print "h(u) = "+str(hu_int)+"("+hu+")"

'''Alice decrypts hash of u using her private key and sends to Bob'''
v = FastExponentiation(hu_int,d_Alice,n_Alice,False)

'''Bob encrypts the cipher using Alice's public key to get the hash back
thus ensuring that he is indeed talking to Alice'''
Ev = FastExponentiation(v,e_Alice,n_Alice,False)

print "v = D(d,h(u)) = " + str(v) + "(" + bin(v)[2:] + ")"
print "E(e,v) = " + str(Ev) + "(" + bin(Ev)[2:].zfill(32) + ")\n"

'''Show the trace of how the cipher is encrypted using Fast Exponentiation'''
Ev = FastExponentiation(v,e_Alice,n_Alice,True)