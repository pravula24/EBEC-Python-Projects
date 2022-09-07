"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 08.4 - Number Writer
Date: 4/4/2022

Description:
This program asks a user how many random numbers between
1019 and 1215 inclusive it should geenrate, and then writes
these random numbers to a random number text file
  
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
from random import randint
"""Write new functions below this line (starting with unit 4)."""

def main():
  #Number and file input, list initialization
  user_num = int(input("How many numbers would you like? "))
  filename = open('random_numbers.txt','a')
  num_list = []

  #Random number generation, writing to file
  count = 0
  for i in range(user_num):
    num_list.append(randint(1019,1215))
    filename.write(str(num_list[count]))
    count += 1
    filename.write("\n")

  filename.close()
  
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

