from functools import reduce

def multiply_list(numbers):
    
    result = reduce(lambda x, y: x * y, map(int, numbers))
    return result


numbers_list = ["2", "3", "4", "5"]
result = multiply_list(numbers_list)

print(f"The product of the numbers in the list {numbers_list} is: {result}")

