#!/usr/bin/env python3 

#-*-coding:utf-8-*-

import os,sqlite3

db_file=os.path.join(os.path.dirname(__file__),'test.db')

if os.path.isfile(db_file):
    os.remove(db_file)

conn=sqlite3.connect('test.db')
cursor=conn.cursor()
cursor.execute('create table user (id varchar(20) primary key,name varchar(20),score int)')
cursor.execute(r"insert into user values ('A-001','Adm',95)")
cursor.execute(r"insert into user values ('A-002','Bart',62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low,high):
    names=[]
    try:
        conn=sqlite3.connect('test.db')
        cursor=conn.cursor()
    except:
        print('DB test.db can\'t be connected') 
    finally:
        cursor.execute('select name,score from user where score>? and score <? order by score',(low,high))
        values=cursor.fetchall()
        for data in values:
            names.append(data[0])
    return names


print(get_score_in(70,80))




