"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 2/13/2022

Description:
    This program takes the temperature, the velocity of the fluid, and
    diameter of the pipe, and calculates the Reynolds number, which
    is used to determine if the fluid flow is laminar or turbulent.

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
    #Input statement taking velocity, temperature, and pipe diameter
    temp = int(input("Enter the temperature in \u00B0C as 5, 20, or 50: "))
    velocity = float(input("Enter the velocity of water in the pipe (m/s): "))
    d = float(input("Enter the pipe's diameter (m): "))

    #Assigning of kinematic velocity
    if temp == 5:
        v = 1.52 * 10**(-6)
    elif temp == 20:
        v = 1.00 * 10**(-6)
    else:
        v = 5.54 * 10**(-7)
    #Calculation of Reynolds number
    r = (velocity*d)/(v)
    num = (format(r,'.2e'))
    temp = float(temp)
    #Print statement
    print(f"At {temp}\u00B0C, the Reynolds number for flow at {velocity} m/s in a {d} m diameter pipe is {num}.")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
