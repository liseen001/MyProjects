#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  faker模块
# faker模块为python的第三方模块，主要用来创伪数据
#无需再手动生成或者手写随机数来生成数据，
#pip install faker
from faker import  Faker

f = Faker(locale='zh_CN')  #为生成数据的文化选项，默认为en_US，只有使用了相关文化，侧能生成对应的随机信息

for i in range(5):
    print(f.name() + ":" + f.address())   #随机生成中文姓名和地址


# print(f.lexify())
# print('test' + f.user_name())
# print(f.text())