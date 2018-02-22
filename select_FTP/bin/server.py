#_*_coding:utf-8*_
#Author:Fiona

import  os,sys
BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR) #添加环境变量
from core.server_main import server_ftp
if __name__ == '__main__':
    myserver = server_ftp()
    myserver.start()