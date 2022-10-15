"""EX06 - Choose Your Own Adventure."""
__author__ = "730563181"

# third game, a random number and associated guess

def main() -> None:
    """Developing the main function of the game."""
    # Run stuff here in your main file
    
    # variable declaration
    global player
    global points
    global guesses
    global keep_playing 

    # call your greet function

    player = greet()
    points = custom_func_one()
    points = custom_func_two(points)
    keep_playing = True

    while keep_playing:

        print("Your point total is: ", points)

        # call your custom function, either one or two

        # e.g., 
        points = custom_func_two(points)
        player_input: bool = input(f"Do you want to keep playing {player}? Type 'yes' or 'no' ")  # also think this is illegal, will need this to be inside a function

        if player_input == "yes":
            keep_playing = True
        elif player_input == "no":
            keep_playing = False
        else: 
            print("Invalid response. You did not enter 'yes' or 'no'.")
            player_input: bool = input(f"Do you want to keep playing {player}? Type 'yes' or 'no'")  # likewise on line 80, this is illegal action

    # test random stuff here --> DO NOT need this when finished with the game. 
    print("Your player name is: ", player)
    print("Your point total is: ", points)

# Greet function 
def greet() -> str:
    """Naming the player."""
    print("Welcome to the game! You will guess a random number and see how many guesses it takes to get it right!")
    player_name: str = input("Player 1, what is your name? ")
    return player_name


# custom procedure 1
def custom_func_one() -> str:
    global points
    """Player choosing a number."""
    from random import randint
    Random_Guess  = randint(0,10)
    points=0
    i = True
    adventure_pts = 0
    guess_count = 0
    print(Random_Guess)
    while i:
        player_input = input(f"What number do you choose {player}? ") 
        intplayer_input=int(player_input)
        print(type(intplayer_input))
        while ( intplayer_input) != Random_Guess:
           adventure_pts +=1
           print( "Not quite. Try again? ")
           player_input = input("What number do you choose? ")  # really needs to address the player in this statement using the global variable player
           intplayer_input=int(player_input)
        print(f"Congraluations {player}!")
        print(f"Along the way you earned {adventure_pts} adventure points!")
        x=False
           
      


    # generate a random number 
    # this should use the random library

    # if statement here to compare the random number to the number chosen
     # probably an if statement :
    # to increment the points whethere or not they got it. and increment another variable called referring to the guesses
    
    adventure_pts += 1
    guess_count += 1
    return adventure_pts


# custom procedure 2
def custom_func_two(input1: int) -> int:
    """Choosing random number and incrementing guesses."""
    adventure_pts = input1

    # same thing as before, generate a rand number and increment the points / guesses 

    return adventure_pts



if __name__ == "__main__":
    main()