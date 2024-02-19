def split_by_uppercase (s : str) -> list:
    import re

    return re.findall("[A-Z][^A-Z]*", s)

print(split_by_uppercase("auydbfKapsidjKidL"))
f = open("row.txt", "r")
txt = f.read()
print(split_by_uppercase(txt))