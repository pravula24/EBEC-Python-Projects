"""
Author: Prathyush, psravula@purdue.edu
Assignment: 02.3 - Roulette Colors
Date: -2/12/2022

Description:
    This is program takes the pocket number as input
    and outputs a corresponding poccket roulette color.

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


"""Write new functions below this line (starting with unit 4)."""


def main():
    #Input statement for pocket number
    pocket = int(input("Please choose a pocket number: "))
    #Conditional structure to determine pocket color
    #Outputs print statement with roulette color
    if pocket == 0:
        print(f"  Pocket number {pocket} is green.")
    elif pocket == 1 or pocket == 3 or pocket == 5 or pocket == 7 or pocket == 9 or pocket == 12 or pocket == 14 or pocket == 16 or pocket == 18 or pocket == 19 or pocket == 21 or pocket == 23 or pocket == 25 or pocket == 27 or pocket == 30 or pocket == 32 or pocket == 34 or pocket == 36:
        print(f"  Pocket number {pocket} is red.")
    elif pocket == 2 or pocket == 4 or pocket == 6 or pocket == 8 or pocket == 10 or pocket == 11 or pocket == 13 or pocket == 15 or pocket == 17 or pocket == 20 or pocket == 22 or pocket == 24 or pocket == 26 or pocket == 28 or pocket == 29 or pocket == 31 or pocket == 33 or pocket == 35:
        print(f"  Pocket number {pocket} is black.")
    else:
        print("  Invalid Input!")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
