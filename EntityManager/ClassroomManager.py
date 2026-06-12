from Storage.Data import classrooms, students
from Entities.Classroom import Classroom

class ClassroomManager:
    def addClassroom(self):
        valid=False
        while valid is False:
            class_id=input('Enter class id: ')
            if len(class_id)!=1 or not class_id.isalpha():
                print('Invalid class id')
                continue
            class_id=class_id.upper()
            exists=False
            for classroom in classrooms:
                if classroom.class_id==class_id:
                    exists=True
                    break
            if exists:
                print('Class id already exists')
            else:
                valid=True
        createdClassroom=Classroom(class_id)
        classrooms.append(createdClassroom)
        print('Classroom added successfully')

    def removeClassroom(self):
        class_id=input('Enter class id: ')
        if len(class_id)!=1 or not class_id.isalpha():
            print('Invalid class id')
            return
        not_found=True
        for classroom in classrooms:
            if classroom.class_id==class_id:
                classrooms.remove(classroom)
                for student in students:
                    if student.class_id==student.class_id:
                        student.class_id=None
                print(f"Classroom with class id: {class_id} removed successfully")
                not_found=False
                break
        if not_found:
            print(f"No classroom with class id: {class_id} found")

    def viewClassroom(self):
        class_id=input('Enter class id: ')
        if len(class_id)!=1 or not class_id.isalpha():
            print('Invalid class id')
            return
        not_found=True
        for classroom in classrooms:
            if classroom.class_id==class_id:
                print(f"class id: {classroom.class_id}")
                student_count=0
                for student in students:
                    if student.class_id==classroom.class_id:
                        print(f"Student id: {student.student_id}")
                        print(f"Student name: {student.student_name}")
                        student_count+=1
                        teacher_not_found=False
                    print("\n")
                print(f"Student count: {student_count}")
                not_found=False
                break
        if not_found:
            print(f"No classroom with class id: {class_id} found")

    def viewAllClassrooms(self):
        if len(classrooms)==0:
            print('No classrooms found')
            return
        for classroom in classrooms:
            print(f"class id: {classroom.class_id}")
            student_count=0
            for student in students:
                if student.class_id==classroom.class_id:
                    print(f"Student id: {student.student_id}")
                    print(f"Student name: {student.student_name}")
                    student_count+=1
            print(f"Student count: {student_count}")
            print("\n")