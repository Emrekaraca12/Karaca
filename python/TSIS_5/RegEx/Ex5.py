def a_followed_by_anything_and_b(s : str):
    import re

    subRE = r"a.*b$"

    if re.match(subRE, s):
        return "Match Found"
    else:
        return "Not Found"
    
f = open("row.txt", "r")
txt = f.read()
print(a_followed_by_anything_and_b(txt))