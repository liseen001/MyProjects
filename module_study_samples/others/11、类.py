#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:类
'''
类指的是具有相同属性和方法的一组对象的集合，而实例则是一个具体的对象
'''

class Animal(object):
    def __init__(self,name):  #创建实例的时候，可以传入一些参数，以初始化对象的属性，需要加一个__init__方法
        self.name=name  #创建实例   特殊方法/构造方法

    def greet(self):
        print('Hello,I am %s.'%self.name)   #自定义方法


'''
使用type(obj) 来获取去对象的响应类型；使用isinstance(obj,type)判断对象是否为指定的type类型的实例
'''
dog1=Animal('dog1')
print(dog1.greet())
print(type(dog1))
print(isinstance(dog1,Animal))