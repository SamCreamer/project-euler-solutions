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


def has_array_two_candidates(A, sum_s):
    l = 0
    r = len(A) - 1

    while l < r:
        if (A[l] + A[r] == sum_s):
            return 1
        elif (A[l] + A[r] < sum_s):
            l += 1
        else:
            r -= 1
    return 0


abundants = []

for i in range(12, 28124):
    if abundant(i):
        abundants.append(i)

abundants.sort()
non_sum = 0

for i in range(24, 28123 * 2 + 1):
    for j in abundants:
        if j >= i:
            continue
        for k in abundants:
            if k >= i:
                continue
            jk = j + k
            if jk == i:
                break
            elif jk > i:
                non_sum += jk
                break
