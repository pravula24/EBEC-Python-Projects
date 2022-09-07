"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 09.2 - World Series
Date: 4/11/2022
Description:
    This program takes a year as input and outputs
    the team that won the World Series that years
    as well as the number of times they have won in total.

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

def load_winners_data():

    #Puts the data from the text file into a list
    file = open("WorldSeriesWinners.txt", "r")
    years = list(range(1903, 2021))
    years.remove(1904)
    years.remove(1994)
    teams = file.readlines()
    file.close()

    #Creates the first dictionary
    names = list(set(teams))
    wins = {}
    for i in names:
        wins[i.strip()] = teams.count(i)

    #Creates the second dictionary
    winners = {}
    for i in range(len(years)):
        winners[years[i]] = teams[i].strip()

    return (wins, winners)

def main():

    #Asks the user for a year to display the output
    wins, winners = load_winners_data()
    years = list(range(1903, 2021))
    years.remove(1904)
    years.remove(1994)
    year = int(input(f"Enter a year in the range 1903 -- 2020: "))
    if ((year == 1904) or (year == 1994)):
        print(f"  The World Series wasn't played in the year {year}.")
    elif year not in years:
        print(f"  Data for the year {year} is not included in this system.")
    else:
        print(f"  The {winners[year]} won the World Series in {year}.")
        print(f"  They have won the World Series {wins[winners[year]]} times.")

if __name__ == '__main__':
    main()