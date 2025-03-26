#importing "random" library

game_choice = ["rock", "paper", "scissors"]
correction = ["rock", "paper", "scissors"]

def de_playerchoice2():
    player_choice = input("Choose rock, paper or scissors:" )
    while True:
        if player_choice not in correction:
            print("Inncorect choice. Try again")
            de_playerchoice2()
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

        elif player_choice == game_choice:
            print("Tie. Try again")
            de_playerchoice2()
            

de_playerchoice2()