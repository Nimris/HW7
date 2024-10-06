from random import choice
from connect_db import session
from models import Group, Student, Teacher, Subject, Grade
from faker import Faker


fake = Faker('uk-UA')

if __name__ == "__main__":
    groups = [
        Group(name="Group1"),
        Group(name="Group2"),
        Group(name="Group3")
    ]
    session.add_all(groups)
    
    for i in range(30):
        student = Student(fullname=fake.name(), group_id = choice([1,2,3]))
        session.add(student)
    
    for i in range(5):
        teacher = Teacher(fullname=fake.name())
        session.add(teacher)
    
    for i in range(8):
        subject = Subject(name=fake.word(), teacher_id=choice([1,2,3,4,5]))
        session.add(subject)
        
    for i in range(160):
        grade = Grade(student_id=choice(range(1,31)), subject_id=choice(range(1,9)), grade=choice(range(0,101)))
        session.add(grade)
        
    session.commit()
    
    
    
    
    