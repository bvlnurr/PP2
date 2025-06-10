def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


for val in squares(2, 6):
    print(val)
