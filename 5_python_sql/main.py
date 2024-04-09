from tables import *
import inquirer
from colorama import Fore, Back, Style


if __name__ == '__main__':
    i1 = input("Are you a student or a teacher ")
    if i1 == "student":
        i2 = input("Log in with id: ")
        student = Student.read_one(int(i2))
        if student:
            print(f"Hello {student.name}")
            questions = [
            inquirer.List("value",
                            message="What would you like to do?",
                            choices=[('Update Name',1), ('Delete self',2), ('Display Classes',3),('exit',4)],
                        )
            ]
            in_options = True
            while in_options:
                answers = inquirer.prompt(questions)
                print(answers)
                if answers['value'] == 1:
                    i3 = input("Input new name: ")
                    student.name = i3
                    student.update()
                elif answers['value'] == 2:
                    student.delete()
                elif answers['value'] == 3:
                    grade = 0
                    count = 0
                    for cl in Class.display_student_classes(student.id):
                        count +=1
                        grade+=cl.grade
                    print(grade/count)
                else:
                    in_options = False
    elif i1 == "teacher":
        i2 = input("Log in with id: ")
        teacher = Teacher.read_one(int(i2))
        if teacher:
            questions = [
            inquirer.List("value",
                          message="What would you like to do?",
                        choices=[('Grade',1),('exit',2)],
                        )
            ]
            answer = inquirer.prompt(questions)
            if answer['value'] == 1:
                classes_for_teach = Class.display_teacher_classes(teacher.id)
                # (f"{cl.topic}: {cl.student_id}, {cl.grade}", cl)
                choice_list = [(f"{cl.topic}: {cl.student_id}, {cl.grade}", cl) for cl in classes_for_teach]
                questions = [
                inquirer.List("value",
                          message="Which class?",
                          choices=choice_list,
                        )
                ]
                answer = inquirer.prompt(questions)
                i4 = input(Back.RED+Fore.BLUE+"What is their new grade? ")
                answer["value"].grade = float(i4)
                answer["value"].update()

                          


