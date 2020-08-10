#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import socket


#  基于TCP协议的socke连接 SOCK_STREAM
s=socket.socket( socket.AF_INET,socket.SOCK_STREAM )


#udp使用  s.sendto() 发送数据
# s.sendto('hello'.encode('utf8'),('192.168.20.155',9999))

#使用tcp发送数据之前，必须要先和服务器建立连接,udp不需要
s.connect(('192.168.20.155',9090))  #调用  connect() 方法连接到服务器

# 发送数据
s.send( 'liseen'.encode('utf8') )



s.close() #关闭连接