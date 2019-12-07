import num2words

counter = 0

for i in range(1, 1001):
    print(num2words(i))
    counter += len(num2words(i))
