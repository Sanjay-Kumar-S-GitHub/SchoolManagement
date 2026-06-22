from Storage.Data import classrooms, students, saveClassrooms, saveStudents
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
        valid_capacity=False
        capacity=None
        while valid_capacity is False:
            capacity=input('Enter classroom capacity: ')
            if capacity.isdigit() and int(capacity)>0:
                valid_capacity=True
                capacity=int(capacity)
            else:
                print('Invalid capacity')
        createdClassroom=Classroom(class_id,capacity)
        classrooms.append(createdClassroom)
        saveClassrooms()
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
                    if student.class_id==class_id:
                        student.class_id=None
                saveClassrooms()
                saveStudents()
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
                print(f"capacity: {classroom.capacity}")
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
        import pandas as pd
        data=[]
        for classroom in classrooms:
            has_students=False
            for student in students:
                if student.class_id==classroom.class_id:
                    data.append([classroom.class_id,classroom.capacity,student.student_id,student.student_name])
                    has_students=True
            if not has_students:
                data.append([classroom.class_id,classroom.capacity,'None','None'])
        df=pd.DataFrame(data,columns=['Class ID','Capacity','Student ID','Student Name'])
        print(df.to_string(index=False))
        print("\n")