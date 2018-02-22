#_*_coding:utf-8*_
#Author:Fiona

import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

download_path = os.path.join(os.path.sep,BASE_DIR,'db','server_download')
upload_path = os.path.join(os.path.sep,BASE_DIR,'db','server_upload')
client_download_path = os.path.join(os.path.sep,BASE_DIR,'db','client_download_path')