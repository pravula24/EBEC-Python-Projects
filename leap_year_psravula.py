"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 02.1 - Leap Year
Date: 02/09/2022

Description:
    This program takes the year as input from the year
    and returns the number of days in February based on
    whether or not the year is a leap year.

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
    #Input taking year number
    year = int(input("Enter a year: "))
    #Conditional structure that determines whether year is a leap year
    #or not
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        if year % 4 == 0:
            leap = True
        else:
            leap = False
    #Default number of days in Feb set to 28
    #If 29, prints "leap year statement", if not, prints opposite
    febday = 28
    if leap == True:
        febday = 29
        print(f"The year {year} is a leap year.")
    else:
        print(f"The year {year} is not a leap year.")
    #Prints final statements stating number of days in February
    print(f"February of {year} has {febday} days.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
