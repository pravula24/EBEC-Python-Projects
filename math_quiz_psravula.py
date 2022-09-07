"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 3/19/2022

Description:
    This program outputs random integers and quizzes the user on
    the addition of the two integers.

Contributors:
    Prathyush Ravula, psravula@purdue.edu [repeat for each]

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
#Random number import
from random import randint

"""Write new functions below this line (starting with unit 4)."""
#Function to retrieve random numbers
def random_number(digits):
    if digits == 2:
        num = randint(10, 99)
    if digits == 3:
        num = randint(100, 999)
    return num


def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Calls random number function to generate numbers
    twodigit = random_number(2)
    threedigit = random_number(3)
    sum = twodigit + threedigit

    #Prints initial setup statements
    print(f"   {twodigit}")
    print(f"+ {threedigit}")
    print("-----")
    userinput = int(input("= "))

    #Conditional to check if user input matches sum
    if userinput != sum:
        print(f"Incorrect. The correct answer is {sum}.")
    else:
        print("Correct -- Good Work!")




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
