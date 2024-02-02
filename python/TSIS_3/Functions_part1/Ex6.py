def reversed_word_order(some_string : str) -> str:
    return ' '.join([(x) for x in some_string.split()][::-1])