from Storage.Data import exams, classrooms, subjects, students
from Entities.ExamEntity import Exam

class ExamManager:
    def addExamMarks(self):
        if len(classrooms)==0:
            print('No classrooms available')
            return
        if len(subjects)==0:
            print('No subjects available')
            return
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
        valid_subject_id=False
        subject_id=None
        while valid_subject_id is False:
            subject_id=input('Enter subject id: ')
            if not subject_id.isdigit():
                print('Invalid subject id')
                continue
            for subject in subjects:
                if subject.subject_id==subject_id:
                    valid_subject_id=True
                    break
            if valid_subject_id is False:
                print('Invalid subject id')
        class_students=[]
        for student in students:
            if student.class_id==class_id:
                class_students.append(student)
        if len(class_students)==0:
            print('No students in this class')
            return
        marks={}
        for student in class_students:
            valid_marks=False
            while valid_marks is False:
                try:
                    mark=float(input(f"Enter marks for student {student.student_name} (ID: {student.student_id}): "))
                    if 0<=mark<=100:
                        marks[student.student_id]=mark
                        valid_marks=True
                    else:
                        print('Marks should be between 0 and 100')
                except ValueError:
                    print('Invalid marks')
        exists=False
        for exam in exams:
            if exam.class_id==class_id and exam.subject_id==subject_id:
                exam.marks=marks
                exists=True
                break
        if not exists:
            createdExam=Exam(class_id,subject_id,marks)
            exams.append(createdExam)
        print('Exam marks added successfully')

    def viewExamMarksByClass(self):
        valid_class_id=False
        class_id=None
        while valid_class_id is False:
            class_id=input('Enter class id: ')
            if len(class_id)!=1 or not class_id.isalpha():
                print('Invalid class id')
                continue
            for classroom in classrooms:
                if classroom.class_id==class_id:
                    valid_class_id=True
                    break
            if valid_class_id is False:
                print('Invalid class id')
        found=False
        import pandas as pd
        data=[]
        for exam in exams:
            if exam.class_id==class_id:
                subject_name=None
                for subject in subjects:
                    if subject.subject_id==exam.subject_id:
                        subject_name=subject.subject_name
                        break
                for student_id,mark in exam.marks.items():
                    student_name=None
                    for student in students:
                        if student.student_id==student_id:
                            student_name=student.student_name
                            break
                    data.append([exam.subject_id,subject_name,student_id,student_name,mark])
                found=True
        if found:
            df=pd.DataFrame(data,columns=['Subject ID','Subject Name','Student ID','Student Name','Marks'])
            print(df.to_string(index=False))
            print("\n")
        else:
            print(f"No exam marks found for class id: {class_id}")

    def viewExamMarksBySubject(self):
        valid_subject_id=False
        subject_id=None
        while valid_subject_id is False:
            subject_id=input('Enter subject id: ')
            if not subject_id.isdigit():
                print('Invalid subject id')
                continue
            for subject in subjects:
                if subject.subject_id==subject_id:
                    valid_subject_id=True
                    break
            if valid_subject_id is False:
                print('Invalid subject id')
        found=False
        import pandas as pd
        data=[]
        for exam in exams:
            if exam.subject_id==subject_id:
                subject_name=None
                for subject in subjects:
                    if subject.subject_id==exam.subject_id:
                        subject_name=subject.subject_name
                        break
                for student_id,mark in exam.marks.items():
                    student_name=None
                    for student in students:
                        if student.student_id==student_id:
                            student_name=student.student_name
                            break
                    data.append([exam.class_id,exam.subject_id,subject_name,student_id,student_name,mark])
                found=True
        if found:
            df=pd.DataFrame(data,columns=['Class ID','Subject ID','Subject Name','Student ID','Student Name','Marks'])
            print(df.to_string(index=False))
            print("\n")
        else:
            print(f"No exam marks found for subject id: {subject_id}")

    def editExamMarks(self):
        if len(classrooms)==0:
            print('No classrooms available')
            return
        if len(subjects)==0:
            print('No subjects available')
            return
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
        valid_subject_id=False
        subject_id=None
        while valid_subject_id is False:
            subject_id=input('Enter subject id: ')
            if not subject_id.isdigit():
                print('Invalid subject id')
                continue
            for subject in subjects:
                if subject.subject_id==subject_id:
                    valid_subject_id=True
                    break
            if valid_subject_id is False:
                print('Invalid subject id')
        class_students=[]
        for student in students:
            if student.class_id==class_id:
                class_students.append(student)
        if len(class_students)==0:
            print('No students in this class')
            return
        found_exam=None
        for exam in exams:
            if exam.class_id==class_id and exam.subject_id==subject_id:
                found_exam=exam
                break
        if found_exam is None:
            print('No exam marks found for this class and subject')
            return
        for student in class_students:
            query_done=False
            while query_done is False:
                mark_edit=input(f"Want to edit marks for student {student.student_name} (ID: {student.student_id}) (Y/N): ").upper()
                if mark_edit=='Y':
                    valid_marks=False
                    while valid_marks is False:
                        try:
                            mark=float(input(f"Enter marks for student {student.student_name} (ID: {student.student_id}): "))
                            if 0<=mark<=100:
                                found_exam.marks[student.student_id]=mark
                                valid_marks=True
                            else:
                                print('Marks should be between 0 and 100')
                        except ValueError:
                            print('Invalid marks')
                    query_done=True
                elif mark_edit=='N':
                    query_done=True
                else:
                    print('Invalid input')
        print('Exam marks edited successfully')