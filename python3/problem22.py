import re

nf = open('data/p022_names.txt', 'rb')
names = [re.sub(r'[^\w\s]','', n).replace('b', '') for n in str(nf.read()).split(',')]
nf.close()
names.sort()

result = 0

for i in range(len(names)):
    number = i + 1
    name_score = 0
    for letter in names[i]:
        name_score += ord(letter.lower()) - 96
    result += number * name_score

print(result)
