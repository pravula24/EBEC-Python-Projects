"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 04.2 - Max of Two
Date: 2/21/2022

Description:
    

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
#Function to determine greater number
def max_of_two(one, two):
    if one > two:
        max = one
    else:
        max = two
    return max

def main():
    #Input print statements
    first = int(input("Enter the first integer: "))
    second = int(input("Enter the second integer: "))
    #Function call and output statement
    greater = max_of_two(first, second)
    print(f"The number {greater} is greater.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
