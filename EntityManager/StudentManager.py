from Entities.StudentEntity import Student
from Storage.Data import students, classrooms

class StudentManager:
    def addStudent(self):
        student_id=input('Enter student id: ')
        student_name=input('Enter student name: ')
        valid_class_id=False
        class_id=None
        while valid_class_id is False:
            class_id=input('Enter class id: ')
            for classroom in classrooms:
                if classroom.class_id==class_id:
                    valid_class_id=True
                    break
        createdStudent=Student(student_id,student_name,class_id)
        students.append(createdStudent)
        print('Student added successfully')

    def removeStudent(self):
        student_id=input('Enter student id: ')
        not_found=True
        for student in students:
            if student.student_id==student_id:
                students.remove(student)
                print(f"Student with student id: {student_id} removed successfully")
                not_found=False
                break
        if not_found:
            print(f"No student with student id: {student_id} found")

    def viewStudent(self):
        print(students)
        student_id=input('Enter student id: ')
        not_found=True
        for student in students:
            if student.student_id==student_id:
                print(f"Student id: {student.student_id}")
                print(f"Student name: {student.student_name}")
                print(f"class id: {student.class_id}")
                not_found=False
                break
        if not_found:
            print(f"No student with student id: {student_id} found")

    def editStudent(self):
        student_id=input('Enter student id: ')
        not_found=True
        for student in students:
            if student.student_id==student_id:
                query_done=False
                while query_done is False:
                    name_edit=input("Want to edit student name (Y/N): ").upper()
                    if name_edit=='Y':
                        new_student_name=input("Enter the new name of the student: ")
                        student.student_name=new_student_name
                        query_done=True
                    elif name_edit=='N':
                        query_done=True
                    else:
                        print("Invalid input")
                query_done=False
                while query_done is False:
                    class_id_edit=input("Want to edit student class (Y/N): ").upper()
                    if class_id_edit=='Y':
                        valid_class_id=False
                        while valid_class_id is False:
                            new_class_id=input("Enter the new class id of the student: ")
                            for classroom in classrooms:
                                if classroom.class_id==new_class_id:
                                    valid_class_id=True
                                    student.class_id=new_class_id
                                    break
                        query_done=True
                    elif name_edit=='N':
                        query_done=True
                    else:
                        print("Invalid input")
                not_found=False
                break
        if not_found:
            print(f"No student with student id: {student_id} found")