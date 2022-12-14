"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 10.1 - Monthly Sales
Date: 4/14/2022

Description:
    This program takes user input for monthly
    sales and depicts it in a pie chart.

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
#Import matplotlib module for use
import matplotlib.pyplot as plt


"""Write new functions below this line (starting with unit 4)."""


def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Lists initialization for labels and colors
    l = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    sales = []
    c = ['#4D4038', '#BAA892', '#5B6870', '#6E99B4', '#A3D6D7', '#085C11', '#849E2A', '#C3BE0B', '#E9E45B', '#6B4536', '#B46012', '#FF9B1A']
    
    #User input loop structure, adds input to sales array
    for i in l:
        num = int(input(f"Enter the sales for {i}: "))
        sales.append(num)
    
    #Plotting data and title for output graph visualization
    fig, ax = plt.subplots()
    ax.pie(sales, colors=c, labels=l)
    ax.set_title('Monthly Sales Values')
    plt.show()


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
