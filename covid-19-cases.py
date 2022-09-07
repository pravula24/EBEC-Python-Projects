###############################################################################
# Author: Atharva Gunda
# Date: 12/31/2020
# This program prints a bar graph of the cumulative positive test results for the covid-19 cases in Indiana.
###############################################################################

import datetime
import matplotlib.pyplot as plt

def main():
    fileName = "covid-19_data.txt"
    dates = readDates(fileName)
    cases = readCases(fileName)
    for i in range(1, len(cases)):
        cases[i] = cases[i] + cases[i - 1]
    plot(dates, cases)
    return

def readDates(name):
    fin = open(name, 'r')
    values = fin.readlines()
    values = [i.split()[0] for i in values]
    fin.close()

    return values

def readCases(name):
    fin = open(name, 'r')
    values = fin.readlines()
    values = [int(i.split()[2]) for i in values]
    fin.close()

    return values

def plot(xvals, yvals):
    fig, ax = plt.subplots()
    xv = []
    for d in xvals:
        y, m, d = d.split('-')
        t = datetime.date(int(y), int(m), int(d))
        xv.append(t)

    ax.set_title("Positive COVID-19 Cases in Indiana")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Cases")
    ax.set_yticks([i for i in range(0, 350000, 50000)])

    ax.bar(xv, yvals)
    fig.autofmt_xdate()
    plt.show()

main()
