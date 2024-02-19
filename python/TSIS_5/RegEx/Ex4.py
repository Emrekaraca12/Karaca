def find_uppercase_with_lowercase(s : str):
    import re

    subRE = r"[A-Z][a-z]+"

    if re.match(subRE, s):
        return "Match Found"
    else:
        return "Not Found"

f = open("row.txt", "r")
txt = f.read()
print(find_uppercase_with_lowercase(txt))