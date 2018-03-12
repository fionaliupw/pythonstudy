# test

标签（空格分隔）： 未分类

---

执行命令创建表结构
[star@localhost Fortress]$ python bin/start.py syncdb
Syncing DB....

执行start_session
[star@localhost Fortress]$ python bin/start.py start_session
going to start sesssion 
Username:Fiona
Password:

执行create_groups -f
[star@localhost Fortress]$ python bin/start.py create_groups -f share/examples/new_groups.yml

执行create_users -f
[star@localhost Fortress]$ python bin/start.py create_users -f share/examples/new_users.yml

执行create_hosts -f
[star@localhost Fortress]$ python bin/start.py create_hosts -f share/examples/new_hosts.yml

执行create_bindhosts -f
[star@localhost Fortress]$ python bin/start.py create_bindhosts -f share/examples/new_bindhosts.yml

执行create_remoteusers -f
[star@localhost Fortress]$ python bin/start.py create_remoteusers -f share/examples/new_remoteusers.yml


