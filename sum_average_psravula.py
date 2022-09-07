"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 03.2 - Sum Average
Date: MM/DD/YYYY

Description:
    This program asks the user to enter a series of non
    negative numbers, negative number singaling the end of the list,
    and display the sum and avergae of the numbers.

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
   #Variable initialization
   num = 0
   sum = 0
   count = 0
   #Conditional structure to get inputs
   while num >= 0:
       sum += num
       count += 1
       num = float(input("Enter a non-negative number (negative to quit): "))
   count -= 1
   #Conditional structure to determine output
   if count == 0:
       print("  You didn't enter any numbers.")
   else:
       print(f"  You entered {count} numbers.")
       average = sum/count
       print(f"  Their sum is {sum:.3f} and their average is {average:.3f}.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
