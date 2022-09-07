"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 07.1 - Multiples of N
Date: 3/27/2022

Description:
    This program has a function takes takes an integer and
    list as inputs and builds a list based off of the elements
    from the input list that are multiple of the number chosen.

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
#Function to build list of multiples
def multiples_of(number, array):
    new_list = []
    #Iterates through original list
    for i in array:
        if(i % number == 0):
            new_list.append(i)
    return new_list


def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Initialize list and divisor
    original = [19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406]
    num = 13

    #Function call and output statements
    new = multiples_of(num, original)
    print("Original list of numbers:")
    print(f"  {original}")
    print("Numbers in the list that are multiples of 13:")
    print(f"  {new}")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
