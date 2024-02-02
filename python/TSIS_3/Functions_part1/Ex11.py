def is_word_pallindrom(word : str) -> str:
    return f"Yes, the word {word} is pallindrom" if word.lower() == word.lower()[::-1] else f"No, the word {word} is not pallindrom"

"""
print(is_word_pallindrom("Pallindrom"))
print(is_word_pallindrom("madam"))
print(is_word_pallindrom("Level"))
"""