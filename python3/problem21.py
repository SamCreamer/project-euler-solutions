import math

def sum_of_divisors(n):
    divs = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divs.append(i)
    return sum(divs)

checked = []
result = 0

for i in range(1, 10001):
    if i in checked:
        continue
    fs = sum_of_divisors(i)
    if i == fs:
        continue
    if i == sum_of_divisors(fs):
        result += i
        result += fs
    checked.append(fs)
    checked.append(i)

print(result)
