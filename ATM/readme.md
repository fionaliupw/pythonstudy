# readme

标签（空格分隔）： 未分类

---

###1、功能需求
1、额度 15000或自定义
2、实现购物商城，买东西加入 购物车，调用信用卡接口结账
3、可以提现，手续费5%
4、支持多账户登录
5、支持账户间转账
6、记录每月日常消费流水
7、提供还款接口
8、ATM记录操作日志 
9、提供管理接口，包括添加账户、用户额度，冻结账户等。。。
10、用户认证用装饰器

###2、程序结构
        ├── ATM
            ├── readme.md
            ├── core 
            │   ├── __init__.py
            │   └── main.py  #主程序(启动程序)
            ├── conf #配置文件目录
            │   ├── __init__.py
            │   └── setting.py
            ├── modules #程序核心目录
            │   ├── __init__.py
            │   ├── admincenter.py  #管理模块
            │   ├── authentication.py  #认证模块
            │   ├── creditcard.py  #信用卡模块
            │   ├── shopping.py  #购物模块
            ├── database #程序数据库
            │   ├── creditcard_dict  #信用卡数据库
            │   ├── creditcard_record  #信用卡流水记录数据库
            │   ├── details_tip  #提示信息
                ├── admincenter_dict  #后台管理账户密码
            │   ├── product_list  #商城产品数据库
            │   └── shopping_car  #购物车数据库
            │   ├── shopping_record  #购物记录
                └── users_dict  #用户数据库
          
