"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 3/20/2022

Description:
    This program writes the vowels of the alphabet and is called 
    whenever a vowel is needed to be written by the random_vowels
    python file.

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

#A drawing function
def draw_a():
    """Complete this function to draw the character a."""
    penup()
    left(90)
    forward(35)
    right(180)
    pendown()
    circle(35)
    penup()
    circle(35, 180)
    forward(35)
    right(180)
    pendown()
    forward(70)
    penup()
    setheading(0)
    forward(15)

#E drawing function
def draw_e():
    """Complete this function to draw the character e."""
    penup()
    left(90)
    forward(35)
    pendown()
    right(90)
    forward(70)
    left(90)
    circle(35, 315)
    penup()
    circle(35, 45)
    right(180)
    forward(35)
    left(90)
    forward(15)

#I drawing function
def draw_i():
    """Complete this function to draw the character i."""
    penup()
    forward(35)
    left(90)
    pendown()
    forward(70)
    penup()
    forward(25)
    dot(10)


    penup()
    right(180)
    forward(95)
    left(90)
    forward(50)

#O drawing function
def draw_o():
    """Complete this function to draw the character o."""
    penup()
    setheading(0)
    forward(35)
    pendown()
    setheading(0)
    circle(35)
    penup()
    forward(50)

#U drawing function
def draw_u():
    """Complete this function to draw the character u."""
    penup()
    setheading(90)
    forward(70)
    right(180)
    pendown()
    setheading(0)
    right(90)
    forward(35)
    circle(35, 180)
    forward(35)
    penup()
    right(180)
    forward(35)
    pendown()
    forward(35)
    setheading(0)
    penup()
    forward(15)

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

#Main, nothing in it
def main():
    """You can use this function for your own testing. It will not be checked
    by the auto-grader."""

    #pass


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
