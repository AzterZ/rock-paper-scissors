# importing "random" library

# list of items that PC can choose
game_choice = ["rock", "paper", "scissors"]
# additional one. later to check if player chose correct one
correction = ["rock", "paper", "scissors"]

#defining function of "de_playerchoice2()", where player chooses his pick
def de_playerchoice2():
    # player chooses his pick
    player_choice = input("Choose rock, paper or scissors:" )
    # this is where it gets messy, and it's probably here where the code screwes up. also 
    # "#?" is comment where I'm not 100% sure if I'm right about what code is doing or not lol
    while True:
       # checking if player did chose the right pick
        if player_choice not in correction:
            print("Inncorect choice. Try again")
            de_playerchoice2()
            #? if he chose, the compare player's pick to PC's pick
        elif player_choice == "rock" and game_choice == "paper":
            print("You lost! Computer chose", game_choice)
            break

        elif player_choice == "rock" and game_choice == "scissors":
            print("You won! Computer chose", game_choice)
            break

        elif player_choice == "paper" and game_choice == "scissors":
            print("You lost! Computer chose", game_choice)
            break
            
        elif player_choice == "paper" and game_choice == "rock":
            print("You won! Computer chose", game_choice)
            break
            
        elif player_choice == "scissors" and game_choice == "rock":
            print("You lost! Computer chose", game_choice)
            break
            
        elif player_choice == "scissors" and game_choice == "paper":
            print("You won! Computer chose", game_choice)
            break

        #? if there's a tie, then replay the game
        elif player_choice == game_choice:
            print("Tie. Try again")
            de_playerchoice2()
            
# starting the function "de_playerchoice2()"
de_playerchoice2()
