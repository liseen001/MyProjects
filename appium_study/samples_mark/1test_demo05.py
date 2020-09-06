#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import pytest

@pytest.mark.smoketest
def test_add01():
    print('test_add01嘿嘿')
    assert True
@pytest.mark.smoketest
def test_add02():
    print('test_add02呵呵')
    assert True

@pytest.mark.systemtest
def test_sub01():
    print('test_sub01哼哼')
    assert True

def test_sub02():
    print('test_sub02哈哈')
    assert True

if __name__ == '__main__':
    pytest.main(['-s','-m smoketest'])