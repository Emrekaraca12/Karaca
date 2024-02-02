def returning_the_set_of_list(numbers : list) -> set:
    unique_elements = []
    for x in numbers:
        if x not in unique_elements:
            unique_elements.append(x)
    
    return unique_elements

"""
print(returning_the_set_of_list([1, 1, 2, 3, 5, 4, 7, 9, 5, 5]))
"""