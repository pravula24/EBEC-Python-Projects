"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 07.2 - Number Analysis
Date: 3/27/2022

Description:
    This program prmopts the user to enter a list of numbers
    and calculates the minimum, maximum, avergae, and total
    of the numbers in the list.

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
def get_number_list():
    #Initializes list and makes input statements
    listnum = []
    for i in range(10):
        x = float(input(f"  number {i+1:2d} of 10: "))
        listnum.append(x)
    return(listnum)



def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Initialization of numbers and function call
    print("Enter 10 numbers:")
    num_list = get_number_list()
    min = num_list[0]
    max = num_list[0]
    sum = 0.00
    sum += num_list[0]
    #Iterates through and finds max/min and sum
    for i in num_list[1:]:
        if i < min:
            min = i
        if i > max:
            max = i
        sum += i
    #Average and output statements
    avg = sum/len(num_list)
    print(f"Highest number: {max:.2f}")
    print(f"Lowest number: {min:.2f}")
    print(f"Total: {sum:.2f}")
    print(f"Average: {avg:.2f}")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
