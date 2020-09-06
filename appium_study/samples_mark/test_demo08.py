#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import pytest
import allure

@allure.story('这是一个测试类')
class TestDemo07():
    @pytest.mark.skip(reason='开发未完善，阻碍测试')
    def test_add01(self):
        print('====test_add01====')
        assert True
    def test_add02(self):
        print('====test_add02====')
        assert True
    def test_add03(self):
        if True:
            pytest.skip('无条件跳过')  #3、用例中实现跳过，可以传入msg参数说明跳过原因，也可以判断是否跳过，写在if判断里面或者try expect
        print('====test_add03====')
        assert True

    def test_add04(self):
        print('====test_add04====')
        assert True

class TestDemo08():
    def test_add05(self):
        print('====test_add05====')
        assert True

    def test_add06(self):
        print('====test_add06====')
        assert True

if __name__ == '__main__':
    allure_xml_report_path = os.path.join(os.path.dirname(__file__)+'/allure_xml_report')
    report_html_path = os.path.dirname(__file__)+'/allure_html_report'
    print(allure_xml_report_path)
    print(report_html_path)
    pytest.main(['-s','-v','--alluredir=%s'%allure_xml_report_path])
    os.system('allure generate %s -o %s'%(allure_xml_report_path,report_html_path))   #执行命令行