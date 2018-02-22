#_*_coding:utf-8*_
#Author:Fiona
import os
import sys
import time

BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from . import select_server

class server_ftp(object):
    '''ftp_server交互程序'''
    def start(self):
        '''
        启动函数
        :return:
        '''
        print('欢迎进入Select Ftp')
        msg = '''
        1.select     客户端
        2.exit       退  出
        '''
        while True:
            print(msg)
            user_choice = input('请选择操作>>>:')
            if user_choice == '1':
                server = select_server.select_ftp("localhost",10000)
                print(time.strftime("%Y-%m-%d %X", time.localtime()), '[+]select server ftp already work ')
                server.start()
            elif user_choice == '2' or user_choice== 'q'or user_choice == 'exit':
                sys.exit('程序退出')
            else:
                print('非法的操作,请重新输入')