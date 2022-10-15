"""EX06 - Choose Your Own Adventure."""
__author__ = "730563181"


points: int = 0
player: str = ""
COIN_EMOJI: str = "\U0001fA99"
guesses: int = 0
keep_playing = True
answer: str = ""
coin1: int = 0
coin2: int = 0


def greet() -> None:
    """Welcoming the player."""
    global player
    print(f"Welcome to Coins! {COIN_EMOJI}  You will try and guess what side of the coin will land face up as many times as you can in a row.")
    print("For every correct guess you will earn one point. Good Luck!")
    player = input("What is your name Player?: ")


def main() -> None:
    """Making the coin run in order."""
    global points 
    global player
    global guesses
    global keep_playing
    global answer
    global coin1
    global coin2

    greet()

    while keep_playing is True:
        options: str = input("Would you... \n (A) Like to begin? \n (B) Have the introduction repeated? \n (C) Quit Coins? \n (Type 'A', 'B', or 'C'): ")
        invalid_YN
        if options == "A":
            sides_one()
        elif options == "B":
            greet()
        elif options == "C":
            print("Shutting down. Goodbye.")
            keep_playing = False
    
    try_again()


def play_again() -> None:
    """Asking the player if they want to play again."""
    global keep_playing
    global answer
    while keep_playing is True:
        print(f"You currently have {points} point(s)")
        answer = input(f"Would you like to continue {player}? (Type 'Yes' or 'No'): ?")
        invalid_YN()
        keep_playing is False
        if answer is True or "Yes":
            sides_one()
        elif answer is False or "No":
            bye: str = input("Are you sure you want to quit? (Type 'Yes' or 'No'): ")
            invalid_YN
            if bye is True or "Yes":
                print(f"Thank you for playing {player}! \n You finished with {points} point(s) in {guesses} guess(es)!")
                try_again()
                keep_playing is False
            else:
                sides_one()


def play_again_two() -> None:
    """Asking again if the player if they would like to play again."""
    global keep_playing
    global answer
    global player
    global guesses
    global points
    if keep_playing is True:
        print(f"You currently have {points} point(s)")
        answer = input(f"Would you like to continue {player}? (Type 'Yes' or 'No'): ")
        invalid_YN_two()
        if answer == "Yes":
            stakes_again()
            if answer == "Yes":
                sides_two()
                keep_playing is False
            else:
                sides_three()
                keep_playing is False
        elif answer == "No":
            print(f"Thank you for playing {player}! \n You finished with {points} point(s) in {guesses} guess(es)!")
            keep_playing is False


def sides_one() -> None:
    """Asking the player what side of the coin they think will land face up."""
    from random import randint
    global keep_playing
    global answer
    global points
    global guesses
    global coin1
    global player
    i = True
    while keep_playing is True:
        while i is True:
            coin1 = randint(1, 2)
            answer = input("Will the coin land on Heads or Tails? (Type 'Heads' or 'Tails'): ")
            invalid_HT()
            if coin1 == 1:
                if answer == "Heads":
                    guesses += 1
                    print(f"Congratulations {player}! You guessed correctly!")
                    points += 1
                    stakes()
                    i = False
                    keep_playing = False
                else:
                    incorrect()
                    i = False
                    keep_playing = False
            if coin1 == 2:
                if answer == "Tails":
                    guesses += 1
                    print(f"Congratulations {player}! You guessed correctly!")
                    points += 1
                    stakes()
                    i = False
                    keep_playing = False
                else:
                    incorrect()
                    i = False
                    keep_playing = False


def sides_two() -> None:
    """Another function asking the player what side of the coin will land face up."""
    from random import randint
    global keep_playing
    global points
    global answer
    global guesses
    global coin1
    global coin2
    global player
    i = True
    while keep_playing is True:
        while i is True:
            coin1 = randint(1, 2)
            if coin1 == 1 or 2:
                answer = input("Will the coin land on Heads or Tails? (Type 'Heads' or 'Tails'): ")
                if answer == "Heads" or "Tails":
                    guesses += 1
                    print(f"Congratulations {player}! You guessed correctly!")
                    coin2 = randint(1, 2)
                    answer = input("Will the second coin land on Heads or Tails? (Type 'Heads' or 'Tails'): ")
                    invalid_HT()
                    if coin2 == 1 or 2:
                        if answer == "Heads" or "Tails":
                            print(f"Congratulations {player}! You guessed correctly and doubled your points!")
                            points = points * 2
                            play_again_two()
                            keep_playing is False
                            i = False
                        else:
                            invalid_HT
                else:
                    invalid_HT()
                    if answer is True:
                        incorrect()
                        i = False
                        keep_playing = False


