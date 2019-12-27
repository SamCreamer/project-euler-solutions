from itertools import permutations

perms = list(permutations('0123456789'))

perms.sort()
print(''.join(perms[999999]))
