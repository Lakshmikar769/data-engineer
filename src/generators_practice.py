def square_gen(n):
    for i in range(n):
        yield i ** 2

squares = square_gen(5)
for square in squares:
    print(square)