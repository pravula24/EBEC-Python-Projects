"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 04/18/2022

Description:
    This program reads gas prices from text file and plots them 
    in a line chart using matplotlib.

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
import matplotlib.pyplot as plt

"""Write new functions below this line (starting with unit 4)."""


def main():
    #Reads from file
    with open("2008_Weekly_Gas_Averages.txt") as file:
        price = file.readlines()

    #List Initialization and data collection
    x = []
    y = []
    count = 0
    for i in price:
        y.append(float(i.strip("\n")))
        count += 1
        x.append(count)
    
    #Plot initalization and plot components
    #Setting labels and ticks
    fig, ax = plt.subplots()
    ax.set_xticks([10, 20, 30, 40, 50])
    ax.set_xlim(1,52)
    ax.set_ylim(1.5, 4.25)
    ax.set_title("2008 Weekly Gas Prices") 
    ax.set_xlabel("Weeks (by number)") 
    ax.set_ylabel("Average Price (dollars/gallon)") 
    ax.grid()
    ax.plot(x, y)
    plt.show()


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
