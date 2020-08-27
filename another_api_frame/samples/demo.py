#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import time,random,ast
from samples.faker_demo import faker
# a = {'one':1,'two':2,'three':3}
# print( a )
# a.setdefault('four',4)
# print( a )
# for i in range(10):
#     # print(random.uniform(1,4))
#     data =float('%.1f'%(random.uniform(0,5)))
#     print(float('%.1f'%(random.uniform(0,5))))
#     time.sleep( data )
dict = {'name':'faker.create_random_name','card_num':'faker.create_randon_ssn','age':'faker.create_random_int'}
print(type(dict))
for k,v in dict.items():
    v = eval(v)
    dict.update({k:v})



print(dict)

