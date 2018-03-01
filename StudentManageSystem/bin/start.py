#_*_coding:utf-8*_
#Author:Fiona

import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings
from modules import models
from modules import actions

if __name__ == '__main__':
    obj = actions.Action()
    obj.func()