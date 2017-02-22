#euler10
#sam creamer
# works quite fast

import math

def isPrime(n): ## brute force prime method, probably not fastest algorithm
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(math.sqrt(n)) + 1): # only need to go up the square root of n to test prime
		if n % i == 0:
			return False
	return True

sumP = 0 # 2 is prime, we wont test it

for i in xrange(1, 2000000, 2):
	if (isPrime2(i)):
		sumP += i

print sumP


