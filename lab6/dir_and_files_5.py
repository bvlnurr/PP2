data = ['Apple', 'Banana', 'Cherry']

with open('fruits.txt', 'w') as file:
    for item in data:
        file.write(item + '\n')