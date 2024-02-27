def is_pallindrom(some_string : str) -> bool:
    return some_string.lower() == ''.join((reversed(some_string))).lower()

print(is_pallindrom("Amana"))
print(is_pallindrom("Lol"))
print(is_pallindrom("lalalal"))




    