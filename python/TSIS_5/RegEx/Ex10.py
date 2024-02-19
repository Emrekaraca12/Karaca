def camelCaseto_snake_case(s : str ) -> str:
    import re

    listOfStrings = re.findall("[A-Z][^A-Z]*", s)
    answer = f"{listOfStrings[0].lower()}"
    for i in listOfStrings[1::]:
        answer += '_' + i.lower()
    return answer

print(camelCaseto_snake_case("LetMeThink"))
f = open("row.txt", "r")
txt = f.read()
print(camelCaseto_snake_case(txt))