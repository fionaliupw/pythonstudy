# Readme

标签（空格分隔）： 未分类

---

1、实现以下需求：
（1）可进行模糊查询，查询语法只支持下面3种:
　　select name,age from staff_table where age > 22
　　select  * from staff_table where dept = "IT"
    select  * from staff_table where enroll_date like "2013"
（2）查到的信息，打印后，最后面还要显示查到的条数
（3）可创建新员工纪录，以phone做唯一键，staff_id需自增
insert staff_table values ("Finao",25,15000234234,"IT","2017-08-01")
其中，员工号自增
（4）可删除指定员工信息纪录，输入员工id，即可删除
delete from staff_table where staff_id = 1
（5）可修改员工信息，语法如下:
　　UPDATE staff_table SET dept="Market" where dept = "IT"
(6)输入exit退出程序，并打印最新的表数据。

2、代码文件：staff_info.py

3、数据文件：staff_table,保存员工信息。
初始信息如下：
0,Mike,25,13900000001,FMD,2016-08-01
1,Alex,37,15900000001,HR,2010-07-01
2,Sissi,21,1360000001,Sales,2017-07-01





