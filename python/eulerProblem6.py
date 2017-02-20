# euler problem 6
# sam creamer
# sum of squares difference

def sumOfSquares(min, max):
	sum = 0
	for n in range(min, max + 1):
		sum += n**2
	return sum

def squareOfSum(min, max):
	sum = 0
	for n in range(min, max + 1):
		sum += n
	return sum**2

answer = squareOfSum(1, 100) - sumOfSquares(1, 100)
print answer
