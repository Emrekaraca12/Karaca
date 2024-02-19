def find_ab_in_string (s : str) -> str:
    import re

    subRE = r"ab{2,3}"

    if re.match(subRE, s):
        return "Match found"
    else:
        return "Not Found"
    

f = open("row.txt", "r")
txt = f.read()
print(find_ab_in_string(txt))