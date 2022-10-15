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
    player_name: str = input("What is your name Player?: ")
    return player_name


def main() -> None:
    """Making the coin run in order."""
    global points 
    global player
    global guesses
    global keep_playing
    global answer
    global coin1
    global coin2

    player = greet()

    while keep_playing is True:
        options: str = input("Would you... \n (a) Like to begin? \n (b) Have the introduction repeated? \n (c) Quit Coins? \n (Type 'A', 'B', or 'C'): ")
        invalid_YN
        if options == "A".lower():
            sides_one()
        elif options == "B".lower():
            greet()
        elif options == "C".lower():
            print("Shutting down. Goodbye.")
            keep_playing = False


def play_again() -> bool:
    global keep_playing
    global answer
    while keep_playing is True:
        print(f"You currently have {points} point(s)")
        answer = input(f"Would you like to continue {player}? (Type 'Yes' or 'No'): ?")
        invalid_YN()
        if answer is True or "Yes".lower():
            sides_one()
        elif answer is False or "No".lower():
            bye: str = input("Are you sure you want to quit? (Type 'Yes' or 'No'): ")
            invalid_YN
            if bye == True or "Yes".lower():
                print(f"Thank you for playing {player}! \n You finished with {points} point(s) in {guesses} guess(es)!")
            else:
                sides_one()


def play_again_two() -> bool:
    global keep_playing
    global answer
    while keep_playing is True:
        print(f"You currently have {points} point(s)")
        answer = input(f"!Would you like to continue {player}? (Type 'Yes' or 'No'): ")
        invalid_YN_two()
        if answer == True or "Yes".lower():
            stakes_again()
            if answer is True or "Yes".lower():
                sides_two()
            else:
                sides_three()


def sides_one() -> str:
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
            print(coin1)
            answer = input("!Will the coin land on Heads or Tails? (Type 'Heads' or 'Tails'): ")
            invalid_HT()
            if coin1 == 1:
                if answer == "Heads".lower():
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
                if answer == "Tails".lower():
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


def sides_two() -> str:
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
            print(coin1)
            if coin1 == 1 or 2:
                answer = input("!!Will the coin land on Heads or Tails? (Type 'Heads' or 'Tails'): ")
                if answer == "Heads".lower() or "Tails".lower():
                    guesses += 1
                    print(f"Congratulations {player}! You guessed correctly!")
                    coin2 = randint(1, 2)
                    print(coin2)
                    answer = input("Will the second coin land on Heads or Tails? (Type 'Heads' or 'Tails'): ")
                    invalid_HT()
                    if coin2 == 1 or 2:
                        if answer == "Heads".lower() or "Tails".lower():
                            print(f"Congratulations {player}! You guessed correctly and doubled your points!")
                            points = points * 2
                            play_again_two()
                            i = False
                        else:
                            invalid_HT
                else:
                    invalid_HT()
                    if answer == True:
                        incorrect()
                        i = False
                        keep_playing = False


def sides_three() -> str:
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
            print(coin1)
            answer = input("Will the coin land on Heads or Tails? (Type 'Heads' or 'Tails'): ")
            invalid_HT()
            if coin1 == 1:
                if answer == "Heads".lower():
                    guesses += 1
                    print(f"Congratulations {player}! You guessed correctly!")
                    points += 1
                    play_again_two()
                    i = False
                else:
                    incorrect()
                    i = False
                    keep_playing = False
            if coin1 == 2:
                if answer == "Tails".lower():
                    guesses += 1
                    print(f"Congratulations {player}! You guessed correctly!")
                    points += 1
                    play_again_two()
                    i = False
                else:
                    incorrect()
                    i = False
                    keep_playing = False


def invalid_YN() -> bool:
    global keep_playing
    global answer
    while keep_playing is True:
        if answer == "Yes".lower() or "No".lower():
            return answer
        else:
            while answer != "Yes".lower() or "No".lower():
                answer = input("Invalid Response. Please respond with 'Yes' or 'No' or game will shut down: ")
                if answer == "Yes".lower() or "No".lower():
                    keep_playing == True
                    return answer
                else:
                    keep_playing == False


def invalid_YN_two() -> bool:
    global keep_playing
    global answer
    while keep_playing is True:
        if answer == "Yes".lower() or "No".lower():
            return answer
        else:
            while answer != "Yes".lower() or "No".lower():
                answer = input("Invalid Response. Please respond with 'Yes' or 'No' or game will shut down: ")
                if answer == "Yes".lower() or "No".lower():
                    keep_playing == True
                    return answer
                else:
                    keep_playing == False


def invalid_HT() -> bool:
    global keep_playing
    global answer
    while keep_playing is True:
        if answer == "Heads".lower() or "Tails".lower():
            return answer
        else:
            while answer != "Heads".lower() or "Tails".lower():
                answer = input("Invalid Response. Please respond with 'Heads' or 'Tails' or game will shut down: ")
                if answer == "Heads".lower() or "Tails".lower():
                    keep_playing == True
                    return answer
                else:
                    keep_playing == False


def incorrect() -> bool:
    global keep_playing
    global player
    while keep_playing is True:
        print(f" Sorry, that wasn't the correct answer! \n Thank you for playing {player}! Try again soon! \n You finished with {points} point(s) in {guesses} guess(es).")

        keep_playing = False


def stakes() -> str:
    global answer
    print(f"{COIN_EMOJI}  Do you want to try and earn more points? {COIN_EMOJI}")
    print("You can earn double your current points if you guess the sides of two coins correctly in a row.")
    print("However, if you get one wrong..game over.")
    answer = input(f"Are you willing to take the risk {player}? (Type 'Yes' or 'No'): ")
    invalid_YN
    if answer == True:
        sides_two()
    else:
        print("Okay! This next guess is only worth 1 point.")
        sides_three()


def stakes_again() -> str:
    global answer
    answer = input(f"{player}, do you want to raise the stakes and potentially double your points? (Type 'Yes' or 'No'): ")
    invalid_YN_two


if __name__ == "__main__":
    main()