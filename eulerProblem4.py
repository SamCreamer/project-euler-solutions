## euler problem 4
## sam creamer

def reverseString(s):
	return s[::-1]

def isPalindrome(s):
	return s == reverseString(s)

largest = 0
n = 0

for i in range(100, 1000): #100 to 999
	for j in range(i, 1000): #i to 999
		n = i * j
		if(isPalindrome(str(n))):
			if n > largest:
				largest = n

print largest
