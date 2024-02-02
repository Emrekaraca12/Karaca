def filter_prime(numbers : str) -> list:
    splitted_list = [int(x) for x in numbers.split()]
    is_prime = lambda n: all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
    return list(filter(is_prime, splitted_list))

print("1 2 3 4 5 6 21 18 19")