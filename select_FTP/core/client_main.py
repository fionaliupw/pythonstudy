#_*_coding:utf-8*_
#Author:Fiona
import os
import sys

BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from . import select_client

class client_ftp(object):
    '''client_ftp交互类'''
    def start(self):
        '''
        启动函数
        :return:
        '''
        print('欢迎进入Select Ftp')
        msg = '''
        1.select模块客户端上传下载测试
        2.exit
        '''
        while True:
            print(msg)
            user_choice = input('请选择操作>>>:')
            if user_choice == '1':
                client = select_client.select_client()
                client.connect("localhost", 10000)
                client.start()
            elif user_choice == '2' or user_choice == 'q' or user_choice == 'exit':
                sys.exit('程序退出')
            else:
                print('非法操作,请重新输入')