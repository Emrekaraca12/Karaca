def spy_game(nums : list) -> bool:
    str_version_of_nums = "".join([str(x) for x in nums])
    return False if str_version_of_nums.find("007") == -1 else True

"""
print(spy_game([1, 2, 3, 0, 0, 7, 7]))
print(spy_game([1, 2, 3, 0, 0, 4, 7]))
print(spy_game([1, 2]))
"""