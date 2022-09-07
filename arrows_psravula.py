"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 03.1 - Arrows
Date: 2/19/2022

Description:
    This program takes the number of arrows as input and uses
    nested for loops to draw a pattern of arrows correlating
    to the number of arrows taken as input.

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
    #Input statement
    arrows = int(input("Enter the number of arrows to draw: "))
    #For loop nested conditional structure
    for x in range(0, arrows):
        str = ""
        str += "<"
        for j in range(0, x):
            str += "="
        str += ">"
        #Print statement with string
        print(str)




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
