#_*_coding:utf-8*_
#Author:Fiona

import os,sys

#程序主目录

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#添加环境变量
sys.path.append(BASE_DIR)
sys.path.append("..")
#print(BASE_DIR)

from core import main

if __name__ == '__main__':
    s = main.CourseSystem()
    s.interactive()