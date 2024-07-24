from classes import *
import inquirer
from colorama import Fore, Back, Style
# questions = [
#   inquirer.List('size',
#                 message="What size do you need?",
#                 choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
#             ),
# ]
# answers = inquirer.prompt(questions)



if __name__ == "__main__":
    print('''
    WELCOME TO YOUR PORTAL
    ''')
    while True:
        questions = [
        inquirer.List('input1',
                        message="What would you like to do?",
                        choices=[('Log in as student',1),('Log in as teacher',2), ('Exit',3)],
                    ),
        ]
        answers = inquirer.prompt(questions)
        # print(answers)
#         i1 = input('''
# What would you like to do?
# 1) Log in as student
# 2) Log in as teacher
# 3) Exit
# ''')
        if answers["input1"] == 1:
            stud_input = input("Input your id? ")
        elif answers["input1"] == 2:
            teach_input = input("Input your id? ")
            user = Teacher.get_one(teach_input)
            if user:
                print(f"Hello {user.name}")
                while True:
                    i2 = input('''
What would you like to do?
1) Remove Student
2) Attendence
3) See all students
4) Back
''')
                    if i2 == "1":
                        my_students = user.students()
                        questions = [
                        inquirer.List('student',
                                        message="Which Student would you like to grade?",
                                        choices=[(student.name,student) for student in my_students],
                                    ),
                        ]
                        selected_student = inquirer.prompt(questions)
                        print('\033[31m'+ f"DELETING {selected_student['student'].name}")
                        print(Style.RESET_ALL)
                        selected_student["student"].delete()
                    elif i2 == "3":
                        my_students = user.students()
                        for student in my_students:
                            print(student.name)
                    elif i2 == "4":
                        break
            else:
                print("Not valid teacher id")
            
        elif answers["input1"] == 3:
            break
        else:
            print("Please have valid input")
            break