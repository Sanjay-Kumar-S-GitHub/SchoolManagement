from Storage.Data import teachers, subjects
from Entities.TeacherEntity import Teacher

class TeacherManager:
    def addTeacher(self):
        if len(subjects)==0:
            print('No subjects available. Please add a subject first.')
            return
        valid=False
        while valid is False:
            teacher_id=input('Enter teacher id: ')
            if not teacher_id.isdigit():
                print('Invalid teacher id')
                continue
            exists=False
            for teacher in teachers:
                if teacher.teacher_id==teacher_id:
                    exists=True
                    break
            if exists:
                print('Teacher id already exists')
            else:
                valid=True
        valid_name=False
        while valid_name is False:
            teacher_name=input('Enter teacher name: ')
            if not teacher_name.replace(' ', '').isalpha() or teacher_name.strip()=='':
                print('Invalid teacher name')
            else:
                valid_name=True
        valid_subject_id=False
        subject_id=None
        while valid_subject_id is False:
            subject_id=input('Enter subject id: ')
            for subject in subjects:
                if subject.subject_id==subject_id:
                    valid_subject_id=True
                    break
            if valid_subject_id is False:
                print('Invalid subject id')
        createdTeacher=Teacher(teacher_id,teacher_name,subject_id)
        teachers.append(createdTeacher)
        print('Teacher added successfully')

    def removeTeacher(self):
        teacher_id=input('Enter teacher id: ')
        not_found=True
        for teacher in teachers:
            if teacher.teacher_id==teacher_id:
                teachers.remove(teacher)
                print(f"Teacher with teacher id: {teacher_id} removed successfully")
                not_found=False
                break
        if not_found:
            print(f"No teacher with teacher id: {teacher_id} found")

    def viewTeacher(self):
        teacher_id=input('Enter teacher id: ')
        not_found=True
        for teacher in teachers:
            if teacher.teacher_id==teacher_id:
                print(f"teacher id: {teacher.teacher_id}")
                print(f"teacher name: {teacher.teacher_name}")
                subject_not_found=True
                for subject in subjects:
                    if subject.subject_id==teacher.subject_id:
                        print(f"Subject id: {subject.subject_id}")
                        print(f"subject name: {subject.subject_name}")
                        subject_not_found=False
                if subject_not_found:
                    print('No subject assigned to this teacher')
                not_found=False
                break
        if not_found:
            print(f"No teacher with teacher id: {teacher_id} found")

    def editTeacher(self):
        teacher_id=input('Enter teacher id: ')
        not_found=True
        for teacher in teachers:
            if teacher.teacher_id==teacher_id:
                query_done=False
                while query_done is False:
                    name_edit=input("Want to edit teacher name (Y/N): ").upper()
                    if name_edit=='Y':
                        valid_new_name=False
                        while valid_new_name is False:
                            new_teacher_name=input("Enter the new name of the teacher: ")
                            if not new_teacher_name.replace(' ', '').isalpha() or new_teacher_name.strip()=='':
                                print('Invalid teacher name')
                            else:
                                teacher.teacher_name=new_teacher_name
                                valid_new_name=True
                        query_done=True
                    elif name_edit=='N':
                        query_done=True
                    else:
                        print("Invalid input")
                query_done=False
                while query_done is False:
                    subject_id_edit=input("Want to edit teacher subject (Y/N): ").upper()
                    if subject_id_edit=='Y':
                        valid_subject_id=False
                        while valid_subject_id is False:
                            new_subject_id=input("Enter the new subject id of the student: ")
                            for subject in subjects:
                                if subject.subject_id==new_subject_id:
                                    teacher.subject_id=new_subject_id
                                    valid_subject_id=True
                                    break
                            if valid_subject_id is False:
                                print('Invalid subject id')
                        query_done=True
                    elif name_edit=='N' or subject_id_edit=='N':
                        query_done=True
                    else:
                        print("Invalid input")
                not_found=False
                break
        if not_found:
            print(f"No teacher with teacher id: {teacher_id} found")

    def viewAllTeachers(self):
        if len(teachers)==0:
            print('No teachers found')
            return
        import pandas as pd
        data=[]
        for teacher in teachers:
            subject_found=False
            for subject in subjects:
                if subject.subject_id==teacher.subject_id:
                    data.append([teacher.teacher_id,teacher.teacher_name,subject.subject_id,subject.subject_name])
                    subject_found=True
            if not subject_found:
                data.append([teacher.teacher_id,teacher.teacher_name,'None','No subject assigned'])
        df=pd.DataFrame(data,columns=['Teacher ID','Teacher Name','Subject ID','Subject Name'])
        print(df.to_string(index=False))
        print("\n")