"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 09.1 - Capital Quiz
Date: 4/11/2022

Description:
    This program quizzes the user on state capitals,
    states are asked in a random order and a function that initializes
    state capital data is called upon to check user answers.

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
import random

def get_state_data():

    #Reads from text file into dictionary
    file = open("state_capitals.txt", "r")
    capital_list = {}
    for i in file.readlines():
        cap = i.split(", ")
        capital_list[cap[1].strip()] = cap[0].strip()
    file.close()

    return (capital_list)

def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Function call and initialization
    clist = get_state_data()
    states = list(clist.keys())
    correct = 0
    tot = 0
    var = True

    #Random question user input and answer verification
    while var:
        state = random.choice(states)
        capital = (clist[state])
        answer = input(f"What is the capital of {state} (enter 0 to quit)? ")
        if answer == '0':
            print(f"You answered {correct} out of {tot} questions correctly.")
            var = False
            break

        if answer.upper() == capital.upper():
            print(f"  That is correct!")
            states.remove(state)
            correct += 1
            tot += 1
        else:
            print(f"  That is incorrect.")
            print(f"  The capital of {state} is {capital}.")
            tot += 1

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
