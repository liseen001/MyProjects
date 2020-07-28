#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  os模块封装了常见的文件和目录操作
'''
1、os.mkdir:创建目录；2、os.rmdir: 删除目录；3、os,rename：重命令； 4、os.remove:删除文件；5、os.getcwd  获取当前工作路径
6、os.walk：遍历目录；7、os.path.join：链接目录与文件名；8、os.path.split：分隔文件名与目录；9、os.path.abspath：获取绝对路径
10、os.path.dirname：获取路径；11、os.path.basename：获取文件名或文件夹名；12、os.path.splitext：分离文件名与扩展名
13、os.path.isfile：判断给出的路径是否是一个文件；14、os.path.isdir：判断给出的路径是否是一个目录
'''
import os
print(os.path.abspath('os模块.py'))  #获取当前.py文件的绝对路径
print(os.path.abspath('..'))         #获取当前目录的绝对路径
print(os.path.abspath('.'))          #获取上级目录的绝对路径

