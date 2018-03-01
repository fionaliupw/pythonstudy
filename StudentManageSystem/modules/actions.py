#_*_coding:utf-8*_
#Author:Fiona
from sqlalchemy.orm import sessionmaker
from conf.settings import engine
from .models import Teacher,Class
from .teacher_center import Teacher_center
from .student_center import Student_center
class Action(object):
    '''管理视图'''
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.initialize_database()

    def func(self):
        while True:
            print("\033[36;1m欢迎进入CLASS_SYSTEM系统\n"
                  "1 讲师视图\n"
                  "2 学生视图\n"
                  "q 退出系统\n\033[0m")
            user_choice = input("\033[34;0m请输入你进入的视图：\033[0m")
            if user_choice == '1':
                Teacher_center(self.session)
            elif user_choice == '2':
                Student_center(self.session)
            elif user_choice == 'q':
                print("\033[34;1m感谢使用管理系统,退出\033[0m")
                break
            else:
                print("\033[31;1m请输入正确的选项\033[0m")

    def initialize_database(self):
        '''初始化数据库'''
        rest = self.session.query(Teacher).filter(Teacher.teacher_id>0).all()
        if not rest:
            class1 = Class(class_name = "S14",course="python")
            teacher1 = Teacher(teacher_name="Fiona")
            teacher1.classes = [class1]

            self.session.add_all([class1,teacher1])
            self.session.commit()