def sides_three() -> None:
    """Another function asking the player what side they think will land face up."""
    from random import randint
    global keep_playing
    global answer
    global points
    global guesses
    global coin1
    global player
    i = True
    while keep_playing is True:
        while i is True:
            coin1 = randint(1, 2)
            answer = input("Will the coin land on Heads or Tails? (Type 'Heads' or 'Tails'): ")
            invalid_HT()
            if coin1 == 1:
                if answer == "Heads":
                    guesses += 1
                    print(f"Congratulations {player}! You guessed correctly!")
                    points += 1
                    play_again_two()
                    keep_playing is False
                    i = False
                else:
                    incorrect()
                    i = False
                    keep_playing = False
            if coin1 == 2:
                if answer == "Tails":
                    guesses += 1
                    print(f"Congratulations {player}! You guessed correctly!")
                    points += 1
                    play_again_two()
                    keep_playing is False
                    i = False
                else:
                    incorrect()
                    i = False
                    keep_playing = False


def invalid_YN() -> str:
    """Making sure player only enters 'Yes' or 'No'."""
    global keep_playing
    global answer
    while keep_playing is True:
        if answer == "Yes" or "No":
            return answer
        else:
            while answer != "Yes" or "No":
                answer = input("Invalid Response. Please respond with 'Yes' or 'No' or game will shut down: ")
                if answer == "Yes" or "No":
                    keep_playing is True
                    return answer
                else:
                    keep_playing is False
    return answer


def invalid_YN_two() -> str:
    """Another function to make sure the player only enters 'Yes' or 'No'."""
    global keep_playing
    global answer
    while keep_playing is True:
        if answer == "Yes" or "No":
            return answer
        else:
            while answer != "Yes" or "No":
                answer = input("Invalid Response. Please respond with 'Yes' or 'No' or game will shut down: ")
                if answer == "Yes" or "No":
                    return answer
                else:
                    keep_playing is False
                    return answer
    return answer


def invalid_HT() -> str:
    """A function that runs to make sure the player enters only 'Heads' or 'Tails'."""
    global keep_playing
    global answer
    while keep_playing is True:
        if answer == "Heads" or "Tails":
            return answer
        else:
            while answer != "Heads" or "Tails":
                answer = input("Invalid Response. Please respond with 'Heads' or 'Tails' or game will shut down: ")
                if answer == "Heads" or "Tails":
                    keep_playing is True
                    return answer
                else:
                    keep_playing is False
                    return answer
    return answer


def incorrect() -> None:
    """Running a function to say the input was incorrect."""
    global keep_playing
    global player
    while keep_playing is True:
        print(f" Sorry, that wasn't the correct answer! \n Thank you for playing {player}! Try again soon! \n You finished with {points} point(s) in {guesses} guess(es).")
        try_again()
        keep_playing = False


def stakes() -> str:
    """Determining if player wants to do double or nothing."""
    global answer
    print(f"{COIN_EMOJI}  Do you want to try and earn more points? {COIN_EMOJI}")
    print("You can earn double your current points if you guess the sides of two coins correctly in a row.")
    print("However, if you get one wrong..game over.")
    answer = input(f"Are you willing to take the risk {player}? (Type 'Yes' or 'No'): ")
    invalid_YN
    if answer == "Yes":
        sides_two()
        return answer
    else:
        print("Okay! This next guess is only worth 1 point.")
        sides_three()
        return answer


def stakes_again() -> str:
    """Determining if player wants to risk their points again."""
    global answer
    answer = input(f"{player}, do you want to raise the stakes and potentially double your points? (Enter '2' for Yes or '1' for No): ")
    while keep_playing is True:
        if answer == "2" or "1":
            return answer
        else:
            while answer != "2" or "1":
                answer = input("Invalid Response. Please respond with 'Yes' or 'No' or game will shut down: ")
                if answer == "2" or "1":
                    return answer
                else:
                    keep_playing is False
    return answer


def try_again() -> str:
    """Asking the player if they would like to try again."""
    reload: str = input(f"Would you like to play again {player}? (Type 'Yes' or 'No'): ")
    while keep_playing is True:
        if reload == "Yes":
            greet()
        elif reload == "No":
            print("Thanks for playing! \n Game Over.")
        else:
            reload = input("Invalid Input. Please enter 'Yes' or 'No' or game will shut down: ")
            if reload == "Yes":
                greet()
            else:
                keep_playing is False
    return reload


if __name__ == "__main__":
    main()