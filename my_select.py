from datetime import datetime
from pprint import pprint
from sqlalchemy import func, desc, distinct

from connect_db import session
from models import Grade, Student, Subject, Teacher, Group


def select1():
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
    .join(Grade, Student.id == Grade.student_id)\
    .group_by(Student.id)\
    .order_by(desc('avg_grade'))\
    .limit(5)\
    .all()
     
     
def select2(sub_id):
    return session.query(Student.fullname,func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
    .join(Student, Grade.student_id == Student.id)\
    .filter(Grade.subject_id == sub_id)\
    .group_by(Student.id)\
    .order_by(desc('avg_grade'))\
    .limit(1)\
    .all()
     
def select3(sub_id):
    return session.query(Group.name.label('group_name'), func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
    .join(Student, Group.id == Student.group_id)\
    .join(Grade, Student.id == Grade.student_id)\
    .join(Subject, Grade.subject_id == Subject.id)\
    .filter(Subject.id == sub_id)\
    .group_by(Group.name)\
    .order_by(desc('avg_grade'))\
    .all()
     
def select4():
    return session.query(func.round(func.avg(Grade.grade), 2)).one()
    
def select5(teach_id):
    return session.query(Teacher.fullname, Subject.id)\
    .select_from(Teacher)\
    .join(Subject, Teacher.id == Subject.id)\
    .filter(Teacher.id == teach_id)\
    .one()
    
def select6(gr_id):
    return session.query(Student.fullname, Group.name)\
    .select_from(Student)\
    .join(Group, Student.group_id == Group.id)\
    .filter(Group.id == gr_id)\
    .all()

def select7(gr_id, sub_id):
    return session.query(Grade.grade, Student.fullname, Group.name, Subject.id)\
    .select_from(Student)\
    .join(Group, Student.group_id == Group.id)\
    .join(Grade, Student.id == Grade.student_id)\
    .join(Subject, Grade.subject_id == Subject.id)\
    .filter(Group.id == gr_id, Subject.id == sub_id)\
    .all()    

def select8(teach_id):
    return session.query(Teacher.fullname.label("Teacher"), func.round(func.avg(Grade.grade), 2).label('avg_grade'), Subject.id.label("Subject"))\
    .select_from(Teacher)\
    .join(Subject, Teacher.id == Subject.teacher_id)\
    .join(Grade, Subject.id == Grade.subject_id)\
    .filter(Teacher.id == teach_id)\
    .group_by(Teacher.fullname, Subject.id)\
    .all()

def select9(stud_id):
    return session.query(distinct(Student.fullname), Subject.id)\
    .select_from(Subject)\
    .join(Grade, Subject.id == Grade.subject_id)\
    .join(Student, Student.id == Grade.student_id)\
    .filter(Student.id == stud_id)\
    .all()
    
def select10(stud_id, teach_id):
    return session.query(distinct(Subject.id), Student.fullname, Teacher.fullname)\
    .select_from(Subject)\
    .join(Teacher, Teacher.id == Subject.teacher_id)\
    .join(Grade, Subject.id == Grade.subject_id)\
    .join(Student, Grade.student_id == Student.id)\
    .filter(Student.id == stud_id, Teacher.id == teach_id)\
    .all()
    
def select11(teach_id, stud_id):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'), Teacher.fullname, Student.fullname)\
    .select_from(Grade)\
    .join(Subject, Grade.subject_id == Subject.id)\
    .join(Teacher, Subject.teacher_id == Teacher.id)\
    .join(Student, Grade.student_id == Student.id)\
    .filter(Teacher.id == teach_id, Student.id == stud_id)\
    .group_by(Teacher.fullname, Student.fullname)\
    .all()  

if __name__ == '__main__':
    # pprint(select1())
    # print("+++")
    # pprint(select2(1))
    # print("+++")
    # pprint(select3(1))
    # print("+++")
    # pprint(select4())
    # print("+++")
    # pprint(select5(1))
    # print("+++")
    # pprint(select6(1))
    # print("+++")
    # pprint(select7(1, 1))
    # print("+++")
    # pprint(select8(1))
    # print("+++")
    # pprint(select9(1))
    # print("+++")
    # pprint(select10(1, 1))
    # print("+++")
    # pprint(select11(1,1))
