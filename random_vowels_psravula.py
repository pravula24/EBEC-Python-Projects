"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 3/20/2022

Description:
    This program calls the vowels module and prints
    out each vowel in a random order until all vowels
    have been printed.

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

"""Import modules below this line (starting with unit 6)."""
#Importing modules
from turtle import *
import vowels
import random as r
from random import randint


"""Write new functions below this line (starting with unit 4)."""

#Starting function
def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Samples 5 random integers from 1 to 5
    numlist = r.sample(list(range(5)), 5)
    
    #Assigns letter to number and outputs in order
    for i in numlist:
        if i == 2:
            vowels.draw_u()
        if i == 3:
            vowels.draw_o()
        if i == 4:
            vowels.draw_e()
        if i == 1:
            vowels.draw_a()
        if i == 0:
            vowels.draw_i()
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
