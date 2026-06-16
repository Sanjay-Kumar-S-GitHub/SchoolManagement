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
            target_classroom=None
            for classroom in classrooms:
                if classroom.class_id==class_id:
                    target_classroom=classroom
                    break
            if target_classroom is None:
                print('Invalid class id')
                continue
            current_count=0
            for student in students:
                if student.class_id==class_id:
                    current_count+=1
            if current_count>=target_classroom.capacity:
                print('Classroom is at full capacity')
            else:
                valid_class_id=True
        valid_phone=False
        phone_number=None
        while valid_phone is False:
            phone_number=input('Enter phone number: ')
            if phone_number.isdigit() and len(phone_number)==10:
                valid_phone=True
            else:
                print('Invalid phone number')
        valid_email=False
        email=None
        while valid_email is False:
            email=input('Enter email: ')
            if '@' in email and '.' in email.split('@')[-1] and email.strip()!='':
                valid_email=True
            else:
                print('Invalid email')
        valid_dob=False
        date_of_birth=None
        while valid_dob is False:
            date_of_birth=input('Enter date of birth (YYYY-MM-DD): ')
            try:
                import datetime
                datetime.datetime.strptime(date_of_birth,'%Y-%m-%d')
                valid_dob=True
            except ValueError:
                print('Invalid date of birth')
        valid_gender=False
        gender=None
        while valid_gender is False:
            gender=input('Enter gender (M/F/O): ').upper()
            if gender in ['M','F','O']:
                valid_gender=True
            else:
                print('Invalid gender')
        valid_guardian=False
        guardian_name=None
        while valid_guardian is False:
            guardian_name=input('Enter guardian name: ')
            if not guardian_name.replace(' ', '').isalpha() or guardian_name.strip()=='':
                print('Invalid guardian name')
            else:
                valid_guardian=True
        createdStudent=Student(student_id,student_name,class_id,phone_number,email,date_of_birth,gender,guardian_name)
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
                print(f"Email: {student.email}")
                print(f"Date of birth: {student.date_of_birth}")
                print(f"Gender: {student.gender}")
                print(f"Guardian name: {student.guardian_name}")
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
                            target_classroom=None
                            for classroom in classrooms:
                                if classroom.class_id==new_class_id:
                                    target_classroom=classroom
                                    break
                            if target_classroom is None:
                                print('Invalid class id')
                                continue
                            current_count=0
                            for other in students:
                                if other.class_id==new_class_id and other.student_id!=student.student_id:
                                    current_count+=1
                            if current_count>=target_classroom.capacity:
                                print('Classroom is at full capacity')
                            else:
                                valid_class_id=True
                                student.class_id=new_class_id
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
                query_done=False
                while query_done is False:
                    email_edit=input("Want to edit student email (Y/N): ").upper()
                    if email_edit=='Y':
                        valid_email=False
                        while valid_email is False:
                            new_email=input("Enter the new email of the student: ")
                            if '@' in new_email and '.' in new_email.split('@')[-1] and new_email.strip()!='':
                                student.email=new_email
                                valid_email=True
                            else:
                                print("Invalid email")
                        query_done=True
                    elif name_edit=='N' or email_edit=='N':
                        query_done=True
                    else:
                        print("Invalid input")
                query_done=False
                while query_done is False:
                    dob_edit=input("Want to edit student date of birth (Y/N): ").upper()
                    if dob_edit=='Y':
                        valid_dob=False
                        while valid_dob is False:
                            new_dob=input("Enter the new date of birth of the student (YYYY-MM-DD): ")
                            try:
                                import datetime
                                datetime.datetime.strptime(new_dob,'%Y-%m-%d')
                                student.date_of_birth=new_dob
                                valid_dob=True
                            except ValueError:
                                print("Invalid date of birth")
                        query_done=True
                    elif name_edit=='N' or dob_edit=='N':
                        query_done=True
                    else:
                        print("Invalid input")
                query_done=False
                while query_done is False:
                    gender_edit=input("Want to edit student gender (Y/N): ").upper()
                    if gender_edit=='Y':
                        valid_gender=False
                        while valid_gender is False:
                            new_gender=input("Enter the new gender of the student (M/F/O): ").upper()
                            if new_gender in ['M','F','O']:
                                student.gender=new_gender
                                valid_gender=True
                            else:
                                print("Invalid gender")
                        query_done=True
                    elif name_edit=='N' or gender_edit=='N':
                        query_done=True
                    else:
                        print("Invalid input")
                query_done=False
                while query_done is False:
                    guardian_edit=input("Want to edit student guardian name (Y/N): ").upper()
                    if guardian_edit=='Y':
                        valid_guardian=False
                        while valid_guardian is False:
                            new_guardian=input("Enter the new guardian name of the student: ")
                            if not new_guardian.replace(' ', '').isalpha() or new_guardian.strip()=='':
                                print("Invalid guardian name")
                            else:
                                student.guardian_name=new_guardian
                                valid_guardian=True
                        query_done=True
                    elif name_edit=='N' or guardian_edit=='N':
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
        import pandas as pd
        data=[]
        for student in students:
            data.append([student.student_id,student.student_name,student.class_id,student.phone_number,student.email,student.date_of_birth,student.gender,student.guardian_name])
        df=pd.DataFrame(data,columns=['Student ID','Student Name','Class ID','Phone Number','Email','Date of Birth','Gender','Guardian Name'])
        print(df.to_string(index=False))
        print("\n")