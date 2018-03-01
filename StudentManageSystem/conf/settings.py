#_*_coding:utf-8*_
#Author:Fiona
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://testuser:test_clic1234@localhost/test",encoding='utf-8', echo=True)