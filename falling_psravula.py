"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 04.1 - Falling
Date: 02/21/2022

Description:
    This programs loops through certain time values, sends them to functions,
    and calculates the distance fallen.

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
#Function to calculate falling distance
def falling_dist(time):
    d = (1/2)*(8.87)*(time)**2
    return d

def main():
    #Output print statements
    print("Time (s)  Distance (m)")
    print("----------------------")
    #Conditional structure calling function
    for i in range(5, 55, 5):
        distance = falling_dist(i)
        print(f"{i:8d}  {distance:12.1f}")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
