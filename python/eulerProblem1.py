## euler problem 1
## sam creamer

m3 = 0
m5 = 0

for i in range(1, 1000): #1000 is exclusive, so goes from 1 to 999, question asks for numbers below 1000
	if (i % 3 == 0):
		m3 += i
	elif (i % 5 == 0):
		m5 += i

print m5 + m3