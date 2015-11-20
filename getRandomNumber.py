import random
from modulo import modulo

length = 32

def get_RandomNumber():
	n = random.getrandbits(length)
	n = bin(n)[2:].zfill(length)
	return n

def get_RandomNumberlessThan(n):
	x = get_RandomNumber()
	x = modulo(int(x,2),n)
	return x