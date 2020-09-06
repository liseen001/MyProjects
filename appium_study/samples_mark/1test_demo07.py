#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import pytest
pytestmark=pytest.mark.skip()    # 5、改方法可以跳过整个模块
# @pytest.mark.skip(reason='设置整个测试类不执行')    #4、设置整个测试类不执行
class TestDemo07():
    @pytest.mark.skip(reason='开发未完善，阻碍测试')  #1、无条件跳过
    def test_add01(self):
        print('test_add03嘿嘿')
        assert True

    @pytest.mark.skipif(condition=True,reason='条件满足，用例不执行')   #2、条件为真时跳过
    def test_add02(self):
        print('test_add04呵呵')
        assert True


    def test_sub01(self):
        if True:
            pytest.skip('无条件跳过')  #3、用例中实现跳过，可以传入msg参数说明跳过原因，也可以判断是否跳过，写在if判断里面或者try expect
        print('test_sub01哼哼')
        assert True

    def test_sub02(self):
        print('test_sub02哈哈')
        assert True

class TestDemo08():
    def test_add01(self):
        print('test_add03嘿嘿')
        assert True

    def test_add02(self):
        print('test_add04呵呵')
        assert True

if __name__ == '__main__':
    pytest.main(['-s','-v'])