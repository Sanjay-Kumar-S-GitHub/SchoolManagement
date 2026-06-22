import json
import os
from Entities.StudentEntity import Student
from Entities.TeacherEntity import Teacher
from Entities.Classroom import Classroom
from Entities.SubjectEntity import Subject
from Entities.ExamEntity import Exam

DB_DIR=os.path.dirname(os.path.abspath(__file__))
STUDENTS_FILE=os.path.join(DB_DIR,'students.json')
TEACHERS_FILE=os.path.join(DB_DIR,'teachers.json')
CLASSROOMS_FILE=os.path.join(DB_DIR,'classrooms.json')
SUBJECTS_FILE=os.path.join(DB_DIR,'subjects.json')
EXAMS_FILE=os.path.join(DB_DIR,'exams.json')

students=[]
teachers=[]
classrooms=[]
subjects=[]
exams=[]

def saveStudents():
    data=[]
    for s in students:
        data.append({
            'student_id':s.student_id,
            'student_name':s.student_name,
            'class_id':s.class_id,
            'phone_number':s.phone_number,
            'email':s.email,
            'date_of_birth':s.date_of_birth,
            'gender':s.gender,
            'guardian_name':s.guardian_name
        })
    with open(STUDENTS_FILE,'w') as f:
        json.dump(data,f,indent=4)

def loadStudents():
    global students
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE,'r') as f:
            try:
                data=json.load(f)
                students=[Student(
                    s['student_id'],
                    s['student_name'],
                    s['class_id'],
                    s['phone_number'],
                    s['email'],
                    s['date_of_birth'],
                    s['gender'],
                    s['guardian_name']
                ) for s in data]
            except Exception:
                students=[]

def saveTeachers():
    data=[]
    for t in teachers:
        data.append({
            'teacher_id':t.teacher_id,
            'teacher_name':t.teacher_name,
            'subject_id':t.subject_id,
            'email':t.email,
            'phone_number':t.phone_number,
            'salary':t.salary
        })
    with open(TEACHERS_FILE,'w') as f:
        json.dump(data,f,indent=4)

def loadTeachers():
    global teachers
    if os.path.exists(TEACHERS_FILE):
        with open(TEACHERS_FILE,'r') as f:
            try:
                data=json.load(f)
                teachers=[Teacher(
                    t['teacher_id'],
                    t['teacher_name'],
                    t['subject_id'],
                    t['email'],
                    t['phone_number'],
                    t['salary']
                ) for t in data]
            except Exception:
                teachers=[]

def saveClassrooms():
    data=[]
    for c in classrooms:
        data.append({
            'class_id':c.class_id,
            'capacity':c.capacity
        })
    with open(CLASSROOMS_FILE,'w') as f:
        json.dump(data,f,indent=4)

def loadClassrooms():
    global classrooms
    if os.path.exists(CLASSROOMS_FILE):
        with open(CLASSROOMS_FILE,'r') as f:
            try:
                data=json.load(f)
                classrooms=[Classroom(
                    c['class_id'],
                    c['capacity']
                ) for c in data]
            except Exception:
                classrooms=[]

def saveSubjects():
    data=[]
    for s in subjects:
        data.append({
            'subject_id':s.subject_id,
            'subject_name':s.subject_name
        })
    with open(SUBJECTS_FILE,'w') as f:
        json.dump(data,f,indent=4)

def loadSubjects():
    global subjects
    if os.path.exists(SUBJECTS_FILE):
        with open(SUBJECTS_FILE,'r') as f:
            try:
                data=json.load(f)
                subjects=[Subject(
                    s['subject_id'],
                    s['subject_name']
                ) for s in data]
            except Exception:
                subjects=[]

def saveExams():
    data=[]
    for e in exams:
        data.append({
            'class_id':e.class_id,
            'subject_id':e.subject_id,
            'marks':e.marks,
            'exam_date':e.exam_date,
            'max_marks':e.max_marks,
            'exam_name':e.exam_name
        })
    with open(EXAMS_FILE,'w') as f:
        json.dump(data,f,indent=4)

def loadExams():
    global exams
    if os.path.exists(EXAMS_FILE):
        with open(EXAMS_FILE,'r') as f:
            try:
                data=json.load(f)
                exams=[Exam(
                    e['class_id'],
                    e['subject_id'],
                    e['marks'],
                    e['exam_date'],
                    e['max_marks'],
                    e['exam_name']
                ) for e in data]
            except Exception:
                exams=[]

loadStudents()
loadTeachers()
loadClassrooms()
loadSubjects()
loadExams()