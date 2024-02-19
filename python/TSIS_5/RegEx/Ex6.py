def replace_with_colon (s : str) -> str:
    import re

    symbols = [r'\s', r'\.', r',']

    for i in symbols:
        s = re.sub(i, ':', s)

    return s

print(replace_with_colon("I love cookies, espeaccially chocolate ones."))
f = open("row.txt", "r")
txt = f.read()
print(replace_with_colon(txt))