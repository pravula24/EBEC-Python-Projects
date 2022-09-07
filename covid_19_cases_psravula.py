"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 10.3 - Covid 19 Cases
Date: 4/18/2022

Description:
    This program reads data from a covid 19 cases text file
    and calculates the total number of positive test cases for
    each day and plots it in a bar chart.

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
import datetime
import matplotlib.pyplot as plt

"""Write new functions below this line (starting with unit 4)."""
#Read dates function
def readDates(name):
    file = open(name, 'r')
    values = file.readlines()
    values = [i.split()[0] for i in values]
    file.close()
    return values

#Read cases function
def readCases(name):
    file = open(name, 'r')
    val = file.readlines()
    val = [int(k.split()[2]) for k in val]
    file.close()
    return val

def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Initializes file name and sends to functions
    fileName = "indiana_covid-19_data_spring_2022.txt"
    time = readDates(fileName)
    case = readCases(fileName)
    for i in range(1, len(case)):
        case[i] = case[i] + case[i - 1]

    #Initializes sub plot and divides date data
    fig, ax = plt.subplots()
    xv = []
    for d in time:
        y, m, d = d.split('-')
        t = datetime.date(int(y), int(m), int(d))
        xv.append(t)

    #Sets title, labels, ticks, and bar charts
    ax.set_title("Positive COVID-19 Cases in Indiana")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Cases (in thousands)")
    ax.set_yticklabels(['0', '200', '400', '600', '800', '1000', '1200', '1400', '1600', '1800'])

    ax.bar(xv, case)
    fig.autofmt_xdate()
    plt.show()


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
