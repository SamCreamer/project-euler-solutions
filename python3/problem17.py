from num2words import num2words

counter = 0

for i in range(1, 1001):
    counter += len(num2words(i).replace('-', '').replace(' ', ''))

print(counter)
