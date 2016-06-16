#!/usr/bin/env python3 

#!-*- coding:uft-8 -*-

#摘要算法应用

import hashlib

md5=hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md5=hashlib.md5()
md5.update('how to use md5 in python '.encode('utf-8'))
md5.update('hashlib?'.encode('utf-8'))
print(md5.hexdigest())


sha1=hashlib.sha1()
sha1.update('how to use md5 in python '.encode('utf-8'))
sha1.update('hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

#任何允许用户登录的网站都会存储用户登录的用户名和口令。如何存储用户名和口令呢？方法是存到数据库表中：
#name    | password
#--------+----------
#michael | 123456
#bob     | abc999
#alice   | alice2008

#正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：
#username | password
#---------+---------------------------------
#michael  | e10adc3949ba59abbe56e057f20f883e
#bob      | 878ef96e86145580c38c87f0410ad153
#alice    | 99b1c2188db85afee403b1536010c2c9

#当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，如果不一致，口令肯定错误。


#def calc_md5(password):
#    pass


#db={
#    'michael': 'e10adc3949ba59abbe56e057f20f883e',
#    'bob': '878ef96e86145580c38c87f0410ad153',
#    'alice': '99b1c2188db85afee403b1536010c2c9'
#}


#def log(user,password):
#    pass


#由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符##串来实现，俗称“加盐”：
#如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。
#def calc_md5(password):
#    return get_md5(password + 'the-Salt')


db={}

def get_md5(s):
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return (md5.hexdigest())


def register(username,password):
    db[username]=get_md5(password+username+'the-Salt')
    

register('Michael','123456')
register('Jack','123456')

def login(username,password):
    if username in db.keys():
        if(db[username]==get_md5(password+username+'the-Salt')):
            print('Hello %s , welcome back again!' % username)
        else:
            print('You have entered a wrong password for user %s' % username)
    else:
        print('Don\'t have username %s registered ' % username)


if __name__=='__main__':
    login('Michael','123456')
    login('Jack','23456')








































