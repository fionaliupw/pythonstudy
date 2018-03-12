#_*_coding:utf-8*_
#Author:Fiona

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

# print(sys.argv)
if __name__ == '__main__':
    from modules.actions import excute_from_command_line
    excute_from_command_line(sys.argv)