def count_upper_lower(string):
    # Calculate the number of uppercase and lowercase letters
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    
    return upper_count, lower_count

# Example usage
input_string = "exapmle STRING"
upper, lower = count_upper_lower(input_string)

print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")


