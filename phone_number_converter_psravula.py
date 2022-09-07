"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 08.2 - Phone Number Converter
Date: 4/4/2022

Description:
    This program takes a telephone number with letters
    in the number and converts it to an all number caller
    id.

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
#Function to convert telephone number
def convert_number(mix):
    array2 = [['A','B','C','a','b','c'],
    ['D','E','F','d','e','f'],
    ['G','H','I','g','h','i'],
    ['J','K','L','j','k','l'],
    ['M','N','O','m','n','o'],
    ['P','Q','R','S','p','q','r','s'],
    ['T','U','V','t','u','v'],
    ['W','X','Y','Z','w','x','y','z']]
    #Looping structure to replace characters with numbers
    for i in array2:
        for c in i:
            num = str(array2.index(i)+2)
            mix = mix.replace(c, num)
    return mix

def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Input, function call, and output statement
    phone = str(input("Enter a telephone number: "))
    num_phone = convert_number(phone)
    print(f'The phone number is {num_phone}')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
