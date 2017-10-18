#_*_coding:utf-8*_
#Author:Fiona

import os,sys
import pickle
import json
sys.path.append("..")

from bin import course
from core import uid

#db文件路径
db_DIR = course.BASE_DIR  + r"\db"
db_admin = db_DIR + r"\admin"
db_school = db_DIR + r"\school"
db_course = db_DIR + r"\course"
db_student = db_DIR + r"\student"
db_teacher = db_DIR + r"\teacher"
db_classes = db_DIR + r"\classes"
db_class_grade = db_DIR + r"\class_grade"
db_class_record = db_DIR + r"\class_record"

#文件的读写操作类
class baseclass(object):
    def __init__(self):
        pass
    def save(self,type,dict):
        filename = uid.create_md()
        dict['uid'] = filename
        filepath = "%s\%s"%(db_DIR,type)
        save_file = "%s\%s"%(filepath,filename)
        if os.path.isdir(filepath):
            with open(save_file,"wb") as f:
                f.write(pickle.dumps(dict))         #pickle.dumps将数据通过特殊方式转换为只有python可以识别的字符串
                if True:
                    print("--------",type,"创建成功","--------")
                    for key in dict:
                        print(key,":\t",dict[key])
    def seek_list(self,type,list):
        filename = uid.create_md()
        filepath = "%s\%s"%(db_DIR,type)
        seek_file = "%s\%s"%(filepath,filename)
        if os.path.isdir(filepath):
            with open(seek_file,"wb") as f:
                f.write(pickle.dumps(list))
                if True:
                    print("--------",type,"创建成功","--------")
                    for i in list:
                        for key in i:
                            print(key,i[key])
                        print("\n")
        return True
    def open(self,type):
        all_data = []
        db_path = "%s\%s" %(db_DIR,type)
        for i in os.listdir(db_path):
            if os.path.isfile(os.path.join(db_path,type)):
                db_file = os.path.join(db_path,type)
                with open(db_file,"rb") as f:
                    filedict = pickle.load(f)
                    all_data.append(filedict)
        return all_data
#管理员类
class Admin(baseclass):
    def __init__(self):
        baseclass.__init__(self)
    def create_school(self):
        school_dict = {}
        school_name = input("学校名称：")
        school_addr = input("学校地址：")
        s1 = School(school_name,school_addr)
        school_dict["学校名称"] = s1.school_name
        school_dict["学校地址"] = s1.school_addr
        baseclass.save(self,"school",school_dict)
    def create_teacher(self):
        teacher_dict = {}
        teacher_name = input("讲师姓名：")
        teacher_salary = input("讲师薪资：")
        teacher_school = input("所属学校：")
        t1 = Teacher(teacher_name,teacher_salary,teacher_school)
        teacher_dict["讲师姓名"] = t1.teacher_name
        teacher_dict["讲师薪资"] = t1.teacher_salary
        teacher_dict["所属学校"] = t1.teacher_school
        print(teacher_dict)
        baseclass.save(self,"teacher",teacher_dict)
    def create_student(self):
        student_dict = {}
        student_name = input("学员姓名：")
        student_sex = input("学员性别：")
        student_school = input("所属学校：")
        student_classes = input("所属班级：")
        stu1  = Student(student_name,student_sex,student_school,student_classes)
        student_dict["学员姓名"] = stu1.student_name
        student_dict["学员性别"] = stu1.student_sex
        student_dict["所属学校"] = stu1.student_school
        student_dict["所属班级"] = stu1.student_classes
        baseclass.save(self,"student",student_dict)
    def create_course(self):
        course_dict = {}
        course_name = input("课程名：")
        course_period = input("课程周期：")
        course_price = input("课程价格：")
        c1 = Course(course_name,course_period,course_price)
        course_dict["课程名"] = c1.course_name
        course_dict["课程周期"] = c1.course_period
        course_dict["课程价格"] = c1.course_price
        baseclass.save(self,"course",course_dict)
    def create_classes(self):
        classes_dict = {}
        classes_name = input("班级名：")
        classes_teacher = input("班级讲师：")
        classes_course = input("班级课程：")
        cl1 = Classes(classes_name,classes_teacher,classes_course)
        classes_dict["班级名"] = cl1.classes_name
        classes_dict["班级讲师"] = cl1.classes_teacher
        classes_dict["班级课程"] = cl1.classes_course
        baseclass.save(self,"classes",classes_dict)
#学校类
class School(baseclass):
    def __init__(self,school_name,school_addr):
        baseclass.__init__(self)
        self.school_name = school_name
        self.school_addr = school_addr
