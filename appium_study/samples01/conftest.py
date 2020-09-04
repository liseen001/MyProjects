#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import pytest
@pytest.fixture(scope='module')
def module():
    print('测试开始执行')
    yield
    print('开始测试清理')