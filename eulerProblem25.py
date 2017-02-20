##### PROJECT EULER PROBLEM
from math import *
import decimal

def fib2(n):
	n = decimal.Decimal(n)
	if n == 0: return 0
	elif n == 1: return 1
	else: return fib2(n-1) + fib2(n - 2)

def fib(n): # good fib method
	n = decimal.Decimal(n)
	s = decimal.Decimal(sqrt(5))
	return decimal.Decimal(((1+s**n-(1-s**n)/(2**n*s))))

for i in range(0, 10000): #assuming its in the first 10000 fibs
	# print fib2(i)
	print fib2(i)
	if (fib2(i) > (decimal.Decimal(10)**decimal.Decimal(999))):
		
		print i
		break
	




	