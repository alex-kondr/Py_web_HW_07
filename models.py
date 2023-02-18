from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Date


Base = declarative_base()


class Group(Base):
    
    __tablename__ = "Groups"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    students = relationship("Student", cascade="all, delete", backref="Group")
    
    
class Student(Base):
    
    __tablename__ = "Students"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    grades = relationship("Grade", cascade="all, delete", backref="student")
    group_id = Column(Integer, ForeignKey(Group.id, ondelete="CASCADE"))
    
    
class Teacher(Base):
    
    __tablename__ = "Teachers"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    subjects = relationship("Subject", cascade="all, delete", backref="teacher")

    
class Subject(Base):
    
    __tablename__ = "Subjects"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    grades = relationship("Grade", cascade="all, delete", backref="subject")
    teacher_id = Column(Integer, ForeignKey(Teacher.id, ondelete="CASCADE"))


class Grade(Base):
    
    __tablename__ = "Grades"
    
    id = Column(Integer, primary_key=True)
    rating = Column(Integer, nullable=False)
    date = Column(Date, default=datetime.now().date)
    student_id = Column(Integer, ForeignKey(Student.id, ondelete="CASCADE"))
    subject_id = Column(Integer, ForeignKey(Subject.id, ondelete="CASCADE"))
    