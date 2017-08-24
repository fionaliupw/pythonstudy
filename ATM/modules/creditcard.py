#_*_coding:utf-8*_
#Author:Fiona

#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-Author-Lian

import json,os,datetime,time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#数据库文件相对路径
__db_creditcard_dict = BASE_DIR + r"\database\creditcard_dict"
__db_details_tip = BASE_DIR + r"\database\details_tip"
__db_creditcard_record = BASE_DIR + r"\database\creditcard_record"

#取现需知
def details_tip():
    with open(__db_details_tip,"r",encoding="utf-8") as f_details_tip:
        print(f_details_tip.read())

#  我的信用卡----选项
def My_creditcard(current_creditcard):
    while True:
        print("\33[32;0m我的信用卡信息\33[0m".center(40, "-"))
        with open(__db_creditcard_dict, "r+") as f_creditcard_dict:
            creditcard_dict = json.loads(f_creditcard_dict.read())
            print("卡号：\t【%s】\n额度:\t【￥%s】\n提现额度:\t【￥%s】\n持卡人:\t【%s】\n"%(current_creditcard,
            creditcard_dict[current_creditcard]["limit"],creditcard_dict[current_creditcard]["limitcash"],
            creditcard_dict[current_creditcard]["personinfo"]))
            if_back = input("\33[34;0m是否退出 返回【b】\33[0m:")
            if if_back == "b":
                break


#信用卡流水记录
def Creditcard_record(creditcard,value):
    with open(__db_creditcard_record, "r+") as f_creditcard_record:
        record_dict = json.loads(f_creditcard_record.read())
        month = time.strftime('%Y-%m-%d', time.localtime())
        times = time.strftime("%H:%M:%S")
        if str(creditcard) not in record_dict.keys():
            record_dict[creditcard]={month:{times:value}}
        else:
            if month not in record_dict[creditcard].keys():
                record_dict[creditcard][month] = {times: value}
            else:
                record_dict[creditcard][month][times] = value
        dict = json.dumps(record_dict)
        f_creditcard_record.seek(0)
        f_creditcard_record.truncate(0)
        f_creditcard_record.write(dict)


#提现
def Cash_advance(current_creditcard):
    while True:
            print("\33[32;0m提现\33[0m".center(40, "-"))
            with open(__db_creditcard_dict, "r+") as f_creditcard_dict:
                creditcard_dict = json.loads(f_creditcard_dict.read())
                limit = creditcard_dict[current_creditcard]["limit"]
                limitcash = creditcard_dict[current_creditcard]["limitcash"]
                print("信用卡号：\t【%s】\n提现额度:\t【￥%s】" % (current_creditcard, limitcash))
                if limit >= limitcash:
                    print("可提现金额:\t【￥%s】\n" % (limitcash))
                    details_tip()
                    if_adv = input("\n\33[34;0m是否进行提现 确定【y】/返回【b】\33[0m:")
                    if if_adv == "y":
                        cash = input("\33[34;0m输入要提现的金额 提现手续费按提现金额的5%进行收取\33[0m:")
                        if cash.isdigit():
                            cash=int(cash)
                            if cash != 0:
                                    if cash <= limitcash:
                                        limitcash = limitcash - int(cash*1.05)
                                        limit = limit - int(cash*1.05)
                                        creditcard_dict[current_creditcard]["limit"]=limit
                                        creditcard_dict[current_creditcard]["limitcash"] = limitcash
                                        f_creditcard_dict.seek(0)
                                        f_creditcard_dict.truncate(0)
                                        dict = json.dumps(creditcard_dict)
                                        f_creditcard_dict.write(dict)
                                        record = "\33[31;1m提现￥%s 手续费￥%s\33[0m"%(cash,int(cash*0.05))
                                        print(record,"\n")
                                        Creditcard_record(current_creditcard,record)
                                    else:
                                         print("\33[31;0m超出信用卡提现额度\33[0m\n")
                            else:
                                 print("\33[31;0m提现额度不能为空\33[0m\n")
                    if if_adv == "b":
                        break

                if limit < limitcash:
                    print("可提现金额:\t￥【%s】\n" % (int(limit*0.95)))
                    details_tip()
                    if_adv = input("\n\33[34;0m是否进行提现 确定【y】/返回【b】\33[0m:")
                    if if_adv == "y":
                        cash = input("\33[34;0m输入要提现的金额 收取%5手续费\33[0m:")
                        if cash.isdigit():
                            cash = int(cash)
                            if cash != 0:
                                    if cash <= int(limit*0.95):
                                        limit = limit - int(cash * 1.05)
                                        limitcash = limitcash - int(cash * 1.05)
                                        creditcard_dict[current_creditcard]["limitcash"] = limitcash
                                        creditcard_dict[current_creditcard]["limit"] = limit
                                        f_creditcard_dict.seek(0)
                                        f_creditcard_dict.truncate(0)
                                        dict = json.dumps(creditcard_dict)
                                        f_creditcard_dict.write(dict)
                                        record= "\33[31;1m提现￥%s 手续费￥%s\33[0m" % (cash, int(cash * 0.05))
                                        print(record,"\n")
                                        Creditcard_record(current_creditcard, record)
                                    else:
                                        print("\33[31;0m信用卡没有足够的额度去支付提现，请去【我的信用卡】查看当前额度\33[0m\n")
                            else:
                                print("\33[31;0m提现额度不能为空\33[0m\n")
                    if if_adv == "b":
                        break


