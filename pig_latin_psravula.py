"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 08.1 - Pig Latin
Date: 4/4/2022

Description:
    This program takes a string input and divides into
    words, and then takes the first letter and puts it at
    the end of each word and attach an a and a y at the end as well.

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
#Function to get final string
def pig(lst):
    count = 0
    #Iterates through word list
    word_list = lst.split()
    for i in word_list:
        #Builds new string for each word
        letter = i[0]
        i = str(i[1:]) + letter + 'ay'
        word_list[count] = i
        count += 1
    final_string = ' '.join(word_list)
    final = final_string.capitalize()
    return final


def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Takes string input
    input_string = str(input("Enter a string: "))
    output = pig(input_string)
    #Capitalizes string, display statement
    print(f"Pig latin: {output}")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
