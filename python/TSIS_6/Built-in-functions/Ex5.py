def is_all_elems_true(some_tuple : tuple):
    from functools import reduce

    return reduce(lambda x, y : y * bool(x), some_tuple, 1)

some_tuple = (1, 1, 0, 1)
some_tuple_1 = (1, 1, 1, 1)

print(is_all_elems_true(some_tuple))
print(is_all_elems_true(some_tuple_1))