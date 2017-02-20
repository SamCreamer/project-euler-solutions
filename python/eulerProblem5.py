## euler problem 5
## sam creamer
# this works pretty fast... i'm sure there's a better algorithm

i = 2520 # start here

def evenlyDivisible(n, min, max): # takes n, min, max, sees if n is evenly divisible by the numbers betwee min and max
	for i in range(min, max + 1):
		if n % i != 0:
			return False
	return True

while (True):
	if (evenlyDivisible(i, 1, 20)):
		print i
		break
	else:
		i += 10 #only have to check every 10, not sure if we can increment more...