#转账
def Transfer(current_creditcard):
    while True:
        print("\33[32;0m转账\33[0m".center(40, "-"))
        if_trans = input("\n\33[34;0m是否进行转账 确定【y】/返回【b】\33[0m:")
        if if_trans == "y":
            with open(__db_creditcard_dict, "r+") as f_creditcard_dict:
                creditcard_dict = json.loads(f_creditcard_dict.read())
                current_limit = creditcard_dict[current_creditcard]["limit"]
                transfer_creditcard = input("\33[34;0m输入转账的银行卡卡号\33[0m:")
                if transfer_creditcard.isdigit():
                    if len(transfer_creditcard) == 6:
                        if transfer_creditcard in creditcard_dict.keys():
                            again_creditcard = input("\33[34;0m再次确认转账的银行卡卡号\33[0m:")
                            if transfer_creditcard == again_creditcard:
                                transfer_cash = input("\33[34;0m输入转账的金额\33[0m:")
                                if transfer_cash.isdigit():
                                    transfer_cash=int(transfer_cash)
                                    if transfer_cash <= current_limit:
                                        transfer_limit = creditcard_dict[current_creditcard]["limit"]
                                        creditcard_dict[current_creditcard]["limit"] = current_limit-transfer_cash
                                        creditcard_dict[transfer_creditcard]["limit"] = transfer_limit+transfer_cash
                                        f_creditcard_dict.seek(0)
                                        f_creditcard_dict.truncate(0)
                                        dict = json.dumps(creditcard_dict)
                                        f_creditcard_dict.write(dict)
                                        record="\33[31;1m转账卡号 %s 金额 ￥%s 转账成功\33[0m"%(transfer_creditcard,transfer_cash)
                                        print(record,"\n")
                                        Creditcard_record(current_creditcard, record)
                                    else:
                                        print("\33[31;0m金额不足 转账失败\33[0m\n")
                                else:
                                    print("\33[31;0m输入金额有误\33[0m\n")
                            else:
                                print("\33[31;0m两次输入银行卡卡号不一致\33[0m\n")
                        else:
                            print("\33[31;0m输入银行卡不存在\33[0m\n")
                    else:
                        print("\33[31;0m输入银行卡有误\33[0m\n")
                else:
                    print("\33[31;0m输入银行卡有误\33[0m\n")
        if if_trans == "b":
            break


#还款
def Repayment(current_creditcard):
    while True:
        print("\33[32;0m还款\33[0m".center(40, "-"))
        if_repay = input("\n\33[34;0m是否进行还款 确定【y】/返回【b】\33[0m:")
        if if_repay == "y":
            repay_cash = input("\33[34;0m输入要还款的金额\33[0m:")
            if repay_cash.isdigit():
                repay_cash=int(repay_cash)
                with open(__db_creditcard_dict, "r+") as f_creditcard_dict:
                    creditcard_dict = json.loads(f_creditcard_dict.read())
                    limit = creditcard_dict[current_creditcard]["limit"]
                    limit = limit+repay_cash
                    creditcard_dict[current_creditcard]["limit"]=limit
                    f_creditcard_dict.seek(0)
                    f_creditcard_dict.truncate(0)
                    dict = json.dumps(creditcard_dict)
                    f_creditcard_dict.write(dict)
                    record="\33[31;1m信用卡 %s 还款金额 ￥%s 还款成功\33[0m" % (current_creditcard, repay_cash)
                    print(record,"\n")
                    Creditcard_record(current_creditcard, record)
            else:
                print("\33[31;0m输入金额格式有误\33[0m\n")
        if if_repay == "b":
            break




#查看信用卡流水
def Catcard_record(current_creditcard):
    while True:
        print("\33[32;0m信用卡流水单\33[0m".center(40, "-"))
        with open(__db_creditcard_record, "r+") as f_creditcard_record:
            f_creditcard_record.seek(0)
            record_dict = json.loads(f_creditcard_record.read())
            #print(record_dict)
            print("\33[34;0m流水单日期\33[0m:")
            if current_creditcard in record_dict.keys():
                for key in record_dict[current_creditcard]:
                    print(key)
                date = input("\n\33[34;0m流水单查询 返回【b】 / 输入流水单的日期【2000-01-01】\33[0m:")
                if date == "b":
                    break
                if date in record_dict[current_creditcard].keys():
                    keys = sorted(record_dict[current_creditcard][date])
                    print("\33[31;1m当前信用卡【%s】 交易记录-》》\33[0m"%(current_creditcard))
                    for key in keys:
                        print("\33[31;1m时间：%s  %s\33[0m"%(key,record_dict[current_creditcard][date][key]))
                    print("")
                else:
                    print("\33[31;0m输入的日期有误\33[0m\n")
            else:
                print("\33[31;0m信用卡 %s 还没有进行过消费\33[0m\n"%(current_creditcard))
                break
