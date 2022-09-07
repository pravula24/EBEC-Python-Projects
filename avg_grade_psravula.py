"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 02/22/2022

Description:
    This program takes five grades as inputs and calculates the
    letter grades for those numbers and calculates the average
     and displays the letter grade for it as well.

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
from turtle import end_fill

#Function to get valid score
def get_valid_score():
    score = float(input("Enter a score: "))
    while score < 0 or score > 100:
        print("  Invalid Input. Please try again.")
        score = float(input("Enter a score: "))
    return score

#Function to get letter correlated to number
def determine_grade(number):
    if 0 <= number < 64:
        letter = 'F'
    elif 64 <= number < 73:
        letter = 'D'
    elif 73 <= number < 82:
        letter = 'C'
    elif 82 <= number < 92:
        letter = 'B'
    else:
        letter = 'A'
    return letter

#Functin to get average of numbers
def calc_average(num_list):
    sum = 0
    for i in num_list:
        sum += i
    avg = sum/len(num_list)
    return avg

def main():
    #Function calls for scores and letters
    one = get_valid_score()
    one_letter = determine_grade(one)
    print(f"  The letter grade for {one:.1f} is {one_letter}.")

    two = get_valid_score()
    two_letter = determine_grade(two)
    print(f"  The letter grade for {two:.1f} is {two_letter}.")

    three = get_valid_score()
    three_letter = determine_grade(three)
    print(f"  The letter grade for {three:.1f} is {three_letter}.")

    four = get_valid_score()
    four_letter = determine_grade(four)
    print(f"  The letter grade for {four:.1f} is {four_letter}.")

    five = get_valid_score()
    five_letter = determine_grade(five)
    print(f"  The letter grade for {five:.1f} is {five_letter}.")

    #Score in average grade function call
    average = calc_average([one, two, three, four, five])
    average_grade = determine_grade(average)
    
    #Output statements
    print("\nResults:")
    print(f"  The average score is {average:.2f}.")
    print(f"  The letter grade for {average:.2f} is {average_grade}.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
