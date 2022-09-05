"""EX02 - One-shot Wordle."""
__author__ = "730563181"


secret_word: int = "python"
counter = len(secret_word)
wordle_guess: str = input(f"What is your {counter}-letter guess? ")


while len(wordle_guess) != counter:
        new_guess: str = input("That was not 6 letters! Try again: ")
        if len(new_guess) == counter:
            if new_guess != secret_word:
                print("Not quite. Play again soon!")
                exit()
            else:
                new_guess == secret_word
                print("Woo! You got it!")
                exit()
else:
    if len(wordle_guess) == counter:
        if wordle_guess != secret_word:
                print("Not quite. Play again soon!")
                exit()
        if wordle_guess == secret_word:
            print("Woo! You got it!")
            exit()

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"