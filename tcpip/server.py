#!/usr/bin/env python3 

#-*-coding:utf-8-*-

import socket
import threading


#创建一个socket：AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接。
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 监听端口:
s.bind(('192.168.56.101', 9999))
#紧接着，调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量
s.listen(5)
print('Waiting for connection...')

def tcplink(sock,addr):
    print('Accept new connection from %s: %s...'% addr)
    sock.send(b'Welcome!')
    while True:
        data=sock.recv(4096)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s: %s closed' % addr)


while True:
     # 接受一个新连接:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start








