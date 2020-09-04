#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import pytest
class TestDemo01():
    def testadd(self,module):
        print('开始执行 TestDemo01类 testadd方法')
        assert 10+10 == 20
if __name__ == '__main__':
    pytest.main(['-s'])