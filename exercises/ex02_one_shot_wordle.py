"""EX02 - One-shot Wordle."""
__author__ = "730563181"

secret_word: str = "python"
counter = len(secret_word)
wordle_guess: str = input(f"What is your {counter}-letter guess? ")

current = 0
result = ""
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

if secret_word == wordle_guess:
    if len(wordle_guess) >= len(secret_word):
        while current <= len(secret_word) - 1:
            if wordle_guess[current] == secret_word[current]:
                result = result + green_box
                current += 1
            else:
                if wordle_guess[current] in secret_word:
                    result = result + yellow_box
                    current += 1
                else:
                    result = result + white_box
                    current += 1
        print(result)
        print("Woo! You got it!")
else:
    if wordle_guess != secret_word:
        while len(wordle_guess) != counter:
            wordle_guess = input(f"That was not {counter} letters! Try again: ")
        else:
            len(wordle_guess) == counter
            if len(wordle_guess) >= len(secret_word):
                while current <= len(secret_word) - 1:
                    if wordle_guess[current] == secret_word[current]:
                        result = result + green_box
                        current += 1
                    else:
                        if wordle_guess[current] in secret_word:
                            result = result + yellow_box
                            current += 1
                        else:
                            result = result + white_box
                            current += 1
                print(result)
                print("Not quite. Play again soon!")