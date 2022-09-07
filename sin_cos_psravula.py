"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 10.4 - Sin Cos
Date: 4/14/2022

Description:
    This program plots a sine and cosine wave,
    and sets 1 and -1 as y boundaries, and shows
    the x boundaries 0 and 2pi.

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
#Import matplotlib as plt and numpy as np
import matplotlib.pyplot as plt
import numpy as np

"""Write new functions below this line (starting with unit 4)."""


def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Data for x and y values
    x = np.arange(0,2*np.pi,0.1)
    y = np.sin(x)
    z = np.cos(x)

    #PLot initialization
    fig, ax = plt.subplots()
    ax.plot(x,y, 'r', x,z, 'b')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    #PLot x and y ticks
    ax.set_xticks([np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax.set_xticklabels(['$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$'])
    ax.set_yticks([-1 ,1])
    
    #Frame removal
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
