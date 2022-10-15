"""EX03 - Wordle."""
__author__ = "730563181"


def contains_char(searched_through: str, single_character: str) -> bool: 
    """Determining if the secret word has the character anywhere within it."""
    index = 0
    assert len(single_character) == 1
    while index < len(searched_through):
        if searched_through[index] == single_character:
            return True
        else:
            index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Making white, green, or yellow boxes appear if the character is in the guess."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    current = 0
    emoji: str = ""

    # test letters
    while current < len(secret):
        if (contains_char(secret, guess[current])): 
            if (guess[current] == secret[current]):
                emoji += GREEN_BOX
                # assign green

            else: 
                emoji += YELLOW_BOX
                # assign yellow

        else:         
            # assign white
            emoji += WHITE_BOX
        current += 1

    return (emoji) 
    # return emoji


def input_guess(secret_len: int) -> str:
    """Secret_len = len(secret)."""
    wordle_guess: str = ""

    wordle_guess = input(f"Enter a {secret_len} character word? ")
    while (len(wordle_guess) != secret_len):
        if len(wordle_guess) == secret_len:
            print(wordle_guess)
        else:
            print(f"That wasn't {secret_len} chars! Try again:")
    return (wordle_guess) 


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    turnString = str(turn)
    secret_word: str = "python"
    secret_len = len(secret_word)
    guess: str = ""

    # while loop through the turns
    while (turn <= 6):
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(secret_len)
        emojified(guess, secret_word)
        if (guess == secret_word):
            print("You won in ", turnString, "/6 turns!")
            turn = 7
        else:
            turn += 1
            turnString = str(turn)
            if (turn > 6):
                print("X/6 - Sorry try again tomorrow!")


if __name__ == "__main__":
    main()
