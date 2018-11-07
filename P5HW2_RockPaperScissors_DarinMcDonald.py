# Player against the computer in Rock Paper Scissors
# 10/30/18
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Darin McDonald
#


# Set a variable for a while loop and a starting variable for the cpu choice.

# Get input from the user and use if statments to convert the entered string to
# a number in order where Rock is 1, so on and so forth.

# If the player enters anything besides Rock Paper or Scissors give an error

# A long as the player and cpu choice numbers do not match give different
# messages based on the rules of Rock Paper Scissors also break the loop

# If both player and cpu choice are = there is a draw and another match needs to
# be played

import random

def main():
    retry = True
    cpu_choice = random.randint(1,3)
    while retry == True: 
        choice = input("Please enter Rock, Paper, or Scissors: ")
        if choice == 'Rock':
            player_choice = 1
        elif choice == 'Paper':
            player_choice = 2
        elif choice == 'Scissors':
            player_choice = 3
        else:
           print("Please enter a valid move!")
           player_choice = 0
 
        if cpu_choice != player_choice and player_choice!= 0:
            if player_choice == 1:
                if cpu_choice == 3:
                    print("Player: Rock \nCPU: Scissors \nYou Win! Congrats!")
                else:
                    print("Player: Rock \nCPU: Paper \nYou Lose... Better luck next time!")
            if player_choice == 2:
                if cpu_choice == 1:
                    print("Player: Paper \nCPU: Rock \nYou Win! Congrats!")
                else:
                    print("Player: Paper \nCPU: Scissors \nYou Lose... Better luck next time!")
            if player_choice == 3:
                if cpu_choice == 2:
                    print("Player: Scissors \nCPU: Paper \nYou Win! Congrats!")
                else:
                    print("Player: Scissors \nCPU: Rock \nYou Lose... Better luck next time!")
            retry = False
        else:
            if player_choice!= 0:
                print("Player:",choice," \nCPU: ",choice," \nIt's a tie! Go again!")
                cpu_choice = random.randint(1,3)
                print()

main()
    
