# euler problem 7
# sam creamer
# what is the 10001st prime?

def prime(n): # returns nth prime
	primes = [2]
	i = 3
	while (len(primes) < n):
		if all(i % j != 0 for j in primes):
			primes.append(i)
		i += 2
	return primes[-1]

answer = prime(10001)
print answer
