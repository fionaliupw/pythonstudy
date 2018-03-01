#_*_coding:utf-8*_
#Author:Fiona

from .models import Teacher,Student,Class,Course,Class_Course,Study_Record
import random

class Student_center(object):
    '''学生视图'''
    def __init__(self,session):
        self.session = session
        self.authentication()
        self.handler()

    def handler(self):
        while True:
            print("\033[36;1m欢迎【%s】进入学员管理系统\n"
                  "upload_homework 上传作业\n"
                  "check homework 查看作业(功能待完善)\n"
                  "check rank 查看班级排名(功能待完善)\n"
                  "exit 退出系统\n\033[0m" % self.student_obj.stu_name)
            user_func = input("\033[34;0m请输入进行操作的命令：\033[0m")
            if hasattr(self,user_func):
                getattr(self,user_func)()

    def upload_homework(self):
        '''上传作业'''
        class_name = input("\033[34;0m请输入班级名：\033[0m")
        for class_obj in self.student_obj.classes:
            print(class_obj.class_name)
            if class_name == class_obj.class_name:
                course_name = input("\033[34;0m请输入的课节名（lesson）:\033[0m")
                course_obj = self.session.query(Course).filter_by(course_name=course_name).first()
                if course_obj:  # 输入的course名字存在
                    class_course_obj = self.session.query(Class_Course).filter(
                        Class_Course.class_id == class_obj.class_id). \
                        filter(Class_Course.course_id == course_obj.course_id).first()
                    if class_course_obj:  # 班级对应的课course表数据存在
                        study_record_obj = self.session.query(Study_Record).filter(
                            Study_Record.class_course_id == class_course_obj.id).filter(
                            Study_Record.stu_id == self.student_obj.stu_id).first()
                        if study_record_obj:  # 上课记录存在
                            score = random.randint(10,100)
                            study_record_obj.score = score
                            self.session.commit()
                            print("上传成功")
                        else:
                            print("\33[31;1m系统错误：当前上课记录已经创建\33[0m")
                else:
                    print("\33[31;1m系统错误：course未创建\33[0m")

    def authentication(self):
        '''认证'''
        while True:
            student_name = input("\033[34;0m请输入学生名：\033[0m").strip()
            self.student_obj = self.session.query(Student).filter_by(student_name=student_name).first()
            if not self.student_obj:
                print("\33[31;1m输入错误：请输入有效的学生名\33[0m")
                continue
            else:
                break