def snake_case_to_CamelCase (s : str) -> str:
    import re

    listOfStrings = re.split(r"\_", s)

    return "".join([x.capitalize() for x in listOfStrings])

print(snake_case_to_CamelCase("snake_case"))
f = open("row.txt", "r")
txt = f.read()
print(snake_case_to_CamelCase(txt))