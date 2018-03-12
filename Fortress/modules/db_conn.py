#_*_coding:utf-8*_
#Author:Fiona

from sqlalchemy import create_engine,Table
from sqlalchemy.orm import sessionmaker
from conf import settings

engine = create_engine(settings.DB_CONN)

SessionCls = sessionmaker(bind=engine)  #创建会话类，返回一个class
session = SessionCls()       #实例化