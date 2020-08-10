#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import socket

#创建一个基于udp 的网络socket连接
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


# 绑定端口号和ip地址
s.bind(('192.168.20.155',9090))    #元组


# recvfrom 接收数据
# content = s.recvfrom(1024)
# print(content)

#接收到的数据是一个元祖，元组里面有两个元素
# 第 0 个元素是接收到的数据，第 1 个元素是发送方的 ip 地址和端口号

data ,addr = s.recvfrom( 1024 )  #recvfrom是一个阻塞的方法，等待
print('从{}地址{}端口号接收到了消息，内容是：{}'.format(addr[0],addr[1],data.decode('utf8')))

#  关闭socket链接
s.close()