def find_lowercase_with_underscore(s : str):
    import re

    subRE = r"[a-z]+_[a-z]+"

    if re.match(subRE, s):
        return "Match Found"
    else:
        return "Not Found"
    
f = open("row.txt", "r")
txt = f.read()
print(find_lowercase_with_underscore(txt))