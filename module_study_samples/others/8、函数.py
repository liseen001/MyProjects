#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 函数
#1、函数三部分构成：   函数名、函数参数、函数返回值
def hello(name):
    return name

#2、必选参数，就是在调用函数的时候要传入数量一致的参数，比如
def add(x,y):
    return x+y
print(add(1,2))

#3、默认参数，是指在定义函数的时候提供一些默认值，如果在调用函数的时候没有传递该参数，则使用默认值，否则使用传递时该参数的值
#默认参数需要放所有必选参数的后面，默认参数应该使用不可变对象
def sum(x,y,z=0):
    return x+y+z
print(sum(1,2))

#4、可变参数：某些情况下，我们在定义函数的时候，无法预估函数该指定多少个参数，这时可以使用可变参数，适用函数的参数个数是不确定的情况下
#  参数前面一个 *  表示是可变的，在函数内部，参数numbers接收到的是一个 tuple
def add01(*numbers):
    sum=0
    for i in numbers:
        sum +=i
    print(numbers)
    return sum

print(add01(3,4,5))

# 5、关键字参数，可变参数允许你将不定数量的参数传递给函数，而关键字参数则允许你将不定长度的键值对，作为参数传递给一个函数
# kwargs是一个关键字参数，前面两个 * 号， kwargs 是可以接受不定长度的键值对，在函数内部，它会表示成一个字典
def add02(**kwargs):
    return  kwargs
print(add02(x=1,y=2))

def sun(**kwargs):
    sum = 0
    for k,v in kwargs.items():
        sum +=v
    return  sum
print(sun())
dict1={'x':1}
print(sun(**dict1))

#6、在实际的使用中，经常会用到必选参数、默认参数、可变参数或关键字参数或其中的某些，他们的优先级顺序为 必选参数、默认参数、可变参数、关键字参数
