'''This module generates a randon number'''
import random
from modulo import modulo

length = 32

'''Procedure to get some random number of 32 bits'''
def get_RandomNumber():
	n = random.getrandbits(length)
	n = bin(n)[2:].zfill(length)
	return n

'''Procedure to get some random number of 32 bits i.e less than some specified n'''
def get_RandomNumberlessThan(n):
	'''Get some random number and take its modulo with n'''
	x = get_RandomNumber()
	x = modulo(int(x,2),n)
	return x