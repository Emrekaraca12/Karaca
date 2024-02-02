def Guess_the_number() -> None:
    import random
    name = input("Hello! What is your name?\n")
    guess_of_user = int(input(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.\n"))

    number = random.choice(range(1, 21))
    number_of_attempts = 0

    while True:
        if guess_of_user == number:
            print(f"Good job, {name}! You guessed my number in {number_of_attempts} guesses!")
            break
        
        if guess_of_user > number:
            guess_of_user = int(input("Your guess is too high.\nTake guess.\n"))
            number_of_attempts += 1
        else:
            guess_of_user = int(input("Your guess is too low.\nTake guess.\n"))
            number_of_attempts += 1
        
    return None

"""
Guess_the_number()
"""