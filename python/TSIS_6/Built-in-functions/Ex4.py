def after_specific_milisecond_square_root(integer : int, miliseconds : int) -> str:
    from time import sleep
    from math import sqrt
    sleep(miliseconds / 1000)
    print(f"Square root of {integer} after {miliseconds} miliseconds is {sqrt(integer)}")

after_specific_milisecond_square_root(25100, 2123)