'''This module returns a random bit 0 or 1'''
from getRandomNumber import get_RandomNumber

def get_RandomBit():
	'''Get some random number'''
	n = get_RandomNumber()
	'''Extract the LSB and return that bit'''
	lsb = n[-1:]
	return (n,lsb)