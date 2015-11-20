from getRandomNumber import get_RandomNumber

def get_RandomBit():
	n = get_RandomNumber()
	lsb = n[-1:]
	return (n,lsb)