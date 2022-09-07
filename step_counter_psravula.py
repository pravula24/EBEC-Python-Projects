"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 08.6 - Step Counter
Date: 4/4/2022

Description:
This program reads the steps.txt, which has the amount of steps
a person has taken each day for a year and returns the average steps taken each month.
  
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
  #List and Filename Initialization 
  filename = open('steps.txt','r')
  mlist = []

  steps = filename.readlines()
  filename.close()

  #Average step calculation for months
  #List appending
  spackets = [float(x) for x in steps]
  mlist.append(sum(spackets[:31])/31)
  mlist.append(sum(spackets[31:59])/28)
  mlist.append(sum(spackets[59:90])/31)
  mlist.append(sum(spackets[90:120])/30)
  mlist.append(sum(spackets[120:151])/31)
  mlist.append(sum(spackets[151:181])/30)
  mlist.append(sum(spackets[181:212])/31)
  mlist.append(sum(spackets[212:243])/31)
  mlist.append(sum(spackets[243:273])/30)
  mlist.append(sum(spackets[273:304])/31)
  mlist.append(sum(spackets[304:334])/30)
  mlist.append(sum(spackets[334:])/31)

  #Outputs 
  print(f'''The average steps taken each month were:
   January : {mlist[0]:.2f}
  February : {mlist[1]:.2f}
     March : {mlist[2]:.2f}
     April : {mlist[3]:.2f}
       May : {mlist[4]:.2f}
      June : {mlist[5]:.2f}
      July : {mlist[6]:.2f}
    August : {mlist[7]:.2f}
 September : {mlist[8]:.2f}
   October : {mlist[9]:.2f}
  November : {mlist[10]:.2f}
  December : {mlist[11]:.2f}''')
            
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

