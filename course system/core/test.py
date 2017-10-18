#_*_coding:utf-8*_
#Author:Fiona

import os,sys,json
sys.path.append("..")
from bin import course

db_DIR = course.BASE_DIR  + r"\db"
db_admin = db_DIR + r"\admin"
username = input("用户名：").strip()
admin_file = "%s\%s.json"%(db_admin,username)
print(admin_file)
print(os.path.isfile(admin_file))
if os.path.isfile(admin_file):
    with open(admin_file,'r') as f:
        admin_data = json.load(f)
    print(admin_data)
