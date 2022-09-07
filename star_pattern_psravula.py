"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 05.3 - Star Pattern
Date: 3/6/2022

Description:
    This program takes the number of points as input 
    and output a drawing of a polygon with the user
    specified number of points.

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

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    #Setup width and background function
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()


def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Input for points
    points = int(input("Enter the number of points for the star: "))
    #Color setup for shape drawing
    color = 'beige'
    fillcolor(color)
    begin_fill()
    A = 360/points
    B = 2*A
    #For loop drawing structure
    start()
    setheading(90-B/2)
    for i in range(points):
        right(180-B)
        forward(60)
        left(180-A)
        forward(60)
    end_fill()



"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
