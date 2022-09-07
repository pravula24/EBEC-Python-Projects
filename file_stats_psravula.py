"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 08.3 - File Stats
Date: 4/4/2022

Description:
This program reads a file and calculates the number of words,
white spaces, and avergae number of words per line in the text file.
  
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
  #File input
  filename = 'frontiero_v_richardson.txt'
  w_count = 0
  l_count = 0

  #Word count within file and line count
  with open(filename) as fo:
    for i in fo:
      l_count += 1
      words = i.split()
      w_count += len(words)

  #Avergae word per line calculation
  #Formats counts
  avg = str(format((w_count / l_count),'.1f'))
  wordnum = str(w_count)
  linenum = str(l_count)

  #Prints output
  print("Total number of words: " + wordnum)
  print("Total number of lines: " + linenum)
  print("Average number of words per line: " + avg)
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

