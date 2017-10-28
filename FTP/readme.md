# readme

标签（空格分隔）： readme

---

## 程序实现以下需求：
开发简单的FTP：
1. 用户登陆
2. 上传/下载文件
3. 不同用户家目录不同
4. 查看当前目录下文件
5. 充分使用面向对象知识

## 程序结构图
├── FTP #主目录
    ├── __init__.py
    ├── ftpclient                 #FTP客户端目录
    │   ├── __init__.py
    │   ├── ftpclient.py          #FTP客户端执行程序
    ├── ftpserver                 #FTP服务端目录
    │   ├── __init__.py
    │   ├── server.py             #FTP服务端执行程序
    ├── conf                      #配置目录
    │   ├── __init__.py
    │   ├── settings.py           #环境变量、相关目录及参数配置程序
    ├── modules
    │   ├── __init__.py
    │   ├── auth_user.py          #用户认证程序
    │   ├── socket_server.py      #socketserver程序
    ├── home
        └── Fiona    #用户Fiona的家目录
        └── Ana      #用户Ana的家目录
        └── Mike     #用户Mike的家目录
    ├── database
        └── Fiona.db    #用户Fiona数据库文件
        └── Ana.db      #用户Ana数据库文件
        └── Mike.db     #用户Mike数据库文件
        