#_*_coding:utf-8*_
#Author:Fiona

import socket
import hashlib
import os
import sys
sys.path.append("..")
#ftp客户端
class Myclient():
    def __init__(self,ip_port):
        self.ip_port = ip_port

    #连接服务器
    def connect(self):
        self.client = socket.socket()
        self.client.connect(self.ip_port)
    #登陆认证
    def login(self):
        self.connect()
        while True:
            username = input("输入用户名：").strip()
            password = input("输入密码：").strip()
            user_info = ('%s:%s'%(username,password))
            self.client.sendall(user_info.encode())
            status_code = self.client.recv(1024).decode()
            if status_code == "400":
                print('[%s]用户密码认证错误'%status_code)
                continue
            else:
                print('[%s]用户密码认证通过'%status_code)
            self.interactive()
    #用户交互
    def interactive(self):
        while True:
            cmd = input("->").strip()
            if not cmd:
                continue
            cmd_str = cmd.split()[0]
            if hasattr(self,cmd_str):
                func = getattr(self,cmd_str)
                func(cmd)
            else:
                print("[%s]命令不存在"%401)
    #下载文件
    def get(self,cmd):
        self.client.sendall(cmd.encode())   #发送要执行的命令
        status_code = self.client.recv(1024).decode()
        if status_code == "201":
            filename = cmd.split()[1]
            #file存在，
            if os.path.isfile(filename):
                recv_size = os.stat(filename).st_size   #接收文件大小
                self.client.sendall("403".encode())
                response = self.client.recv(1024)
                self.client.sendall(str(recv_size).encode())   #发送已接收文件大小
                status_code = self.client.recv(1024).decode()
                # 文件大小不一致，续传
                if status_code == "205":
                    print("继续上次传输")
                    self.client.sendall("000".encode())
                # 文件大小一致，不续传,不下载
                elif status_code == "405":
                    print("文件已经存在，结束下载")
                    return
            #file不存在
            else:
                self.client.sendall("402".encode())
                recv_size = 0

            file_size = self.client.recv(1024).decode() #文件大小
            file_size = int(file_size)
            self.client.sendall("000".encode())

            #接收文件函数
            with open(filename,'ab') as f:
                file_size += recv_size
                m = hashlib.md5()
                while recv_size < file_size:
                    num_size = file_size - recv_size
                    if num_size > 1024:
                        t_size = 1024
                    else:
                        t_size = num_size
                    data = self.client.recv(t_size)
                    recv_size += len(data)
                    f.write(data)
                    m.update(data)
                    percent = recv_size*100.0 / file_size   #计算完成进度，格式为xx.xx%
                    recv_percent = int(percent)
                    remain_percent = 100 - recv_percent
                    process_bar = '[' + '>' * recv_percent + '-' * remain_percent + ']'\
                      + '%.2f' % percent + '%' + '\r' #带输出的字符串，'\r'表示不换行回到最左边
                    sys.stdout.write(process_bar) #这两句打印字符到终端
                    sys.stdout.flush()
                new_file_md5 = m.hexdigest()        #生成新文件的md5值
                server_file_md5 = self.client.recv(1024).decode()
                if new_file_md5 == server_file_md5:     #md5值一致
                    print("\n文件一致")
        else:print("[%s] Error！"%(status_code))
    #上传文件
    def put(self,cmd):
        if len(cmd.split()) > 1:
            filename = cmd.split()[1]
            if os.path.isfile(filename):                #文件是否存在
                self.client.sendall(cmd.encode())       #发送要执行的命令
                response = self.client.recv(1024)       #收到ACK确认
                file_size = os.stat(filename).st_size   #文件大小
                self.client.sendall(str(file_size).encode())  #发送文件大小
                status_code = self.client.recv(1024).decode()  #等待响应,返回状态码
                if status_code == "202":
                    with open(filename,"rb") as f:
                        m = hashlib.md5()
                        for line in f:
                            m.update(line)
                            send_size = f.tell()
                            self.client.sendall(line)
                            percent = send_size*100.0 / file_size   #计算完成进度，格式为xx.xx%
                            send_percent = int(percent)
                            remain_percent = 100 - send_percent
                            process_bar = '[' + '>' * send_percent + '-' * remain_percent + ']'\
                              + '%.2f' % percent + '%' + '\r' #带输出的字符串，'\r'表示不换行回到最左边
                            sys.stdout.write(process_bar) #这两句打印字符到终端
                            sys.stdout.flush()
                    self.client.sendall(m.hexdigest().encode())     #发送文件md5值
                    status_code = self.client.recv(1024).decode()  #返回状态码
                    if status_code == "203":
                        print("\n文件具有一致性")
                else:print("[%s] Error！"%(status_code))
            else:
                print("[402] Error")
        else: print("[401] Error")
    #查看当前目录下的文件
    def dir(self,cmd):
        self.universal_method_data(cmd)
        pass
    #查看当前用户路径
    def pwd(self,cmd):
        self.universal_method_data(cmd)
        pass
    #切换目录
    def cd(self,cmd):
        self.universal_method_none(cmd)
        pass
    #通用方法，无data输出
    def universal_method_none(self,cmd):
        self.client.sendall(cmd.encode())  # 发送要执行的命令
        status_code = self.client.recv(1024).decode()
        if status_code == "201":  # 命令可执行
            self.client.sendall("000".encode())  # 系统交互
        else:
            print("[%s] Error！" % (status_code))
    #通用方法，有data输出
    def universal_method_data(self,cmd):
        self.client.sendall(cmd.encode())   #发送要执行的命令
        status_code = self.client.recv(1024).decode()
        if status_code == "201":            #命令可执行
            self.client.sendall("000".encode())      #系统交互
            data = self.client.recv(1024).decode()
            print(data)
        else:print("[%s] Error！" % (status_code))

if __name__ == "__main__":
    ip_port =("127.0.0.1",9999)         #服务端ip、端口
    client = Myclient(ip_port)            #创建客户端实例
    client.login()                      #开始连接