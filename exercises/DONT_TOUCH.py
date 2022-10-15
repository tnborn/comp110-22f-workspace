"""EX06 - Choose Your Own Adventure."""
__author__ = "730563181"

points: int = 0
player: str = ""


def greet() -> None:
    """Welcoming the player."""
    print("Welcome to CoinFlipper! You will try and guess what side of the coin will land face up as many times as you can in a row.")
    print("For every correct guess you will earn one point. Good Luck!")
    player_name = input("What is your name Player? ")
    return player_name


def cust_prod() -> None:
    """Guessing which side and adding points and guesses."""
    from random import randint
    global points
    coin = randint(1, 2)
    print(coin)
    heads = 0
    tails = 0
    guesses = 0
    i = True

    while i:
        player_input_side = input("Heads or Tails? (Type 'heads' or 'tails')? ")
        guesses += 1
        if coin == 1:
            side = "Heads"
            heads += 1
        elif coin == 2:
            side = "Tails"
            tails += 1
        if player_input_side.lower() == side.lower():
            print(f"Congratulations {player}! You guessed it correctly!")
            points += 1
            i = False
        else:
            print(f"Not quite. The coin flipped {side}.")
            i = False


def cust_funct(multiplier: int) -> int:
    """Raise the stakes."""
    print("To make the game more interesting, you can flip more coins.")
    print("The catch is, the coins all have to land on the same side.")
    print("If you guess correctly, your points will increase by the amount of coins flipped.")
    raise_stakes: str = input(f"{player}, are you willing to risk it all?")
    if raise_stakes.lower() == "yes":
        multiplier: int = input(f"How many coins would you like to flip {player}? ")
        cust_prod
        stakes = points ** multiplier
        print(stakes)
        return points
    elif raise_stakes.lower() == "no":
        cust_prod


def main() -> None:
    """Body of program welcoming and asking player to continue."""
    global points 
    global player
    global keep_playing

    points = 0

    player = greet()
    keep_playing = True

    while keep_playing:

        cust_prod()
        print(f"{player}, your current score is {points}.")
        player_input_play: str = input(f"Do you want to keep playing {player}? Type 'Yes' or 'No' ")

        if player_input_play.lower() == "yes":
            keep_playing = True
            store: int = int(input("Pick a number of coins to flip."))
            cust_funct(store)
        elif player_input_play.lower() == "no":
            keep_playing = False
        else:
            print("Invalid Response. Please type 'yes' or 'no'")


if __name__ == "__main__":
    main()