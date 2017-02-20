## euler problem 2
## sam creamer
## gets the answer in approx 10 seconds, not sure if there is a better way of doing this

def fib(n): ## gets nth fib, classic algorithm
	if n == 0 or n == 1: 
		return n
	else: 
		return fib(n-1) + fib(n - 2)


fibSum = 0 #sum for the final answer
fibN = 1 #index of current fib
fibC = fib(fibN) #fibC means fib current... bad name I know

while (fibC < 4000000):
	if (fibC % 2 == 0):
		fibSum += fibC
	fibN += 1
	fibC = fib(fibN)

print fibSum
