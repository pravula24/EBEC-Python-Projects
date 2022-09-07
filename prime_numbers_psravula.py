"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: 02/22/2022

Description:
    This program takes a number as input and determines if it is a prime numbr or not.
    The user enters -1 to quit the program.

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
import math as m

def is_prime(number):
    #Is_Prime function, looping structure dividing number to find 
    #divisibility
    var = True

    if number > 1:
        for i in range(2, int(m.sqrt(number))):
            if (number % i) == 0:
                var = False
                break
    if number == 1:
        var = False
    return var

def main():
    #Main function, input statement
    num = 0
    num = int(input("Enter a positive integer (-1 to quit): "))

    #While function, function call and output statements
    while num >= 0:
        mark = is_prime(num)
        #Conditional statement for output depending on function output
        if mark:
            print(f"  {num} is prime!")
        else:
            print(f"  {num} is not prime.")

        num = int(input("Enter a positive integer (-1 to quit): "))


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
