"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 03.3 - Rainfall
Date: 2/19/2022

Description:
    This program uses nested loops to collect data and
    calculate average rainfall over a period of years,
    all of which is specified in user input.

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
    #Initialization and input statements
    years=  int(input("Enter the number of years: "))
    sum = 0
    monthcount = 0
    #Year conditional structure
    if years <= 0:
        print("Invalid input; years must be greater than 0.")
    else:
        #Year conditional structure continued
        for i in range(1, years+1):
            print(f"  For year No. {i}")
            #Month conditional structure
            for j in ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"):
                num = float(input(f"    Enter the rainfall for {j}.: "))
                #Repeated while loop checking input
                while num < 0:
                    print("    Invalid input; rainfall cannot be negative.")
                    num = float(input(f"    Enter the rainfall for {j}.: "))
                sum += num
                monthcount += 1
        average = sum/monthcount
        print(f"There are {monthcount} months.")
        print(f"The total rainfall was {sum:.2f} inches.")
        print(f"The monthly average rainfall was {average:.2f} inches.")
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
