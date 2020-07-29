#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
'''
一、什么是网络编程中的socket
socket中文名为 '套接字'，socket表示一个网络连接，通过这个连接，使得主机间或者一台计算机上的进程间可以通讯，
不管是不同主机还是同一主机，既然是通信，必定有一个发送放一个接收方，对应一个客户端和一个服务端
'''

'''
二、创建socket 客户端
'''
import socket
import threading

#1、创建 socket，建立连接 指定IPV4协议(AF_INET)，IPV6协议使用(AF_INET6)，指定使用TCP协议(SOCK_STREAM)，UDP协议使用SOCK_DGRAM
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#2、建立连接，参数是一个tuple，tuple里指定服务器地址(域名或者IP) 和端口号
sock.connect(('www.sina.com.cn',80))

#3、发送数据，注意这里str格式一定要遵循HTTP协议标准，结尾一定要用 \r\n\r\n
sock.send("GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\n\r\n".encode('utf-8'))

#4、接收数据
buffer = []
while True:
    #每次最多接收1k字节
    d = sock.recv(1024)
    if d:
        #python3接收到为bytes类型，要转为str
        buffer.append(str(d))
    else:
        break
data = ''.join(buffer)

#二、创建socket 服务端
#1、串讲socket
import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2、绑定ip和port 注意以元组的格式传入，可以是某网卡的公网ip，或0.0.0，或127.0.0.1
sock.bind(('127.0.0.1',9999))
#3、监听端口  指定等待连接的最大数量
sock.listen(5)
#4、接收数据
while True:
    #接收一个新连接，阻塞的，只有接收到新连接才会往下走
    sock, addr = sock.accept()
    #每一个连接，都要创建新县城，否则一次只能处理一个连接
    t=threading.Thread(target=sock,args=(sock,addr))
    t.start()
