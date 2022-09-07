"""
Author: Your Name, psravula@purdue.edu
Assignment: 01.1 - Vineyard
Date: 01/31/2022

Description:
    This program takes length of row in meters, amount of space,
    and space between vines as input from user, and calculates
    number of grapevines that will fit in the row.

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
    #Prints statement and takes input value from 
    #users on details about vineyard, takes input as float
    print("Enter each of the following quantities in meters.")
    e_val = float(input("  How wide is the end-post assembly? "))
    s_val = float(input("  How much space should be between the vines? "))
    r_val = float(input("  How long is this row? "))

    #performs calculation to find number of grapevines to fit
    v_val = (r_val - (2 * e_val))/s_val
    #converts to int
    v_val = int(v_val)

    #print statement showing calculation
    print(f"\nThere is enough space for {v_val} vine(s) in this row.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
