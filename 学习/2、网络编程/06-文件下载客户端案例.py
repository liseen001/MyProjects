#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('192.168.20.155',9090))

# s.send('hello'.encode('utf8'))

file_name = input( '请输出您要下载的文件名：' )
s.send( file_name.encode('utf8') )

#每次只读1024，需要不断循环读取
with open(file_name,'wb') as file:
    while True:
        content = s.recv( 1024 )
        if not  content:
            break
        file.write(content)
s.close()