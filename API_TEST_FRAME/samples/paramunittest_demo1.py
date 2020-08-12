#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: paramunittest.demo.py
# @time: 2020/8/12 21:56
# @desc:  基本实现写法一、可以传列表、元组
'''
unittest参数化介绍
1、参数化测试相当于需要使用多组不同的测试数据测试同一个方法的时候，及用多组不同的测试数据测试登录模块
2、unittest参数化是指对一个unittest中的测试方法采用多组数据引入进行测试
3、实现unittest参数化的方式多种：ddt、paramunittest等
'''
import unittest
import paramunittest

'''
参数化数据两组  使用修饰器的方式做参数化：可以放元组(单引号)、列表、字典(键的名字必须与形参一致)
需要注意的地方
'''
@paramunittest.parametrized(
    (6,1),
    ('7','2')
)

class TestDemo1( paramunittest.ParametrizedTestCase ):
    def setParameters(self, numa, numb):  #必要的要写的方法，把参数化传递到测试数类中
        self.numa = numa
        self.numb = numb

    def test_case(self):
        print( 'a={},b={}'.format( self.numa,self.numb ))
        self.assertGreater( self.numa,self.numb ) #a大于b

if __name__ == '__main__':
    unittest.main()