#讲师类
class Teacher(baseclass):
    def __init__(self,teacher_name,teacher_salary,teacher_school):
        baseclass.__init__(self)
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.teacher_school = teacher_school
    def create_class_record(self):
        class_record = []
        school_dict = {
            '1':"北京老男孩",
            '2':"上海老男孩"
        }
        for key in school_dict:
            print(school_dict[key])
        student_school = input("选择学校：")
        student_classes = input("选择班级：")
        student_times = input("课程次数：")
        student_list = baseclass.open(self,"student")
        for i in student_list:
            if i["学校"] == student_school and i["班级"] == student_classes:
                student_name = i["姓名"]
                student_status = input("%s 上课情况：" % student_name)
                i["上课情况"] = student_status
                i["课程次数"] = student_times
                class_record.append(i)
        baseclass.seek_list(self,"class_record",class_record)
    def create_class_grade(self):
        class_grade = []
        student_school = input("选择学校：")
        student_classes = input("选择班级：")
        student_times = input("课程次数：")
        student_list = baseclass.open(self,"student")
        for i in student_list:
            if i["学校"] == student_school and i["班级"] == student_classes:
                student_name = i["姓名"]
                student_grade = input("%s 成绩：" % student_name)
                i["成绩"] = student_grade
                i["课程次数"] = student_times
                class_grade.append(i)
        baseclass.seek_list(self,"class_grade",class_grade)
    def teacher_view_grade(self):
        grade_list = []
        student_school = input("选择学校：")
        student_classes = input("选择班级：")
        student_times = input("课程次数：")
        class_grade_list = baseclass.open(self,"class_grade")
        for i in class_grade_list:
            for j in i:
                if j["学校"] == student_school and j["班级"] == student_classes and j["课程次数"] == student_times:
                    grade_list.append(j)
        for i in grade_list:
            for key in i:
                print(key,i[key])
            print("\n")
    def teacher_view_record(self):
        record_list = []
        student_school = input("选择学校：")
        student_classes = input("选择班级：")
        student_times = input("课程次数：")
        class_record_list = baseclass.open(self,"class_record")
        for i in class_record_list:
            for j in i:
                if j["学校"] == student_school and j["班级"] == student_classes and j["课程次数"] == student_times:
                    record_list.append(j)
        for i in record_list:
            for key in i:
                print(key,i[key])
            print("\n")
#课程类
class Course(baseclass):
    def __init__(self,course_name,course_period,course_price):
        baseclass.__init__(self)
        self.course_name = course_name
        self.course_period = course_period
        self.course_price = course_price

#学员类
class Student(baseclass):
    def __init__(self,student_name,student_sex,student_school,student_classes):
        baseclass.__init__(self)
        self.student_name = student_name
        self.student_sex = student_sex
        self.student_school = student_school
        self.student_classes =student_classes
    def stu_register(self):
        student_dict = {}
        print("欢迎进入学员注册系统".center(80,"-"))
        student_name = input("学员注册姓名：")
        student_sex = input("学员性别：")
        student_school = input("注册学校：")
        student_classes = input("注册班级：")
        stu1 = Student(student_name,student_sex,student_school,student_classes)
        student_dict["学员姓名"] = stu1.student_name
        student_dict["学员性别"] = stu1.student_sex
        student_dict["所属学校"] = stu1.student_school
        student_dict["所属班级"] = stu1.student_classes
        baseclass.save(self,"student",student_dict)
    def student_view_grade(self):
        student_school = input("学校名称：")
        student_classes = input("班级：")
        student_times = input("课程次数：")
        student_name = input("学员姓名：")
        class_grade_list = baseclass.open(self,"class_grade")
        for i in class_grade_list:
            for j in i:
                if j["学校"] == student_school and j["班级"] == student_classes and j["课程次数"] == student_times and j["学员姓名"] == student_name:
                    for key in j:
                        print(key,j[key])
                    print("\n")
    def student_view_record(self):
        student_school = input("学校名称：")
        student_classes = input("班级：")
        student_times = input("课程次数：")
        student_name = input("学员姓名：")
        class_record_list = baseclass.open(self,"class_record")
        for i in class_record_list:
            for j in i:
                if j["学校"] == student_school and j["班级"] == student_classes and j["课程次数"] == student_times and j["学员姓名"] == student_name:
                    for key in j:
                        print(key,j[key])
                    print("\n")
#班级类
class Classes(baseclass):
    def __init__(self,classes_name,classes_teacher,classes_course):
        baseclass.__init__(self)
        self.classes_name = classes_name
        self.classes_teacher = classes_teacher
        self.classes_course = classes_course

