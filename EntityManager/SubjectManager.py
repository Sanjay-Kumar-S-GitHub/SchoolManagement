from Entities.SubjectEntity import Subject
# from Entities.TeacherEntity import Teacher
from Storage.Data import subjects, teachers

class SubjectManager:
    def addSubject(self):
        subject_id=input('Enter subject id: ')
        subject_name=input('Enter subject name: ')
        createdSubject=Subject(subject_id,subject_name)
        subjects.append(createdSubject)
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
                        new_subject_name=input("Enter the new name of the subject: ")
                        subject.subject_name=new_subject_name
                        query_done=True
                    elif name_edit=='N':
                        query_done=True
                    else:
                        print("Invalid input")  
                not_found=False
        if not_found:
            print(f"No student with subject id: {subject_id} found")