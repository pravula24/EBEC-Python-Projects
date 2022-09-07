"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 03.4 - Organisms
Date: 2/19/2022

Description:
    This program takes the starting population in the thousands,
    average daily increase in percent, 
    and number of days to multiply, and calculates the gradual
    increase of the population over the time period.

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
    #Input and Initialization Statements
    start = float(input("Starting population, in thousands: "))
    rate = float(input("Average daily increase, in percent: "))
    days = int(input("Number of days to multiply: "))
    curr = start
    print("Day   Approx. Pop")
    #Conditional Structure for Output printing
    for i in range(0, days+1):
        if i == 0:
            print(f"{i:3.0f}   {start:11,.3f}")
        else:
            #Growth calculation
            curr*=(1 + (rate/100))
            print(f"{i:3.0f}   {curr:11,.3f}")
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