#管理视图,继承Admin类
class Adminview(Admin):
    def __init__(self):
        Admin.__init__(self)
    def auth(self,username,password):
        admin_file = "%s\%s.json"%(db_admin,username)
        if os.path.isfile(admin_file):
            with open(admin_file,'r') as f:
                admin_data = json.load(f)
            if admin_data['username'] == username and admin_data['password'] == password:
                return True
            else:
                print("用户名或密码错误！")
    def login(self):
        menu = u'''
       ------- 欢迎进入管理视图 ---------
            \033[32;1m 1.  校区管理
            2.  讲师管理
            3.  学员管理
            4.  课程管理
            5.  返回
            \033[0m'''
        menu_dict = {
            '1':Adminview.school_manager,
            '2':Adminview.teacher_manager,
            '3':Adminview.student_manager,
            '4':Adminview.course_manager,
            '5':"back"
        }
        username = input("输入用户名:").strip()
        password = input("输入密码：").strip()
        auth = Adminview.auth(self,username,password)
        if auth:
            exit_flag = False
            while not exit_flag:
                print(menu)
                option_number = input("请输入菜单编号：").strip()
                if option_number in menu_dict:
                    if int(option_number) == 5:
                        exit_flag = True
                    else:
                        print(menu_dict[option_number])
                        menu_dict[option_number](self)
                else:
                    print("\033[31;1m输入编号不存在，请重新输入\033[0m")
    def school_manager(self):
        exit_flag = False
        menu = u'''
        ------- 欢迎进入校区管理 ---------\033[32;1m
                1.  创建校区
                2.  创建班级
                3.  返回\033[0m
        '''
        while not exit_flag:
            print(menu)
            option_number = input("请输入菜单编号：").strip()
            if int(option_number) == 1:
                Admin.create_school(self)
            elif int(option_number) == 2:
                Admin.create_classes(self)
            else:
                exit_flag = True
    def teacher_manager(self):
        exit_flag = False
        while not exit_flag:
            print("""
                ------- 欢迎进入讲师管理 ---------
                \033[32;1m 1.  创建讲师
                2.  返回
                \033[0m
             """)
            option_number = input("请输入菜单编号：").strip()
            if int(option_number) == 1:
                Admin.create_teacher(self)
            else:
                exit_flag = True
    def student_manager(self):
        exit_flag = False
        while not exit_flag:
            print("""
                ------- 欢迎进入学员管理 ---------
                \033[32;1m 1.  创建学员
                2.  返回
                \033[0m
             """)
            option_number = input("请输入菜单编号：").strip()
            if int(option_number) == 1:
                Admin.create_student(self)
            else:
                exit_flag = True
    def course_manager(self):
        exit_flag = False
        while not exit_flag:
            print("""
                ------- 欢迎进入课程管理 ---------\033[32;1m
                1.  创建课程
                2.  返回
                \033[0m
             """)
            option_number = input("请输入菜单编号：").strip()
            if int(option_number) == 1:
                Admin.create_course(self)
            else:
                exit_flag = True
#讲师视图，继承Teacher类
class Teacherview(Teacher):
    def __init__(self,teacher_name,teacher_salary,teacher_school):
        Teacher.__init__(self,teacher_name,teacher_salary,teacher_school)
    def login(self):
        menu = u'''
       ------- 欢迎进入讲师视图 ---------
        \033[32;1m 1.  创建上课记录
        2.  创建学员成绩
        3.  查看学员上课记录
        4.  查看学员成绩
        5.  返回
        \033[0m'''
        menu_dict = {
            '1': Teacher.create_class_record,
            '2': Teacher.create_class_grade,
            '3': Teacher.teacher_view_record,
            '4': Teacher.teacher_view_grade,
            '5': "back"
        }
        if True:
            exit_flag = False
            while not exit_flag:
                print(menu)
                option_number = input("请输入菜单编号：").strip()
                if option_number in menu_dict:
                    if int(option_number) == 5:
                        exit_flag = True
                    else:
                        print(menu_dict[option_number])
                        menu_dict[option_number](self)
                else:
                    print("\033[31;1m输入编号不存在，请重新输入\033[0m")
#学员视图，继承Student类
class Studentview(Student):
    def __init__(self,student_name,student_sex,student_school,student_classes):
        Student.__init__(self,student_name,student_sex,student_school,student_classes)
    def login(self):
        menu = u'''
        ------- 欢迎进入学生管理视图 ---------
         \033[32;1m 1.  注册
         2.  查看上课记录
         3.  查看作业成绩
         4.  返回
         \033[0m'''
        menu_dict = {
            '1': Student.stu_register,
            '2': Student.student_view_record,
            '3': Student.student_view_grade,
            '4': "back"
        }
        if True:
            exit_flag = False
            while not exit_flag:
                print(menu)
                option_number = input("请输入菜单编号：").strip()
                if option_number in menu_dict:
                    if int(option_number) == 4:
                        exit_flag = True
                    else:
                        menu_dict[option_number](self)
                else:
                    print("\033[31;1m输入编号不存在，请重新输入\033[0m")

class CourseSystem(object):
    def __init__(self):
        pass
    def interactive(self):
        menu = u'''
         ------- 欢迎进入选课系统 ---------
         \033[32;1m 1.  学生视图
         2.  讲师视图
         3.  学校管理视图
         4.  退出
         \033[0m'''
        menu_dict = {
            '1':Studentview,
            '2':Teacherview,
            '3':Adminview,
            '4':"logout"
        }
        exit_flag = False
        while not exit_flag:
            print(menu)
            option_number = input("请选择菜单编号：").strip()
            if option_number in menu_dict:
                if int(option_number) == 4:
                    exit_flag = True
                else:
#                    print(menu_dict[option_number])
                    menu_dict[option_number].login(self)
            else:
                print("\033[31;1m输入编号不存在，请重新输入\033[0m")