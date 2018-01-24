#_*_coding:utf-8*_
#Author:Fiona
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core.main import Manage
from core.main import My_command
from core.main import My_Thread


if __name__ == "__main__":
    MyManage = Manage()
    MyDict = MyManage.host_dict
for ip in MyDict:
    port = MyDict[ip][1]
    username = MyDict[ip][2]
    passwd = MyDict[ip][3]
    t = My_Thread(ip,port,username,passwd)
    t.start()
tt = My_command()
tt.start()