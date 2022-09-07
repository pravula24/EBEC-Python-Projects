"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 09.3 - Course Info
Date: 4/11/2022

Description:
    This program creates nd returns a nested dictionary of courses complete
    with their course name, professor name, and class time.

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
def get_course_data():

    #Creates nested dict with course data
    courses = {'CS101': {'room': '3004', 'instructor': 'Django', 'time': '9:00 a.m.'},
              'CS102': {'room': '4501', 'instructor': 'Idle', 'time': '10:00 a.m.'},
              'CS103': {'room': '6755', 'instructor': 'Rich', 'time': '11:00 a.m.'},
              'NT110': {'room': '1244', 'instructor': 'Marshal', 'time': '12:00 p.m.'},
              'CM241': {'room': '1411', 'instructor': 'Pickle', 'time': '2:00 p.m.'}}
    
    return (courses)

def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Function call and input statement
    course_list = get_course_data()
    course_num = input("Enter a course number: ")

    #Output statements printing course number information
    if course_num in course_list:
        print(f"  The details for course {course_num} are:")
        print(f"    Instructor: {course_list[course_num]['instructor']}")
        print(f"          Room: {course_list[course_num]['room']}")
        print(f"          Time: {course_list[course_num]['time']}")
    else:
        print(f"  {course_num} is an invalid course number.")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
