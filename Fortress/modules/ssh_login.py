#_*_coding:utf-8*_
#Author:Fiona

import paramiko
from modules import models
import datetime
import traceback
import sys
try:
    import interactive
except ImportError:
    from . import interactive
def ssh_login(user_obj,bind_host_obj,mysql_engine,log_recording):
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())
        print('***Connecting***')
        client.connect(bind_host_obj.host.ip_addr,
                       bind_host_obj.host.port,
                       bind_host_obj.remoteuser.username,
                       bind_host_obj.remoteuser.password,
                       timeout=30)
        cmd_caches = []
        chan = client.invoke_shell()
        print(repr(client.get_transport()))
        cmd_caches.append(models.AuditLog(user_id = user_obj.id,
                                          bind_host_id = bind_host_obj.id,
                                          action_type = 'login',
                                          date = datetime.datetime.now()
                                          ))
        log_recording(user_obj,bind_host_obj,cmd_caches)
        interactive.interactive_shell(chan,user_obj,bind_host_obj,cmd_caches,log_recording)
        chan.close()
        client.close()
    except Exception as e:
        print('Caught Exception:%s:%s' % (e.__class__,e))
        traceback.print_exc()
        try:
            client.close()
        except:
            pass
        sys.exit(1)