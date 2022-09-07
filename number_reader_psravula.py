"""
Author: Prathyush Rvaula, psravula@purdue.edu
Assignment: 08.5 - Number Reader
Date: 4/4/2022

Description:
This program takes the random numbers generated in 
random_number.txt and calculates the minimum, maximum,
number of random numbers, sum, and average.
  
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

def main():
  #Variable and fuile name initialization 
  filename = 'random_numbers.txt'
  count = 0
  minimum = 0
  maximum = 0
  sum_tot = 0

  #Reads through file and calculates min, max, avg, count, and sum
  with open(filename, 'r') as read:
    for i in read:
      num = int(i)
      if count == 0:
        minimum = maximum = num
      if num < minimum: 
        minimum = num
      if num > maximum: 
        maximum = num
      sum_tot += num
      count += 1
  avg = sum_tot/count

  #Output Statements
  print(f'{count:,} numbers were read from the file.')
  print(f'Min: {minimum}')
  print(f'Max: {maximum:,}')
  print(f'Sum: {sum_tot:,}')
  print(f'Avg: {avg:,.1f}')
  
          
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

