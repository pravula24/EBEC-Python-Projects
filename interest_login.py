"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 01.2 - Interest
Date: 02/04/2022

Description:
    This program asks the user for the principal amount, annual interest,
    number of years, and number of times interest is compounded every year
    as input, and outputs the future value of the account.

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
    #Input statements taking parameters for future value function
    print("Enter the following parameters.")
    p_val = float(input("  The initial deposit? "))
    r_val = float(input("  The annual interest rate in percent? "))
    t_val = float(input("  The number of years the account earn interest? "))
    n_val = float(input("  The number of times interest is compounded each year: "))

    #Percentage division that divides by 100
    r_val = r_val/100.0

    #formula to calculate future value
    f_val = p_val * pow((1 + (r_val/n_val)),(n_val*t_val))

    #Print statement that displays formatted future value of account
    print(f"The balance of this account will be ${f_val:,.2f} after {t_val} years.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
