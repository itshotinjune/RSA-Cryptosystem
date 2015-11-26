from getRandomNumber import get_RandomNumberlessThan
from MillerRabin import PrimalityTesting

def IsPrime(n,disp):

	testCounter = 0
	while (testCounter < 20):
		a = 0
		while (a == 0):
			a = get_RandomNumberlessThan(n)

		if disp:
			print "a = ",a

		(a,prime) = PrimalityTesting(a,n-1,disp)
		if prime is True:
			testCounter = testCounter + 1
		else :
			break

		if disp:
			print ''
	if prime is True and testCounter == 20 :
		return (a,True)
	else :
		return (a,False)

