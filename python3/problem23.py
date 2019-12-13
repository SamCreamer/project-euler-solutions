def proper_divisors(n):
    divs = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divs.append(i)
    return divs


def abundant(n):
    """
    Returns True if the number is abundant. The definition of abundant is:
    A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
    :param n:
    :return:
    """
    return sum(proper_divisors(n)) > n


abundants = []

for i in range(12, 28124):
    if abundant(i):
        abundants.append(i)

print(abundants)
