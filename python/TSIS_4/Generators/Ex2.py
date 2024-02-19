def generate_evens(N=int(input())):
    i = 0
    while i <= N:
        if not i % 2:
            yield i
        i += 1

def object_return() -> str:
    some_object = generate_evens()
    result = ", ".join([str(i) for i in list(some_object)])
    return result

print(object_return())