def squares(a=int(input("a = ")), b=int(input("b = "))):
    for i in range(a, b):
        yield i * i

for i in list(squares()):
    print(i)