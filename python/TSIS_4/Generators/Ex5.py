def generate_squares(N = int(input("n ="))):
    while N >= 0:
        yield N
        N -= 1