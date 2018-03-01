#_*_coding:utf-8*_
#Author:Fiona

from sqlalchemy import Column,String,Integer,ForeignKey,DATE,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from conf.settings import engine

Base = declarative_base()   # 生成orm基类

# teacher_class对应关系表
teacher_class = Table("teacher_class",Base.metadata,
                      Column("teacher_id",Integer,ForeignKey("teacher.teacher_id")),
                      Column("class_id",Integer,ForeignKey("class.class_id")),
                      )

# class_student对应关系表
class_student = Table("class_student",Base.metadata,
                      Column("class_id",Integer,ForeignKey("class.class_id")),
                      Column("stu_id",Integer,ForeignKey("student.stu_id")),
                      )

class Class_Course(Base):
    '''班级 课程对应关系表'''
    __tablename__ = "class_course"
    id = Column(Integer,primary_key=True)
    class_id = Column(Integer,ForeignKey("class.class_id"))
    course_id = Column(Integer,ForeignKey("course.course_id"))

    classes = relationship("Class",backref="class_courses")
    courses = relationship("Course",backref="class_courses")

    def __repr__(self):
        return "%s %s" % (self.classes,self.courses)

class Study_Record(Base):
    '''上课记录表'''
    __tablename__ = "study_record"
    id = Column(Integer,primary_key=True)
    class_course_id = Column(Integer,ForeignKey("class_course.id"))
    stu_id = Column(Integer,ForeignKey("student.stu_id"))
    status = Column(String(32),nullable=False)  # nullable指not null
    score = Column(Integer,nullable=True)

    class_courses = relationship("Class_Course",backref="my_study_record")
    students = relationship("Student",backref="my_study_record")

    def __repr__(self):
        return "\033[35;0m%s,%s,状态：【%s】,成绩：【%s】\33[0m" % (self.class_courses,self.students,self.status,self.score)

class Teacher(Base):
    '''讲师'''
    __tablename__ = "teacher"
    teacher_id = Column(Integer,primary_key=True)
    teacher_name = Column(String(32),nullable=False,unique=True)

    classes = relationship("Class",secondary=teacher_class,backref="teachers")

    def __repr__(self):
        return "讲师：【%s】" % self.teacher_name

class Class(Base):
    '''班级'''
    __tablename__ = "class"
    class_id = Column(Integer,primary_key=True)
    class_name = Column(String(32),nullable=False,unique=True)
    course = Column(String(32),nullable=False)

    students = relationship("Student",secondary=class_student,backref="classes")

    def __repr__(self):
        return "班级名：【%s】" % self.class_name

class Student(Base):
    '''学生'''
    __tablename__ = "student"
    stu_id = Column(Integer,primary_key=True)
    stu_name = Column(String(32),nullable=False,unique=True)
    QQ_id = Column(Integer,nullable=False)

    def __repr__(self):
        return "学生名：【%s】" % self.stu_name

class Course(Base):
    '''课程'''
    __tablename__ = "course"
    course_id = Column(Integer,primary_key=True)
    course_name = Column(String(32),nullable=False,unique=True)

    def __repr__(self):
        return "课程名：【%s】" % self.course_name

Base.metadata.create_all(engine)