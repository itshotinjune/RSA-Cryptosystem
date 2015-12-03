'''This module checks if a given number is prime or not'''
from getRandomNumber import get_RandomNumberlessThan
from MillerRabin import PrimalityTesting

def IsPrime(n,disp):

	'''Check if the number passes Primality Testing for 20 values of a'''
	testCounter = 0
	while (testCounter < 20):
		a = 0
		'''Get a random numer i.e less than n and not 0'''
		while (a == 0):
			a = get_RandomNumberlessThan(n)

		if disp:
			print "a = ",a

		'''Check if it's prime or not'''
		(a,prime) = PrimalityTesting(a,n-1,disp)

		'''If its prime keep testing for the rest of the values of a'''
		if prime is True:
			testCounter = testCounter + 1
		else:
			break

		if disp:
			print ''
	if prime is True and testCounter == 20 :
		return (a,True)
	else :
		return (a,False)

