#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: unittest_demo01.py
# @time: 2020/8/12 21:50
# @desc:
import unittest
class TestDemo( unittest.TestCase ):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual( 1+2,3 )


if __name__ == '__main__':
    unittest.main()