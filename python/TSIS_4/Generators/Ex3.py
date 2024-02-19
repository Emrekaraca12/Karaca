def generate_nums(N=int(input())):
    i = 0
    while i <= N:
        if i % 3 == 0 and i % 4 == 0:
            yield i
        i += 1

some_object = generate_nums()
print(list(some_object))
