def generate_squares(N):
    i = 0
    while i <= N:
        yield i * i
        i += 1

some_object = generate_squares(12)
print(list(some_object))