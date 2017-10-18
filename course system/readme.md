﻿# readme

标签（空格分隔）： 未分类

---

## 程序实现以下需求：
选课系统：
角色:学校、学员、课程、讲师
要求:
1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 课程包含，周期，价格，通过学校创建课程 
4. 通过学校创建班级， 班级关联课程、讲师
5. 创建学员时，选择学校，关联班级
5. 创建讲师角色时要关联学校， 
6. 提供两个角色接口
6.1 学员视图， 可以注册， 交学费， 选择班级，
6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩 
6.3 管理视图，创建讲师， 创建班级，创建课程
7. 上面的操作产生的数据都通过pickle序列化保存到文件里

## 程序结构图
├── course system #主目录
    ├── __init__.py
    ├── bin                 #course system执行文件目录
    │   ├── __init__.py
    │   ├── course.py       #course system 执行程序
    ├── core                #主要程序逻辑
    │   ├── __init__.py
    │   ├── main.py         #主要程序交互
    │   ├── uid.py          #生成uid信息
    ├── db                  #用户数据存储的目录
        ├── __init__.py
        └── admin    #保存管理员信息
        └── classes  #保存班级信息
        └── school   #保存学校信息
        └── course   #保存课程信息
        └── student  #保存学员信息
        └── teacher  #保存讲师信息
        └── class_grade   #保存讲师创建的学生成绩
        └── class_record  #保存讲师创建的学生上课记录