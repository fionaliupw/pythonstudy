# test

标签（空格分隔）： 未分类

---

1、实现以下需求：
（1）可进行模糊查询，查询语法只支持下面3种:
　　select name,age from staff_table where age > 22
　　select  * from staff_table where dept = IT
    select  * from staff_table where enroll_date like 2013
（2）查到的信息，打印后，最后面还要显示查到的条数
（3）可创建新员工纪录，以phone做唯一键，staff_id需自增
    insert staff_table values (Fiona,27,100054618,IT,2015-07-01)
其中，员工号自增
（4）可删除指定员工信息纪录，输入员工id，即可删除
    delete from staff_table where staff_id = 1
（5）可修改员工信息，语法如下:
　　update staff_table set dept = Market where dept = IT
(6)输入exit退出程序，并打印最新的表数据。

2、测试
输入sql语法时，请注意字符串之前需要有空格，否则程序报错。

（1）运行程序后，显示欢迎页，并提示**请输入编号,输入exit则退出程序！>>>:**

> 欢迎页内容
--------------------------------------------------------------------------------
                           欢迎使用员工信息表程序                            

程序使用说明：
请输入编号进行相应操作，编号
本程序只支持以下几种增删改查的sql语句：
1、增加:insert staff_table values (Fiona,27,100054618,IT,2015-07-01)
2、删除:delete from staff_table where staff_id = 1
3、修改:update staff_table set dept = 运维 where dept = IT
4、查询:select name,age from staff_table where age > 22
        select * from staff_table where dept = IT
        select * from staff_table where enroll_date like 2013
        
--------------------------------------------------------------------------------
（2）输入编号进入下一步查询，或输入exit退出程序

> 编号1表示增加员工信息；编号2表示删除员工信息；编号3表示修改员工信息；编号4表示查询员工信息；exit表示退出程序。

（3）输入编号1，提示如下：
请根据需要输入相应sql语句

    >>>:insert staff_table values (Fiona,27,100054618,IT,2015-07-01)
    输出结果：
    ['3', 'Fiona', '27', '100054618', 'IT', '2015-07-01']
    员工信息添加成功！
输入编号2，提示如下：
请根据需要输入相应sql语句

    >>>:delete from staff_table where staff_id = 1
    ['0', 'Mike', '25', '13900000001', 'FMD', '2016-08-01']
    ['2', 'Sissi', '21', '1360000001', 'Sales', '2017-07-01']
    ['3', 'Fiona', '27', '100054618', 'IT', '2015-07-01']
    员工信息删除成功！
    
输入编号3，提示如下：
请根据需要输入相应sql语句

    >>>:update staff_table set dept = 运维 where dept = IT
    ['0', 'Mike', '25', '13900000001', 'FMD', '2016-08-01']
    ['1', 'Alex', '37', '15900000001', 'HR', '2010-07-01']
    ['2', 'Sissi', '21', '1360000001', 'Sales', '2017-07-01']
    ['3', 'Fiona', '27', '100054618', '运维', '2015-07-01']
    修改成功！
输入编号4，提示如下：
可进行3种查询：
1、请根据需要输入相应sql语句

    >>>:select name,age from staff_table where age > 22
------name,age------
      Mike 25       
      Fiona 27       
查询到2条记录！
2、请根据需要输入相应sql语句

    >>>:select * from staff_table where dept = FMD
-----------------------查询结果-----------------------
['0', 'Mike', '25', '13900000001', 'FMD', '2016-08-01']
查询到1条记录！
3、请根据需要输入相应sql语句

    >>>:select * from staff_table where enroll_date like 2013
-----------------------查询结果-----------------------
查询到0条记录！

