#_*_coding:utf-8*_
#Author:Fiona
import os,sys

#程序主目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#添加环境变量
sys.path.append(BASE_DIR)

from modules import admincenter,shopping,authentication,creditcard

while True:
    print("\33[35;1m欢迎使用信用卡购物商城\33[0m".center(50, "#"),
          "\n1 购物中心\n"
          "2 信用卡中心\n"
          "3 后台管理\n")
    choice_id = input("\33[34;0m选择要进入模式的ID，输入q退出程序\33[0m:")

    if choice_id == "1":
        res = authentication.user_auth()
        if res  != None :
            if res[0] == "True":
                current_user = res[1]
                shopping.Empty_shopping_car()
                while True:
                    print("\33[36;1m欢迎进入购物中心\33[0m".center(50,"*"),
                          "\n1 购物商场\n"
                          "2 查看购物车\n"
                          "3 购物结算\n"
                          "4 个人中心\n")
                    choice_id = input("\33[34;0m选择要进入模式的ID，输入b返回上一级\33[0m:")
                    if choice_id == "1":
                        shopping.Shopping_mall()
                    elif choice_id == "2":
                        shopping.Shopping_car()
                    elif choice_id == "3":
                        shopping.Pay_shopping(current_user)
                    elif choice_id == "4":
                        while True:
                            print("\33[33;1m个人中心\33[0m".center(50, "*"),
                                      "\n1 购物历史记录\n"
                                      "2 修改登录密码\n"
                                      "3 修改个人信息\n"
                                      "4 修改行用卡绑定\n")
                            choice_id = input("\33[34;0m选择要进入模式的ID，输入b返回上一级\33[0m:")
                            if choice_id == "1":
                                shopping.Catcar_record(current_user)
                            elif choice_id == "2":
                                shopping.Updata_password(current_user)
                            elif choice_id == "3":
                                shopping.Updata_address(current_user)
                            elif choice_id == "4":
                                shopping.Link_creditcard(current_user)
                            elif choice_id == "b":
                                   break
                            else:
                                print("\33[31;0m输入的ID无效，请重新选择\33[0m")
                    elif choice_id == "b":
                        break
                    else:
                        print("\33[31;0m输入的ID无效，请重新选择\33[0m")

    elif choice_id == "2":
        res = authentication.creditcard_auth()
        if res != None:
            if res[0] == "True":
                current_creditcard= res[1]
                while True:
                    print("\33[36;1m信用卡中心\33[0m".center(50, "*"),
                          "\n1 我的信用卡\n"
                          "2 提现\n"
                          "3 转账\n"
                          "4 还款\n"
                          "5 流水记录\n")
                    choice_id = input("\33[34;0m选择要进入模式的ID，输入b返回上一级\33[0m:")
                    if choice_id == "1":
                        creditcard.My_creditcard(current_creditcard)
                    elif choice_id == "2":
                        creditcard.Cash_advance(current_creditcard)
                    elif choice_id == "3":
                        creditcard.Transfer(current_creditcard)
                    elif choice_id == "4":
                        creditcard.Repayment(current_creditcard)
                    elif choice_id == "5":
                        creditcard.Catcard_record(current_creditcard)
                    elif choice_id == "b":
                        break
                    else:
                        print("\33[31;0m输入的ID无效，请重新选择\33[0m")

    elif choice_id == "3":
        res = authentication.admincenter_auth()
        if res != None:
            while True:
                print("\33[36;1m管理中心\33[0m".center(50, "*"),
                      "\n1 创建账号\n"
                      "2 锁定账号\n"
                      "3 解锁账号\n"
                      "4 发行信用卡\n"
                      "5 冻结信用卡\n"
                      "6 解冻信用卡\n"
                      "7 提升信用卡额度\n")
                choice_id = input("\33[34;0m选择要进入模式的ID，输入b返回上一级\33[0m:")
                if choice_id == "1":
                    admincenter.User_create()
                elif choice_id == "2":
                    admincenter.Lock_user()
                elif choice_id == "3":
                    admincenter.Unlock_user()
                elif choice_id == "4":
                    admincenter.Creditcard_create()
                elif choice_id == "5":
                    admincenter.Lock_creditcard()
                elif choice_id == "6":
                    admincenter.Unlock_creditcard()
                elif choice_id == "7":
                    admincenter.Updata_limit()
                elif choice_id == "b":
                    break
                else:
                    print("\33[31;0m输入的ID无效，请重新选择\33[0m")

    elif choice_id == "q":
        break

    else:
        print("\33[31;0m输入的ID无效，请重新选择\33[0m")