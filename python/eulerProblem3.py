## euler problem 3
## sam creamer
## finishes very quickly so I assume this algorithm is okay

import math

def isPrime(n): ## brute force prime method, probably not fastest algorithm
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(math.sqrt(n))): # only need to go up the square root of n to test prime
		if n % i == 0:
			return False
	return True

number = 600851475143 
largestPrimeFactor = 0

for i in range(1, int(math.sqrt(number))): # again, dont know if there is a better algorithm than this
	if number % i == 0:
		if (isPrime(i)):
			largestPrimeFactor = i

print largestPrimeFactor

