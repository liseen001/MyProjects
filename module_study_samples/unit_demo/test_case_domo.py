#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import unittest

class TestDemo(unittest.TestCase):
    def setUp(self):
        print('开始执行测试')
    def tearDown(self):
        print('结束执行测试')

    def test_add(self):
        self.assertEqual( 10+6,16,'执行失败' )
        print('test_add')
    def test_sub(self):
        self.assertEqual(10-6,4,'执行失败')
        print('test_sub')

if __name__ == '__main__':
    unittest.main()