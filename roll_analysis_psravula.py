"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 3/28/2022

Description:
    This program takes a number as input as the number of rolls
    of a pair of six-sided dice and calculates the percentage of 
    output for each possible number.

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
from random import randint

"""Write new functions below this line (starting with unit 4)."""
#Roll d6 function
def roll_d6():
    num = randint(1,6)
    return num

#Roll pair of six sided dice function
def get_2d6_rolls(iterations):
    roll_list = []
    for i in range(iterations):
        roll1 = roll_d6()
        roll2 = roll_d6()
        element = roll1 + roll2
        roll_list.append(element)
    return roll_list

def main():
    """Write your mainline logic below this line (then delete this line)."""
    #initialization of frequencies and function call
    numlist = get_2d6_rolls(1000000)
    freqlist = [0,0,0,0,0,0,0,0,0,0,0] 
    #Iterates through list returned
    for i in numlist:
        freqlist[i-2] += 1
    
    #Calculates averages
    #Output statements
    print("Roll  Frequency")
    count = 2
    for k in freqlist:
        avg = (k/len(numlist))*100
        print(f"{count:3d}   {avg:6.2f}%")
        count += 1

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
