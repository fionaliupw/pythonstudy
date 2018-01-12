#_*_coding:utf-8*_
#Author:Fiona

import os,hashlib
import json
import sys
sys.path.append("..")
from conf import settings
from modules import auth_user
from modules import socket_server
class MyServer():
    #创建用户数据库文件
    def create_db(self):
        user_database={}
        encryption = auth_user.User_operation()
        limitsize = settings.LIMIT_SIZE
        for k,v in settings.USERS_DICT.items():
            username = k
            password = encryption.hash(v)
            #user_db_path  = settings.DATABASE + r"\%s.db"%username
            #user_home_path = settings.HOME_PATH + r"\%s"%username
            user_db_path = os.path.join(os.path.sep,settings.DATABASE,"%s.db"%username)
            user_home_path = os.path.join(os.path.sep,settings.HOME_PATH,"%s"%username)
            user_database["username"] = username
            user_database["password"] = password
            user_database["limitsize"] = limitsize
            user_database["homepath"] = user_home_path
            if not os.path.isfile(user_db_path):
                with open(user_db_path,"w") as file:
                    file.write(json.dumps(user_database))
    #创建用户属主目录
    def create_dir(self):
        for username in settings.USERS_DICT:
            #user_home_path = settings.HOME_PATH + r"\%s" %username
            user_home_path = os.path.join(os.path.sep,settings.HOME_PATH,"%s" %username)
            if not os.path.isdir(user_home_path):
                os.popen("mkdir %s" %user_home_path)
#初始化系统数据并启动程序
if __name__ == "__main__":
    #create_db()         #创建数据库
    #create_dir()        #创建属主目录
                        #启动ftp服务
    ftpserver = MyServer()
    ftpserver.create_db()
    ftpserver.create_dir()
    server = socket_server.socketserver.ThreadingTCPServer(settings.IP_PORT, socket_server.Myserver)
    server.serve_forever()
