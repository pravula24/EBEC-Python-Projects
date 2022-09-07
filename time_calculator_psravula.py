"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 2/12/2022

Description:
    This program takes seconds as input and converts it to
    days, hours, minutes, and seconds.

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
    #Input statement getting time in seconds
    time = int(input("Please enter a time in seconds: "))

    #Calculating minutes, hours, days, and seconds to display
    minutes = time // 60
    hours = time // 3600
    days = time // 86400

    seconds = time - (minutes*60)
    minutedisp = minutes - (hours*60)
    hourdisp = hours - (days*24)

    #Conditional structure deciding which print statement to output based on values
    if time < 60:
        print(f"  {time} seconds is less than one minute.")
    
    elif days > 0 and hourdisp == 0 and minutedisp == 0 and seconds == 0:
        print(f"  {time:,d} seconds equals {days} day(s).")
    
    elif days == 0 and hourdisp > 0 and minutedisp == 0 and seconds == 0:
        print(f"  {time:,d} seconds equals {hourdisp} hour(s).")
   
    elif days == 0 and hourdisp == 0 and minutedisp > 0 and seconds == 0:
        print(f"  {time:,d} seconds equals {minutedisp} minute(s).")
    
    elif days == 0 and hourdisp == 0 and minutedisp > 0 and seconds > 0:
        print(f"  {time:,d} seconds equals {minutedisp} minute(s) and {seconds} second(s).")
    
    elif days == 0 and hourdisp > 0 and minutedisp == 0 and seconds > 0:
        print(f"  {time:,d} seconds equals {hourdisp} hour(s) and {seconds} second(s).")
    
    elif days > 0 and hourdisp == 0 and minutedisp == 0 and seconds > 0:
        print(f"  {time:,d} seconds equals {days} day(s) and {seconds} second(s).")

    elif days == 0 and hourdisp > 0 and minutedisp > 0 and seconds == 0:
        print(f"  {time:,d} seconds equals {hourdisp} hour(s) and {minutedisp} minute(s).")
    
    elif days > 0 and hourdisp == 0 and minutedisp > 0 and seconds == 0:
        print(f"  {time:,d} seconds equals {days} day(s) and {minutedisp} minute(s).")

    elif days > 0 and hourdisp > 0 and minutedisp == 0 and seconds == 0:
        print(f"  {time:,d} seconds equals {days} day(s) and {hourdisp} hour(s).")
    
    elif days > 0 and hourdisp > 0 and minutedisp == 0 and seconds > 0:
        print(f"  {time:,d} seconds equals {days} day(s), {hourdisp} hour(s) and {seconds} second(s).")
    
    elif days > 0 and hourdisp == 0 and minutedisp > 0 and seconds > 0:
        print(f"  {time:,d} seconds equals {days} day(s), {minutedisp} minute(s) and {seconds} second(s).")
    
    elif days > 0 and hourdisp > 0 and minutedisp > 0 and seconds == 0:
        print(f"  {time:,d} seconds equals {days} day(s), {hourdisp} hour(s) and {minutedisp} minute(s).")

    elif days == 0 and hourdisp > 0 and minutedisp > 0 and seconds > 0:
        print(f"  {time:,d} seconds equals {hourdisp} hour(s), {minutedisp} minute(s) and {seconds} second(s).")

    elif days > 0 and hourdisp > 0 and minutedisp > 0 and seconds > 0:
        print(f"  {time:,d} seconds equals {days} day(s), {hourdisp} hour(s), {minutedisp} minute(s) and {seconds} second(s).")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
