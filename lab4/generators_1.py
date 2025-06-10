def generate_squares(n):
    for i in range(n + 1):
        yield i * i


for square in generate_squares(5):
    print(square)
