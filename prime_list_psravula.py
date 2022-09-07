"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 04.5 - Prime List
Date: 02/27/2022

Description:
    This program takes a number as input and determines all the prime numbers
    that go from 0 up to the input, and displays it in a list.

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
        divider = 2
        while divider <= int(m.sqrt(number)):
            if (number % divider) == 0:
                var = False
                break
            else:
                divider += 1
    if number == 1:
        var = False
    return var

def main():
    #Main function, input statement
    list = []
    num = int(input("Enter a positive integer: "))
    #Looping structure calling function and adding list elements
    for x in range(1, num+1):
        mark = is_prime(x)
        if mark:
            list.append(x)
    #Output statement formatting, looping structure to print
    str = ""
    str += f"{list[0]}"
    for i in range(1, len(list)):
        str += f", {list[i]}"
    
    print(f"The primes up to {num} are: {str}")

        


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
