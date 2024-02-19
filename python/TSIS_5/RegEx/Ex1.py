def find_ab_in_RE(s : str) -> str:
    import re

    subRE = r"ab*"

    if re.match(subRE, s):
        return "Match found"
    else:
        return "Not found"
    
f = open("row.txt", "r")
txt = f.read()
print(find_ab_in_RE(txt))