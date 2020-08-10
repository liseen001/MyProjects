#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import socket


server_soceket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_soceket.bind( ('192.168.20.155',9999) )

server_soceket.listen(128)

#接收客户端的请求
client_socket,client_addr = server_soceket.accept()




data = client_socket.recv(1224).decode('utf8')

# print('接收到了来自{}地址{}端口的数据，内容是：{}'.format( client_addr[0],client_addr[1],data ))

if os.path.isfile(data):
    print('读取文件，返回给客户端')
    with open(data,'rb') as file:
        content = file.read()
        client_socket.send( content )  #返回给客户端需要下载的文件
else:
    print('文件不存在')