#_*_coding:utf-8*_
#Author:Fiona

import hashlib
import time

def create_md():
    tmp = hashlib.md5()
    tmp.update(bytes(str(time.time()),encoding="utf-8"))
    return tmp.hexdigest()