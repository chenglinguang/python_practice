#!/usr/bin/env python3 

#-*-coding:utf-8-*-

import mysql.connector

conn=mysql.connector.connect(user='root',password='123456789',database='test')

cursor=conn.cursor()

#cursor.execute('create table newuser (id varchar(20) primary key,name varchar(20))')

#cursor.execute('insert into newuser (id,name) values(%s,%s)',['2','Chris'])


conn.commit()
cursor.close()

cursor=conn.cursor()
cursor.execute('select * from newuser where id=%s',('1',))
#cursor.execute('select * from newuser')
values=cursor.fetchall()

print(values)

cursor.close()

conn.close()



