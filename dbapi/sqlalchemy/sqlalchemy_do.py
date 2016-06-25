#!/usr/bin/env python3 

#-*-coding:utf-8-*-

#导入
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象基类
Base=declarative_base()

#定义newuser对象：
class NewUser(Base):
    #表的名称
    __tablename__='newuser'
    #表的结构
    id=Column(String(20),primary_key=True)
    name=Column(String(20))

#初始化数据库连接：
engine=create_engine('mysql+mysqlconnector://root:123456789@localhost:3306/test')
#创建DBSession类型
DBSession=sessionmaker(bind=engine)
#创建session对象
session=DBSession()
#创建新user对象
new_user=NewUser(id='5',name='Bob')
#添加到session
session.add(new_user)
#提交即保存到数据库：
session.commit()
#关闭session
session.close()




