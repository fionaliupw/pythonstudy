#_*_coding:utf-8*_
#Author:Fiona
#name,age,phone,dept,enroll_date

def info_welcome(): #欢迎页面信息打印
    print("-".center(80,"-"))
    print("\033[1;31;47m欢迎使用员工信息表程序\033[0m".center(80," "))
    help_info = '''
程序使用说明：
请输入编号进行相应操作，编号
本程序只支持以下几种增删改查的sql语句：
1、增加:insert staff_table values (Fiona,27,100054618,IT,2015-07-01)
2、删除:delete from staff_table where staff_id = 1
3、修改:update staff_table set dept = 运维 where dept = IT
4、查询:select name,age from staff_table where age > 22
        select * from staff_table where dept = IT
        select * from staff_table where enroll_date like 2013
        '''
    print(help_info)
    print("-".center(80,"-"))
    return 0


def insert(sql_text):
    sql_info = sql_text.split(" ")
    info = sql_info[3]
    len_info = len(info)
    info_data = info[1:len_info-1]
    info_list = info_data.split(",")
    # print(info_list)
    with open("staff_table","r",encoding="utf-8") as f1:
        list = []
        phone_list = []
        for line1 in f1:
            temp1 = line1.strip().split(",")
            phone_list.append(temp1[3])
        if info_list[2] in phone_list:
            print("手机号码已存在")
        else:
            with open("staff_table","r+",encoding="utf-8") as f2:
                for line2 in f2:
                    temp2 = line2.strip().split(",")
                    list.append(temp2)
                if len(list) == 0:
                    num = str(0)
                else:
                    num = str(int(list[-1][0])+1)
                info_list.insert(0,num)
                print(info_list)
                info_list = ",".join(info_list)
                f2.write(info_list)
                f2.write("\n")
                print("员工信息添加成功！")
    return 0

def delete(sql_text):
    sql_info = sql_text.split(" ")
    #要被删除的id信息存在则标记exist_flag为1
    exist_flag = 0

    with open("staff_table","r",encoding="utf-8") as f1:
        list = []
        for line1 in f1:
            temp1 = line1.strip().split(",")
            # list.append(temp1)
            if temp1[0] == sql_info[6]:
                #要被删除的id信息存在则标记exist_flag为1
                exist_flag = 1
            else:
                list.append(temp1)
        if len(list)+1 == 0:
            print("员工信息表为空！无内容可被删除！")
        else:
            if exist_flag == 1:
                with open("staff_table","w",encoding="utf-8") as f2:
                    for i in list:
                        print(i)
                        info_list = ",".join(i)
                        f2.write(info_list)
                        f2.write("\n")
                    print("员工信息删除成功！")
            else:
                print("不存在要被删除的员工信息记录！")
    return 0
def update(sql_text):
    sql_text = 'update staff_table set dept = 运维 where dept = IT'
    sql_info = sql_text.split(" ")
    with open("staff_table","r+",encoding="utf-8") as f1:
        list = []
        for line1 in f1:
            temp1 = line1.strip().split(",")
            # print(temp1)
            if sql_info[9] in temp1:
                temp1[4] = sql_info[5]
                # print(temp1)
            list.append(temp1)
    with open("staff_table","w",encoding="utf-8") as f2:
        for i in list:
            print(i)
            info_list = ",".join(i)
            f2.write(info_list)
            f2.write("\n")
        print("修改成功！")
    return 0

def select(sql_text):
    sql_info = sql_text.split(" ")
    #print(sql_info)
    if sql_text == ("select name,age from staff_table where age > %s"%(sql_info[7])):
        with open("staff_table","r",encoding="utf-8") as f1:
            list = []
            for line1 in f1:
                temp1 = line1.strip().split(",")
                if temp1[2]>sql_info[7]:
                    list.append(temp1[1:3])
            print("name,age".center(20,"-"))
            for i in list:
                print("%s %s".center(18," ")%(i[0],i[1]))
            print("查询到\033[1;31;47m%s\033[0m条记录！"%len(list))
    elif sql_text == ("select * from staff_table where dept = %s"%(sql_info[7])):
        with open("staff_table","r",encoding="utf-8") as f2:
            list = []
            for line2 in f2:
                temp2 = line2.strip().split(",")
                if temp2[4] == sql_info[7]:
                    list.append(temp2)
            print("查询结果".center(50,"-"))
            for i in list:
                print(i)
            print("查询到\033[1;31;47m%s\033[0m条记录！"%len(list))
    elif sql_text == ("select * from staff_table where enroll_date like %s"%(sql_info[7])):
        with open("staff_table","r",encoding="utf-8") as f3:
            list = []
            for line3 in f3:
                temp3 = line3.strip().split(",")
                if temp3[5][0:4] == sql_info[7]:
                    list.append(temp3)
            print("查询结果".center(50,"-"))
            for i in list:
                print(i)
            print("查询到\033[1;31;47m%s\033[0m条记录！"%len(list))
    return 0

def input_sql():
    input_text = input('请根据需要输入相应sql语句\n>>>:').strip()
    return input_text

exit_flag = 0
info_welcome()
while not exit_flag:
    input_num = input('请输入编号,输入exit则退出程序！>>>:')
    if input_num == 'exit':
        print("\033[1;31;47m退出成功！\033[0m")
        exit_flag = 1
    elif input_num.isdigit():
        # input_num = int(input_num)
        if input_num == "1":
            sql = input_sql()
            insert(sql)
        elif input_num == "2":
            sql = input_sql()
            delete(sql)
        elif input_num == "3":
            sql = input_sql()
            update(sql)
        elif input_num == "4":
            sql = input_sql()
            select(sql)
        else:
            print("您输入的编号不在范围之内，请重新输入！")
    else:
        print("您的输入不合法，请重新输入！")