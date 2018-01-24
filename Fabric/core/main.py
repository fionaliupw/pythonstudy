#_*_coding:utf-8*_
#Author:Fiona
import os,sys
import json
import threading,paramiko
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
host_file = os.path.join(os.path.sep,BASE_DIR,"database","host_info.json")

# host_dict = {}
# with open(host_file,"r",encoding="UTF-8") as f:
#     host_data = json.load(f)
# print(host_data)
# for i in host_data:
#
#     print("%s %s"%(i,host_data[i]))

class Manage(object):
    def __init__(self):
        self.host_dict = {}         # 存放选定查看的IP主机信息
        with open(host_file,"r",encoding="UTF-8") as f:
            self.host_data = json.load(f)

        self.show()

        while True:
            manage_input = input("添加主机，删除主机，查询主机，命令操作(Add/Delete/Select/Next/exit)>>>>>>").strip()
            if manage_input == "Add":
                self.Add()
                # print("最新主机信息".center(40,"="))
                self.show()
            elif manage_input == "Delete":
                self.Delete()
                # print("最新主机信息".center(40,"="))
                self.show()
            elif manage_input == "Select":
                # print("最新主机信息".center(40,"="))
                self.show()
            elif manage_input == "Next":
                break
            elif manage_input == "exit":
                sys.exit("程序退出")
            else:
                print("输入不合法。")
                continue
        while True:
            # self.show()
            choose_1 = input("输入Next，程序进行下一步执行；输入选定的ip，查询该主机信息>>>>>>").strip()
            if choose_1 == "Next":
                print(self.host_dict)
                break
            elif choose_1 in self.host_data:
                self.host_dict[choose_1] = self.host_data[choose_1]
            else:
                print("不存在该ip!!!")

    def show(self):
        for i in self.host_data:
            print("%s %s"%(i,self.host_data[i]))
    def Add(self):
        ip_addr,group,port,username,passwd = input("请输入新增主机信息，必须使用逗号分隔（如ip_addr,group,port,username,passwd）>>>>>>").strip().split(",")
        self.host_data[ip_addr] = [group,port,username,passwd]
        with open(host_file,"w",encoding="UTF-8") as f1:
            json.dump(self.host_data,f1)
    def Delete(self):
        delete_ip = input("请输入需要删除的主机ip>>>>>>").strip()
        if delete_ip in self.host_data:
            del self.host_data[delete_ip]
            with open(host_file,"w",encoding="UTF-8") as f2:
                json.dump(self.host_data,f2)
            if delete_ip in self.host_data:
                print("删除失败！！！")
            else:
                print("%s删除成功！！！"%delete_ip)
        else:
            print("不存在该ip!!!")

class My_Thread(threading.Thread):
    def __init__(self,ip_addr,port,username,passwd):
        threading.Thread.__init__(self)
        self.ip_addr = ip_addr
        self.port = port
        self.username = username
        self.passwd = passwd
        print(self.ip_addr,self.port,self.username,self.passwd)

    def run(self):
        if self.ssh_connect() == False:
            # print(self)
            del self
            exit()
        while True:
            cmd_event.wait()        # 等待事件
            self.cmd_input = My_command.command_info
            self.cmd_list = self.cmd_input.split()
            if hasattr(self,self.cmd_list[0]):
                send_cmd = getattr(self,self.cmd_list[0])
                send_cmd()
            else:
                self.other_cmd()
            cmd_event.clear()
    def other_cmd(self):
        stdin,stdout,stderr =  self.ssh.exec_command(self.cmd_input)
        res,err = stdout.read(),stderr.read()
        if res:
            print("command result:\n%s"%res.decode())
        elif err:
            print("command error:\n%s"%err.decode())
    def get(self):
        try:
            file_count = len(self.cmd_list[1:])
            if file_count == 1:
                # self.sftp.get(self.cmd_list[1])
                print("文件下载需要本地文件和远程文件,如sftp.get(local_file,remote_file)")
            elif file_count == 2:
                self.sftp.get(self.cmd_list[1],self.cmd_list[2])
        except FileNotFoundError as e:
            print("get command不合法!!!")

    def put(self):
        try:
            file_count = len(self.cmd_list[1:])
            if file_count == 1:
                # self.sftp.put(self.cmd_list[1])
                print("文件上传需要本地文件和远程文件,如sftp.put(local_file,remote_file)")
            elif file_count == 2:
                self.sftp.put(self.cmd_list[1],self.cmd_list[2])
        except FileNotFoundError as e:
            print("put command不合法!!!")
    def ssh_connect(self):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # print(self.ip_addr,self.port,self.username,self.passwd)
            self.ssh.connect(hostname=self.ip_addr,port=int(self.port),username=self.username,password=self.passwd)
            self.sftp = paramiko.SFTPClient.from_transport(self.ssh.get_transport())
        except:
            print("SSH连接失败")
            return False

class My_command(threading.Thread):
    command_info = ''

    def __init__(self):
        threading.Thread.__init__(self)
        self.help_info()
    def run(self):
        while True:
            cmd_event.clear()           #阻塞

            info = input("请输入操作指令>>>>>>").strip()
            if not info:
                continue
            elif info == "exit":
                Manage()
            My_command.command_info = info
            cmd_event.set()             #非阻塞
    def help_info(self):
        tips = '''
--------------------常用操作命令指南如下---------------
        上传命令:put local_file remote_file
        下载命令:get remote_file local_file
        查看主机当前路径:pwd
        查看磁盘空间使用情况:df -h
        查看当前目录的所有文件:ls
        退到主入口:exit
------------------------------------------------------
        '''
        print(tips)
cmd_event = threading.Event()
cmd_event.clear()       #阻塞
