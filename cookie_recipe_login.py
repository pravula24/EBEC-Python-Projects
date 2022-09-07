"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 02/04/2022

Description:
    This program takes number of cookies the user
    would like to make as input, and outputs the cups of butter, sugar,
    and flour needed to make the batch.

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
    #This is the input statement taking the number of cookies
    #the user wants
    batch = int(input("How many cookies do you want to make? "))
    print(f"To make {batch:,.0f} cookies, you will need:")
    #Mathematical calculations to get the cups of butter, sugar, and
    #flour
    butter = batch/38.4
    sugar = batch/32.0
    flour = batch/19.2
    #Print statements containing width spacer, prints out number of 
    #cups of butter, sugar, flour needed, formatted properly
    print(f"{butter:10,.2f} cups of butter")
    print(f"{sugar:10,.2f} cups of sugar")
    print(f"{flour:10,.2f} cups of flour")
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
20