"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 04.3 - Average Grade
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


def get_valid_score():
    score = print("Enter a score: ")
    while score < 0:
        print("  Invalid input. Please try again.")
        score = print("Enter a score: ")
    return score

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

def calc_average(num_list):
    sum = 0
    for i in num_list:
        sum += i
    avg = sum/5
    return avg

def main():
    one = get_valid_score()
    one_letter = determine_grade(one)
    print(f"  The letter grade for{one} is {one_letter}.")

    two = get_valid_score()
    two_letter = determine_grade(two)
    print(f"  The letter grade for{two} is {two_letter}.")

    three = get_valid_score()
    three_letter = determine_grade(three)
    print(f"  The letter grade for{three} is {three_letter}.")

    four = get_valid_score()
    four_letter = determine_grade(four)
    print(f"  The letter grade for{four} is {four_letter}.")

    five = get_valid_score()
    five_letter = determine_grade(five)
    print(f"  The letter grade for{five} is {five_letter}.")

    score_list = [one, two, three, four, five]
    average = calc_average(score_list)
    average_grade = determine_grade(average)
    print("\n")
    print(f"  The average score is {average:.2f}.")
    print(f"  The letter grade for {average:.2f} is {average_grade}.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
