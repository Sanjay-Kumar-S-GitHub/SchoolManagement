from Entities.SubjectEntity import Subject
# from Entities.TeacherEntity import Teacher
from Storage.Data import subjects, teachers, saveSubjects, saveTeachers

class SubjectManager:
    def addSubject(self):
        valid=False
        while valid is False:
            subject_id=input('Enter subject id: ')
            if not subject_id.isdigit():
                print('Invalid subject id')
                continue
            exists=False
            for subject in subjects:
                if subject.subject_id==subject_id:
                    exists=True
                    break
            if exists:
                print('Subject id already exists')
            else:
                valid=True
        valid_name=False
        while valid_name is False:
            subject_name=input('Enter subject name: ')
            if not subject_name.replace(' ', '').isalpha() or subject_name.strip()=='':
                print('Invalid subject name')
            else:
                valid_name=True
        createdSubject=Subject(subject_id,subject_name)
        subjects.append(createdSubject)
        saveSubjects()
        print('Subject added successfully')

    def removeSubject(self):
        subject_id=input('Enter subject id: ')
        not_found=True
        for subject in subjects:
            if subject.subject_id==subject_id:
                subjects.remove(subject)
                for teacher in teachers:
                    if teacher.subject_id==subject.subject_id:
                        teacher.subject_id=None
                saveSubjects()
                saveTeachers()
                print(f"Subject with subject id: {subject_id} removed successfully")
                not_found=False
                break
        if not_found:
            print(f"No subject with subject id: {subject_id} found")

    def viewSubject(self):
        subject_id=input('Enter subject id: ')
        not_found=True
        for subject in subjects:
            if subject.subject_id==subject_id:
                print(f"Subject id: {subject.subject_id}")
                print(f"Subject name: {subject.subject_name}")
                teacher_not_found=True
                for teacher in teachers:
                    if teacher.subject_id==subject.subject_id:
                        print(f"Teacher name: {teacher.teacher_name}")
                        teacher_not_found=False
                if teacher_not_found:
                    print("No teacher is assigned for this subject")
                not_found=False
                break
        if not_found:
            print(f"No student with subject id: {subject_id} found")

    def editSubject(self):
        subject_id=input('Enter subject id: ')
        not_found=True
        for subject in subjects:
            if subject.subject_id==subject_id:
                query_done=False
                while query_done is False:
                    name_edit=input("Want to edit stubject name (Y/N): ").upper()
                    if name_edit=='Y':
                        valid_new_name=False
                        while valid_new_name is False:
                            new_subject_name=input("Enter the new name of the subject: ")
                            if not new_subject_name.replace(' ', '').isalpha() or new_subject_name.strip()=='':
                                print('Invalid subject name')
                            else:
                                subject.subject_name=new_subject_name
                                valid_new_name=True
                        query_done=True
                    elif name_edit=='N':
                        query_done=True
                    else:
                        print("Invalid input")  
                saveSubjects()
                not_found=False
        if not_found:
            print(f"No student with subject id: {subject_id} found")

    def viewAllSubjects(self):
        if len(subjects)==0:
            print('No subjects found')
            return
        import pandas as pd
        data=[]
        for subject in subjects:
            teacher_found=False
            for teacher in teachers:
                if teacher.subject_id==subject.subject_id:
                    data.append([subject.subject_id,subject.subject_name,teacher.teacher_name])
                    teacher_found=True
            if not teacher_found:
                data.append([subject.subject_id,subject.subject_name,'No teacher assigned'])
        df=pd.DataFrame(data,columns=['Subject ID','Subject Name','Teacher Name'])
        print(df.to_string(index=False))
        print("\n")