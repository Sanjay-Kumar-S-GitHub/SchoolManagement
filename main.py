from EntityManager.ClassroomManager import ClassroomManager
from EntityManager.TeacherManager import TeacherManager
from EntityManager.StudentManager import StudentManager
from EntityManager.SubjectManager import SubjectManager

def main():
    studentManager=StudentManager()
    teacherManager=TeacherManager()
    subjectManager=SubjectManager()
    classroomManager=ClassroomManager()
    while True:
        print("Menu:")
        print("1. Manage classrooms")
        print("2. Manage subjects")
        print("3. Manage teachers")
        print("4. Manage students")
        option=input("Select an option from above: ")
        if option=='1':
            again=True
            while again:
                print("\n")
                print("Classroom Menu:")
                print("1. Add classroom")
                print("2. Remove classroom")
                print("3. View classroom")
                print("4. Exit to main menu")
                option1=input("Select an option from above: ")
                if option1=='1':
                    classroomManager.addClassroom()
                    validYN=False
                    while validYN is False:
                        exit=input('Do you want to exit: (Y/N): ').upper()
                        if exit=='Y':
                            validYN=True
                            again=False
                        elif exit=='N':
                            validYN=True
                        else:
                            print('Invalid input for Y/N')
                elif option1=='2':
                    classroomManager.removeClassroom()
                    validYN=False
                    while validYN is False:
                        exit=input('Do you want to exit: (Y/N): ').upper()
                        if exit=='Y':
                            validYN=True
                            again=False
                        elif exit=='N':
                            validYN=True
                        else:
                            print('Invalid input for Y/N')
                elif option1=='3':
                    classroomManager.viewClassroom()
                    validYN=False
                    while validYN is False:
                        exit=input('Do you want to exit: (Y/N): ').upper()
                        if exit=='Y':
                            validYN=True
                            again=False
                        elif exit=='N':
                            validYN=True
                        else:
                            print('Invalid input for Y/N')
                elif option1=='4':
                    again=False
                else:
                    print("Invalid input")  
            print("\n")
        elif option=='2':
            again=True
            while again:
                print("\n")
                print("Subjects Menu:")
                print("1. Add subject")
                print("2. Remove subject")
                print("3. View subject")
                print("4. edit subject")
                print("5. Exit to main menu")
                option2=input("Select an option from above: ")
                if option2=='1':
                    subjectManager.addSubject()
                    validYN=False
                    while validYN is False:
                        exit=input('Do you want to exit: (Y/N): ').upper()
                        if exit=='Y':
                            validYN=True
                            again=False
                        elif exit=='N':
                            validYN=True
                        else:
                            print('Invalid input for Y/N')
                elif option2=='2':
                    subjectManager.removeSubject()
                    validYN=False
                    while validYN is False:
                        exit=input('Do you want to exit: (Y/N): ').upper()
                        if exit=='Y':
                            validYN=True
                            again=False
                        elif exit=='N':
                            validYN=True
                        else:
                            print('Invalid input for Y/N')
                elif option2=='3':
                    subjectManager.viewSubject()
                    validYN=False
                    while validYN is False:
                        exit=input('Do you want to exit: (Y/N): ').upper()
                        if exit=='Y':
                            validYN=True
                            again=False
                        elif exit=='N':
                            validYN=True
                        else:
                            print('Invalid input for Y/N')
                elif option2=='4':
                    subjectManager.editSubject()
                    validYN=False
                    while validYN is False:
                        exit=input('Do you want to exit: (Y/N): ').upper()
                        if exit=='Y':
                            validYN=True
                            again=False
                        elif exit=='N':
                            validYN=True
                        else:
                            print('Invalid input for Y/N')
                elif option2=='5':
                    again=False
                else:
                    print("Invalid input")  
            print("\n")
        elif option=='3':
            again=True
            while again:
                print("\n")
                print("Teachers Menu:")
                print("1. Add teacher")
                print("2. Remove teacher")
                print("3. View teacher")
                print("4. edit teacher")
                print("5. Exit to main menu")
                option3=input("Select an option from above: ")
                if option3=='1':
                    teacherManager.addTeacher()
                    validYN=False
                    while validYN is False:
                        exit=input('Do you want to exit: (Y/N): ').upper()
                        if exit=='Y':
                            validYN=True
                            again=False
                        elif exit=='N':
                            validYN=True
                        else:
                            print('Invalid input for Y/N')
                elif option3=='2':
                    teacherManager.removeTeacher()
                    validYN=False
                    while validYN is False:
                        exit=input('Do you want to exit: (Y/N): ').upper()
                        if exit=='Y':
                            validYN=True
                            again=False
                        elif exit=='N':
                            validYN=True
                        else:
                            print('Invalid input for Y/N')
                elif option3=='3':
                    teacherManager.viewTeacher()
                    validYN=False
                    while validYN is False:
                        exit=input('Do you want to exit: (Y/N): ').upper()
                        if exit=='Y':
                            validYN=True
                            again=False
                        elif exit=='N':
                            validYN=True
                        else:
                            print('Invalid input for Y/N')
                elif option3=='4':
                    teacherManager.editTeacher()
                    validYN=False
                    while validYN is False:
                        exit=input('Do you want to exit: (Y/N): ').upper()
                        if exit=='Y':
                            validYN=True
                            again=False
                        elif exit=='N':
                            validYN=True
                        else:
                            print('Invalid input for Y/N')
                elif option3=='5':
                    again=False
                else:
                    print("Invalid input")  
                print("\n")
        elif option=='4':
            again=True
            while again:
                print("\n")
                print("Students Menu:")
                print("1. Add student")
                print("2. Remove student")
                print("3. View student")
                print("4. edit student")
                print("5. Exit to main menu")
                option4=input("Select an option from above: ")
                if option4=='1':
                    studentManager.addStudent()
                    validYN=False
                    while validYN is False:
                        exit=input('Do you want to exit: (Y/N): ').upper()
                        if exit=='Y':
                            validYN=True
                            again=False
                        elif exit=='N':
                            validYN=True
                        else:
                            print('Invalid input for Y/N')
                elif option4=='2':
                    studentManager.removeStudent()
                    validYN=False
                    while validYN is False:
                        exit=input('Do you want to exit: (Y/N): ').upper()
                        if exit=='Y':
                            validYN=True
                            again=False
                        elif exit=='N':
                            validYN=True
                        else:
                            print('Invalid input for Y/N')
                elif option4=='3':
                    studentManager.viewStudent()
                    validYN=False
                    while validYN is False:
                        exit=input('Do you want to exit: (Y/N): ').upper()
                        if exit=='Y':
                            validYN=True
                            again=False
                        elif exit=='N':
                            validYN=True
                        else:
                            print('Invalid input for Y/N')
                elif option4=='4':
                    studentManager.editStudent()
                    validYN=False
                    while validYN is False:
                        exit=input('Do you want to exit: (Y/N): ').upper()
                        if exit=='Y':
                            validYN=True
                            again=False
                        elif exit=='N':
                            validYN=True
                        else:
                            print('Invalid input for Y/N')
                elif option4=='5':
                    again=False
                else:
                    print("Invalid input")  
                print("\n")
        else:
            print("Invalid input")
        print("\n")

main()