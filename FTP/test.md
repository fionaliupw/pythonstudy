﻿# test

标签（空格分隔）： test

---


0. 用户字典
3个测试用户信息：USERS_DICT = {"Fiona":"123456","Ana":"888888","Mike":"666666"}
1. 执行服务端程序提供服务ftpserver/server.py
2. 执行客户端程序ftpclient/ftpclient.py

> 输入用户名：Fiona 
> 输入密码：123456 
> [200]用户密码认证通过
> ->pwd 
> C:\Users\chinalife\Documents\pythonstudy\FTP\home\Fiona
> ->dir  
> 驱动器 C 中的卷是 Windows  
> 卷的序列号是 A8BD-4839
> 
>  C:\Users\chinalife\Documents\pythonstudy\FTP\home\Fiona 的目录
> 
> 2017/10/28  09:38    <DIR>          . 
> 2017/10/28  09:38    <DIR>      .. 
> 2017/10/28  09:38    50 test1.txt 
> 2017/10/28  09:38    18 test2.log
>                2 个文件             68 字节
>                2 个目录 62,956,969,984 可用字节
> 
> ->get test1.txt 
> [>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100.00% 文件一致
> ->put ftpclient.py [>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100.00% 文件具有一致性
> ->






