#_*_coding:utf-8*_
#Author:Fiona

#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-Author-Lian

import os,json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''数据库文件相对路径'''
__db_users_dict = BASE_DIR + r"\database\users_dict"
__db_creditcard_dict = BASE_DIR + r"\database\creditcard_dict"

'''创建用户'''
def User_create(address="None",locked=0,creditcard=0):
    while True:
        print("开始创建用户".center(50,"-"))
        with open(__db_users_dict, "r+") as f_users_dict:
            users_dict = json.loads(f_users_dict.read())
            for key in users_dict:
                print("系统已有用户 【%s】" % (key))
            if_create = input("\n\33[34;0m是否创建新的用户 确定【y】/返回【b】\33[0m:")
            if if_create == "y":
                username = input("\33[34;0m输入要添加账户的用户名：\33[0m")
                password = input("\33[34;0m输入添加账户的密码：\33[0m")
                if username not in users_dict.keys():
                    if len(username.strip()) > 0:
                       if len(password.strip()) > 0:
                           users_dict[username] = {"username":username,"password":password,"creditcard":creditcard,"address":address,
                                                      "locked":locked}
                           dict = json.dumps(users_dict)
                           f_users_dict.seek(0)
                           f_users_dict.truncate(0)
                           f_users_dict.write(dict)
                           print("\33[31;1m创建用户 %s 成功\33[0m\n"%(username))
                       else:
                           print("\33[31;0m输入的密码为空\33[0m\n")
                    else:
                        print("\33[31;0m输入的用户名为空\33[0m\n")
                else:
                    print("\33[31;0m用户名 %s 已经存在\33[0m\n"%(username))
            if if_create == "b":
                break


'''发行信用卡'''
def Creditcard_create(limit=15000,locked=0):
    while True:
        print("发行信用卡".center(50, "-"))
        with open(__db_creditcard_dict, "r+") as f_creditcard_dict:
            creditcard_dict = json.loads(f_creditcard_dict.read())
            for key in creditcard_dict:
                print("系统已有信用卡 【%s】 \t持卡人 【%s】" % (key,creditcard_dict[key]["personinfo"]))
            if_create = input("\n\33[34;0m是否发行新的信用卡 确定【y】/返回【b】\33[0m:")
            if if_create == "y":
                creditcard = input("\33[34;0m输入要发行信用卡卡号(6位数字)：\33[0m")
                if creditcard not in creditcard_dict.keys():
                    if creditcard.isdigit() and len(creditcard) == 6:
                        password = input("\33[34;0m输入要发行信用卡的密码：\33[0m")
                        if len(password.strip()) > 0:
                            personinfo = input("\33[34;0m输入要发行信用卡申请人：\33[0m")
                            if len(personinfo.strip()) > 0:
                                creditcard_dict[creditcard] = {"creditcard":creditcard, "password":password, "personinfo":personinfo,
                                                        "limit":limit,"limitcash":limit//2,"locked":locked,"deflimit":limit}
                                dict = json.dumps(creditcard_dict)
                                f_creditcard_dict.seek(0)
                                f_creditcard_dict.truncate(0)
                                f_creditcard_dict.write(dict)
                                print("\33[31;0m发行信用卡 %s 成功 额度 %s\33[0m\n"%(creditcard,limit))
                            else:
                                print("\33[31;0m信用卡申请人不能为空\33[0m\n")
                        else:
                            print("\33[31;0m输入的密码为空\33[0m\n")
                    else:
                        print("\33[31;0m信用卡 %s 卡号不符合规范\33[0m\n" % (creditcard))
                else:
                    print("\33[31;0m信用卡 %s 已经存在\33[0m\n" % (creditcard))
            if if_create == "b":
                break

'''锁定用户'''
def Lock_user():
    while True:
        print("\33[32;0m锁定用户\33[0m".center(50, "-"))
        with open(__db_users_dict, "r+") as f_users_dict:
            users_dict = json.loads(f_users_dict.read())
            for key in users_dict:
                if users_dict[key]["locked"] == 0:
                    print("系统用户 【%s】\t\t锁定状态：【未锁定】"%(key))
                else:
                    print("系统用户 【%s】\t\t锁定状态：\33[7m【已锁定】\33[0m" % (key))
            if_lock = input("\n\33[34;0m是否进行用户锁定 确定【y】/返回【b】\33[0m:")
            if if_lock == "y":
                lock_user = input("\33[34;0m输入要锁定的用户名\33[0m:")
                if lock_user in users_dict.keys():
                    if users_dict[lock_user]["locked"] == 0:
                        users_dict[lock_user]["locked"] = 1
                        dict = json.dumps(users_dict)
                        f_users_dict.seek(0)
                        f_users_dict.truncate(0)
                        f_users_dict.write(dict)
                        print("\33[31;1m用户 %s 锁定成功\33[0m\n" % (lock_user))
                    else:
                        print("\33[31;0m用户 %s 锁定失败 之前已经被锁定\33[0m\n" % (lock_user))
                else:
                    print("\33[31;0m用户 %s 不存在\33[0m\n"%(lock_user))
            if if_lock == "b":
                break

'''解锁用户'''
def Unlock_user():
    while True:
        print("\33[32;0m解锁用户\33[0m".center(50, "-"))
        with open(__db_users_dict, "r+") as f_users_dict:
            users_dict = json.loads(f_users_dict.read())
            for key in users_dict:
                if users_dict[key]["locked"] == 0:
                    print("系统用户 【%s】\t\t锁定状态：【未锁定】" % (key))
                else:
                    print("系统用户 【%s】\t\t锁定状态：\33[7m【已锁定】\33[0m" % (key))
            if_lock = input("\n\33[34;0m是否进行用户解锁 确定【y】/返回【b】\33[0m:")
            if if_lock == "y":
                unlock_user = input("\33[34;0m输入要解锁的用户名\33[0m:")
                if unlock_user in users_dict.keys():
                    if users_dict[unlock_user]["locked"] == 1:
                        users_dict[unlock_user]["locked"] = 0
                        dict = json.dumps(users_dict)
                        f_users_dict.seek(0)
                        f_users_dict.truncate(0)
                        f_users_dict.write(dict)
                        print("\33[31;1m用户 %s 解锁成功\33[0m\n" % (unlock_user))
                    else:
                        print("\33[31;0m用户 %s 解锁失败 用户未被锁定\33[0m\n" % (unlock_user))
                else:
                    print("\33[31;0m用户 %s 不存在\33[0m\n"%(unlock_user))
            if if_lock == "b":
                break


'''冻结信用卡'''
def Lock_creditcard():
    while True:
        print("\33[32;0m冻结信用卡\33[0m".center(50, "-"))
        with open(__db_creditcard_dict, "r+") as f_creditcard_dict:
            creditcard_dict = json.loads(f_creditcard_dict.read())
            for key in creditcard_dict:
                if creditcard_dict[key]["locked"] == 0:
                    print("信用卡 【%s】\t\t冻结状态：【未冻结】" % (key))
                else:
                    print("信用卡 【%s】\t\t冻结状态：\33[7m【已冻结】\33[0m" % (key))
            if_Unlock = input("\n\33[34;0m是否进行信用卡冻结 确定【y】/返回【b】\33[0m:")
            if if_Unlock == "y":
                creditcard = input("\33[34;0m输入要冻结的信用卡卡号\33[0m:")
                if creditcard in creditcard_dict.keys():
                    if creditcard_dict[creditcard]["locked"] == 0:
                        creditcard_dict[creditcard]["locked"] = 1
                        dict = json.dumps(creditcard_dict)
                        f_creditcard_dict.seek(0)
                        f_creditcard_dict.truncate(0)
                        f_creditcard_dict.write(dict)
                        print("\33[31;1m信用卡 %s 冻结成功\33[0m\n" % (creditcard))
                    else:
                        print("\33[31;0m信用卡 %s 冻结失败 之前已经被冻结\33[0m\n" % (creditcard))
                else:
                    print("\33[31;0m信用卡 %s 不存在\33[0m\n" %(creditcard))
            if if_Unlock == "b":
                break


'''解冻信用卡'''
def Unlock_creditcard():
    while True:
        print("\33[32;0m解冻信用卡\33[0m".center(50, "-"))
        with open(__db_creditcard_dict, "r+") as f_creditcard_dict:
            creditcard_dict = json.loads(f_creditcard_dict.read())
            for key in creditcard_dict:
                if creditcard_dict[key]["locked"] == 0:
                    print("信用卡 【%s】\t\t冻结状态：【未冻结】" % (key))
                else:
                    print("信用卡 【%s】\t\t冻结状态：\33[7m【已冻结】\33[0m" % (key))
            if_Unlock = input("\n\33[34;0m是否进行信用卡解冻 确定【y】/返回【b】\33[0m:")
            if if_Unlock == "y":
                creditcard = input("\33[34;0m输入要解冻的信用卡卡号\33[0m:")
                if creditcard in creditcard_dict.keys():
                    if creditcard_dict[creditcard]["locked"] == 1:
                        creditcard_dict[creditcard]["locked"] = 0
                        dict = json.dumps(creditcard_dict)
                        f_creditcard_dict.seek(0)
                        f_creditcard_dict.truncate(0)
                        f_creditcard_dict.write(dict)
                        print("\33[31;1m信用卡 %s 解冻成功\33[0m\n" % (creditcard))
                    else:
                        print("\33[31;0m信用卡 %s 解冻失败 之前未被冻结\33[0m\n" % (creditcard))
                else:
                    print("\33[31;0m信用卡 %s 不存在\33[0m\n" % (creditcard))
            if if_Unlock == "b":
                break


'''修改信用卡额度'''
def Updata_limit():
    while True:
        print("\33[32;0m修改信用卡额度\33[0m".center(70, "-"))
        with open(__db_creditcard_dict, "r+") as f_creditcard_dict:
            creditcard_dict = json.loads(f_creditcard_dict.read())
            for key in creditcard_dict:
                    limitcash = creditcard_dict[key]["limitcash"]
                    print("信用卡 【%s】\t目前可用额度：【￥%s】\t取现额度：【￥%s】" %
                          (key,creditcard_dict[key]["limit"],limitcash))
            if_Updata = input("\n\33[34;0m是否进行信用卡额度调整 确定【y】/返回【b】\33[0m:")
            if if_Updata == "y":
                creditcard = input("\33[34;0m输入要修改额度的信用卡卡号\33[0m:")
                if creditcard in creditcard_dict.keys():
                    limit = input("\33[34;0m输入额度修改后的金额(至少￥5000)\33[0m:")
                    if limit.isdigit():
                        limit_default = creditcard_dict[creditcard]["deflimit"]
                        limit = int(limit)
                        if limit >=5000:
                            updata = limit - limit_default
                            creditcard_dict[creditcard]["limit"] +=updata
                            creditcard_dict[creditcard]["limitcash"] += updata//2
                            creditcard_dict[creditcard]["deflimit"]=limit
                            dict = json.dumps(creditcard_dict)
                            f_creditcard_dict.seek(0)
                            f_creditcard_dict.truncate(0)
                            f_creditcard_dict.write(dict)
                            print("\33[31;1m信用卡 %s 额度修改成功 额度 %s \33[0m\n" % (creditcard,limit))
                        else:
                            print("\33[31;0m输入金额 ￥%s 小于￥5000\33[0m\n" % (limit))
                    else:
                        print("\33[31;0m输入金额 ￥%s 格式错误\33[0m\n" % (limit))
                else:
                    print("\33[31;0m信用卡 【%s】 不存在\33[0m\n" % (creditcard))
            if if_Updata == "b":
                break
