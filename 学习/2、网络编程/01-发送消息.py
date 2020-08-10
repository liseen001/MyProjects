#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  不同电脑之间通信需要使用socket，还可以在同一个电脑中的不同程序之间通信

import socket
#1、创建并且连接socket
# AF_INET:表示socket是用来进行网络连接
# SOCKET_DGRAM: 表示连接基于UDP的连接
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   #找到socket模块中的socket()类，创建一个对象

#绑定端口，与发送放的端口不一致，先绑定再接收或发送数据
s.bind(('192.168.20.155',9000))

#2、发送数据
# 给 192.168.20.155 这台主机的9000的端口发送hello，输入发送放的IP地址
# 端口号：0-65536   0-1024的端口 不要用，系统重要的服务在使用，端口号是空闲的
#data：要发送的数据，它时二进制的数据  address:发送给谁(),参数是一个元组,元组里有两个元素，第0个表示目标的IP地址，第一个表示程序的端口号
s.sendto('liseen'.encode('utf8'),('192.168.20.155',9999))


#接收数据

data,addr = s.recvfrom( 1024 )
print('接收到了{}地址{}端口消息，内容是：{}'.format( addr[0],addr[1],data.decode('utf8') ))

#3、关闭socket
s.close()