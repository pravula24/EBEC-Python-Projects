"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 3/19/2022

Description:
    This program prompts the user to pick between rock,
    paper, and scissors, and then randomly makes the
    computer draw one of the three, and tells the user
    if they have won, lost, or tied.

Contributors:

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
#Imports random int generator
from random import randint

"""Write new functions below this line (starting with unit 4)."""
#Dtermines computer choice
def get_computer_choice():
    num = randint(1,3)
    if num == 1:
        choice = 'rock'
    if num == 2:
        choice = 'paper'
    if num == 3:
        choice = 'scissors'
    return choice

#Determines player choice
def get_player_choice():
    choice = str(input("Choose rock, paper, or scissors: "))

    while choice != 'rock' and choice != 'paper' and choice != 'scissors':
        print("You made an invalid choice. Please try again.")
        choice = str(input("Choose rock, paper, or scissors: "))

    return choice

#Determines winner of round
def get_winner(comp, user):
    if(comp == 'rock' and user == 'scissors'):
        winner = 'computer'
    if(comp == 'rock' and user == 'rock'):
        winner = 'tie'
    if(comp == 'rock' and user == 'paper'):
        winner = 'player'
    if(comp == 'paper' and user == 'scissors'):
        winner = 'player'
    if(comp == 'paper' and user == 'rock'):
        winner = 'computer'
    if(comp == 'paper' and user == 'paper'):
        winner = 'tie'
    if(comp == 'scissors' and user == 'scissors'):
        winner = 'tie'
    if(comp == 'scissors' and user == 'rock'):
        winner = 'player'
    if(comp == 'scissors' and user == 'paper'):
        winner = 'computer'
    return winner



def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Loop structure to repeat if tie is made
    looper = True
    while(looper):
        #Gets computer and user choices
        computer_hand = get_computer_choice()
        user_hand = get_player_choice()

        win = get_winner(computer_hand, user_hand)
        print(f"  The computer chose {computer_hand}, and you chose {user_hand}.")

        #Determines output based on winner of round
        if win == 'computer':
            print(f"  {computer_hand} beats {user_hand}")
            print("  You lost.  Better luck next time.")
            print("Thanks for playing.")
            looper = False
        if win == 'player':
            print(f"  {user_hand} beats {computer_hand}")
            print("  You won the game!")
            print("Thanks for playing.")
            looper = False
        if win == 'tie':
            print("  Its a tie. Starting over.")
            print("")




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
