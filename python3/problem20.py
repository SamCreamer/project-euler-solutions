import math

big_num = math.factorial(100)
result = 0

for i in str(big_num):
    result += int(i)

print(result)
