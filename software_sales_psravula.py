"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 02.2 - Software Sales
Date: 02/10/2022

Description:
    This program takes the number of software packages sold as input
    and determines the total sales made, with discounts applied based
    on the number of software packages bought.

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


from turtle import numinput


def main():
   #Input statement taking number of orders
   num = float(input("How many packages will be purchased: "))
   #If elif conditional structure
   if num < 0:
       print("  Invalid Input!")
   elif 0 <= num < 4:
       total = 880 * num
       discount = 'No'
   elif 4 <= num <= 39:
       total = (880*0.9) * num
       discount = '10%' 
   elif 40 <= num <= 199:
       total = (880*0.85) * num
       discount = '15%'
   elif 200 <= num <= 999:
       total = (880*0.7) * num
       discount = '30%'
   else:
       total = (880*0.58) * num
       discount = '42%'
   num = int(num)
   #This print statement formats the total revenue
   if num >= 0:
    print(f'  {discount} discount applied.')
    print(f'  The total price to purchase {num} packages is ${total:,.2f}.')    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
