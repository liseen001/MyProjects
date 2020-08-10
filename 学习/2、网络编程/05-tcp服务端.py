#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import socket

#创建socket连接
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('192.168.20.155',9090))

#  1000 120  ==》 20排队
#  1000 1130  ==》128排队  剩下的两个则会连接失败
s.listen(128)  #把socket变成一个被动监听的socket  128表示排队长度


# (<socket.socket fd=752, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.20.155', 9090),
# raddr=('192.168.20.155', 55873)>, ('192.168.20.155', 55873))

# x=s.accept()   #接收客户端的请求,接收到的结果是一个元组，第0个元素是客户端的socket连接，第1个元素是客户端的ip和端口号
# print(x)
client_socket,client_addr = s.accept()

#udp里接收数据，使用的recvfrom
data=client_socket.recv(1024)  #tcp使用recv获取数据，1024：每次读服务器网卡1024个字节的数据
# print(data)

print('接收到了{}客户端{}端口号发送的数据,内容是:{}'.format(client_addr[0],client_addr[1],data.decode('utf8')))