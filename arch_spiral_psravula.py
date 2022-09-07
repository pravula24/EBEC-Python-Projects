"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 06.4 - Arch Spiral
Date: 3/20/2022

Description:
    This program draws an Archimedean spiral using
    turtle graphics.

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
from turtle import *
import math as m


"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(5)


def main():
    """Write your mainline logic below this line (then delete this line)."""
    for i in range(2160):
        angle = i * m.pi/180
        x = angle/(m.pi*m.pi) * m.cos(angle)
        y = angle/(m.pi*m.pi) * m.sin(angle)
        speed(1)
        goto(x, y)



"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
