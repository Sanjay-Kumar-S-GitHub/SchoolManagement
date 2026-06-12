from Entities.StudentEntity import Student
from Storage.Data import students, classrooms

class StudentManager:
    def addStudent(self):
        if len(classrooms)==0:
            print('No classrooms available. Please add a classroom first.')
            return
        valid=False
        while valid is False:
            student_id=input('Enter student id: ')
            if not student_id.isdigit():
                print('Invalid student id')
                continue
            exists=False
            for student in students:
                if student.student_id==student_id:
                    exists=True
                    break
            if exists:
                print('Student id already exists')
            else:
                valid=True
        valid_name=False
        while valid_name is False:
            student_name=input('Enter student name: ')
            if not student_name.replace(' ', '').isalpha() or student_name.strip()=='':
                print('Invalid student name')
            else:
                valid_name=True
        valid_class_id=False
        class_id=None
        while valid_class_id is False:
            class_id=input('Enter class id: ')
            if len(class_id)!=1 or not class_id.isalpha():
                print('Invalid class id')
                continue
            class_id=class_id.upper()
            for classroom in classrooms:
                if classroom.class_id==class_id:
                    valid_class_id=True
                    break
            if valid_class_id is False:
                print('Invalid class id')
        valid_phone=False
        phone_number=None
        while valid_phone is False:
            phone_number=input('Enter phone number: ')
            if phone_number.isdigit() and len(phone_number)==10:
                valid_phone=True
            else:
                print('Invalid phone number')
        createdStudent=Student(student_id,student_name,class_id,phone_number)
        students.append(createdStudent)
        print('Student added successfully')

    def removeStudent(self):
        student_id=input('Enter student id: ')
        if not student_id.isdigit():
            print('Invalid student id')
            return
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
        student_id=input('Enter student id: ')
        if not student_id.isdigit():
            print('Invalid student id')
            return
        not_found=True
        for student in students:
            if student.student_id==student_id:
                print(f"Student id: {student.student_id}")
                print(f"Student name: {student.student_name}")
                print(f"class id: {student.class_id}")
                print(f"Phone number: {student.phone_number}")
                not_found=False
                break
        if not_found:
            print(f"No student with student id: {student_id} found")

    def editStudent(self):
        student_id=input('Enter student id: ')
        if not student_id.isdigit():
            print('Invalid student id')
            return
        not_found=True
        for student in students:
            if student.student_id==student_id:
                query_done=False
                while query_done is False:
                    name_edit=input("Want to edit student name (Y/N): ").upper()
                    if name_edit=='Y':
                        valid_new_name=False
                        while valid_new_name is False:
                            new_student_name=input("Enter the new name of the student: ")
                            if not new_student_name.replace(' ', '').isalpha() or new_student_name.strip()=='':
                                print('Invalid student name')
                            else:
                                student.student_name=new_student_name
                                valid_new_name=True
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
                            if len(new_class_id)!=1 or not new_class_id.isalpha():
                                print('Invalid class id')
                                continue
                            new_class_id=new_class_id.upper()
                            for classroom in classrooms:
                                if classroom.class_id==new_class_id:
                                    valid_class_id=True
                                    student.class_id=new_class_id
                                    break
                            if valid_class_id is False:
                                print('Invalid class id')
                        query_done=True
                    elif name_edit=='N' or class_id_edit=='N':
                        query_done=True
                    else:
                        print("Invalid input")
                query_done=False
                while query_done is False:
                    phone_edit=input("Want to edit student phone number (Y/N): ").upper()
                    if phone_edit=='Y':
                        valid_phone=False
                        while valid_phone is False:
                            new_phone=input("Enter the new phone number of the student: ")
                            if new_phone.isdigit() and len(new_phone)==10:
                                student.phone_number=new_phone
                                valid_phone=True
                            else:
                                print("Invalid phone number")
                        query_done=True
                    elif name_edit=='N' or phone_edit=='N':
                        query_done=True
                    else:
                        print("Invalid input")
                not_found=False
                break
        if not_found:
            print(f"No student with student id: {student_id} found")

    def viewAllStudents(self):
        if len(students)==0:
            print('No students found')
            return
        for student in students:
            print(f"Student id: {student.student_id}")
            print(f"Student name: {student.student_name}")
            print(f"class id: {student.class_id}")
            print(f"Phone number: {student.phone_number}")
            print("\n")