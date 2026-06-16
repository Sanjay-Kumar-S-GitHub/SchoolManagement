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
        valid_name=False
        exam_name=None
        while valid_name is False:
            exam_name=input('Enter exam name: ')
            if exam_name.replace(' ', '').isalnum() and exam_name.strip()!='':
                valid_name=True
            else:
                print('Invalid exam name')
        valid_date=False
        exam_date=None
        while valid_date is False:
            exam_date=input('Enter exam date (YYYY-MM-DD): ')
            try:
                import datetime
                datetime.datetime.strptime(exam_date,'%Y-%m-%d')
                valid_date=True
            except ValueError:
                print('Invalid exam date')
        valid_max_marks=False
        max_marks=None
        while valid_max_marks is False:
            try:
                max_marks=float(input('Enter maximum marks: '))
                if max_marks>0:
                    valid_max_marks=True
                else:
                    print('Maximum marks must be positive')
            except ValueError:
                print('Invalid maximum marks')
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
                    if 0<=mark<=max_marks:
                        marks[student.student_id]=mark
                        valid_marks=True
                    else:
                        print(f"Marks should be between 0 and {max_marks}")
                except ValueError:
                    print('Invalid marks')
        exists=False
        for exam in exams:
            if exam.class_id==class_id and exam.subject_id==subject_id and exam.exam_name==exam_name:
                exam.marks=marks
                exam.exam_date=exam_date
                exam.max_marks=max_marks
                exists=True
                break
        if not exists:
            createdExam=Exam(class_id,subject_id,marks,exam_date,max_marks,exam_name)
            exams.append(createdExam)
        print('Exam marks added successfully')

    def viewExamMarks(self):
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
        class_exams=[]
        for exam in exams:
            if exam.class_id==class_id:
                class_exams.append(exam)
        if len(class_exams)==0:
            print(f"No exam marks found for class id: {class_id}")
            return
        available_subjects=set()
        for exam in class_exams:
            available_subjects.add(exam.subject_id)
        print("Available subject ids: " + ", ".join(sorted(list(available_subjects))))
        valid_subject_id=False
        subject_id=None
        while valid_subject_id is False:
            subject_id=input('Enter subject id: ')
            if subject_id in available_subjects:
                valid_subject_id=True
            else:
                print('Invalid subject id')
        sub_exams=[]
        for exam in class_exams:
            if exam.subject_id==subject_id:
                sub_exams.append(exam)
        available_names=set()
        for exam in sub_exams:
            available_names.add(exam.exam_name)
        print("Available exam names: " + ", ".join(sorted(list(available_names))))
        valid_exam_name=False
        exam_name=None
        while valid_exam_name is False:
            exam_name=input('Enter exam name: ')
            if exam_name in available_names:
                valid_exam_name=True
            else:
                print('Invalid exam name')
        target_exam=None
        for exam in sub_exams:
            if exam.exam_name==exam_name:
                target_exam=exam
                break
        subject_name=None
        for subject in subjects:
            if subject.subject_id==subject_id:
                subject_name=subject.subject_name
                break
        import pandas as pd
        data=[]
        for student_id,mark in target_exam.marks.items():
            student_name=None
            for student in students:
                if student.student_id==student_id:
                    student_name=student.student_name
                    break
            data.append([target_exam.class_id,target_exam.subject_id,subject_name,target_exam.exam_name,target_exam.exam_date,target_exam.max_marks,student_id,student_name,mark])
        df=pd.DataFrame(data,columns=['Class ID','Subject ID','Subject Name','Exam Name','Exam Date','Max Marks','Student ID','Student Name','Marks'])
        print(df.to_string(index=False))
        print("\n")

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
        valid_name=False
        exam_name=None
        while valid_name is False:
            exam_name=input('Enter exam name: ')
            if exam_name.replace(' ', '').isalnum() and exam_name.strip()!='':
                valid_name=True
            else:
                print('Invalid exam name')
        class_students=[]
        for student in students:
            if student.class_id==class_id:
                class_students.append(student)
        if len(class_students)==0:
            print('No students in this class')
            return
        found_exam=None
        for exam in exams:
            if exam.class_id==class_id and exam.subject_id==subject_id and exam.exam_name==exam_name:
                found_exam=exam
                break
        if found_exam is None:
            print('No exam marks found for this class and subject and exam name')
            return
        query_done=False
        while query_done is False:
            date_edit=input("Want to edit exam date (Y/N): ").upper()
            if date_edit=='Y':
                valid_date=False
                while valid_date is False:
                    new_date=input("Enter the new exam date (YYYY-MM-DD): ")
                    try:
                        import datetime
                        datetime.datetime.strptime(new_date,'%Y-%m-%d')
                        found_exam.exam_date=new_date
                        valid_date=True
                    except ValueError:
                        print("Invalid exam date")
                query_done=True
            elif date_edit=='N':
                query_done=True
            else:
                print("Invalid input")
        query_done=False
        while query_done is False:
            max_marks_edit=input("Want to edit maximum marks (Y/N): ").upper()
            if max_marks_edit=='Y':
                valid_max_marks=False
                while valid_max_marks is False:
                    try:
                        new_max_marks=float(input("Enter the new maximum marks: "))
                        if new_max_marks>0:
                            found_exam.max_marks=new_max_marks
                            valid_max_marks=True
                        else:
                            print("Maximum marks must be positive")
                    except ValueError:
                        print("Invalid maximum marks")
                query_done=True
            elif date_edit=='N' or max_marks_edit=='N':
                query_done=True
            else:
                print("Invalid input")
        for student in class_students:
            query_done=False
            while query_done is False:
                mark_edit=input(f"Want to edit marks for student {student.student_name} (ID: {student.student_id}) (Y/N): ").upper()
                if mark_edit=='Y':
                    valid_marks=False
                    while valid_marks is False:
                        try:
                            mark=float(input(f"Enter marks for student {student.student_name} (ID: {student.student_id}): "))
                            if 0<=mark<=found_exam.max_marks:
                                found_exam.marks[student.student_id]=mark
                                valid_marks=True
                            else:
                                print(f"Marks should be between 0 and {found_exam.max_marks}")
                        except ValueError:
                            print('Invalid marks')
                    query_done=True
                elif mark_edit=='N':
                    query_done=True
                else:
                    print('Invalid input')
        print('Exam marks edited successfully')