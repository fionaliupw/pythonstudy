#_*_coding:utf-8*_
#Author:Fiona
import  os,sys
BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR) #添加环境变量
from core.client_main import client_ftp
if __name__ == '__main__':
    myclient = client_ftp()
    myclient.start()