from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    students = relationship("Student", backref="group")
    
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(100), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id", ondelete="CASCADE"))
    grades = relationship("Grade", backref="student")

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(100), nullable=False)
    subjects = relationship("Subject", backref="teacher")
    
class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="CASCADE"))
    grades = relationship("Grade", backref="subject")
    
class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"))
    grade = Column(Integer, nullable=False)
    grade_date = Column(DateTime, default=datetime.now())