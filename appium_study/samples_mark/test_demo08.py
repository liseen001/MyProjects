#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import pytest
import shutil
import allure

@allure.epic('电商项目v1.0')
@allure.feature('登录模块')
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

@allure.epic('电商项目v1.0')
@allure.feature('商品模块')
class TestDemo08():
    @allure.story('正错误的登录名和密码')   #测试用例
    @allure.title('case01 使用admin\\123456登录系统')  #用例步骤描述
    def test_add05(self):
        print('====test_add05====')
        assert True
    @allure.story('正确的登录名和密码')
    @allure.title('case02 使用admin\\456789登录系统')
    def test_add06(self):
        print('====test_add06====')
        assert True

if __name__ == '__main__':
    allure_xml_report_path = os.path.join(os.path.dirname(__file__)+'/allure_xml_report')
    report_html_path = os.path.dirname(__file__)+'/allure_html_report'
    if os.path.isdir(allure_xml_report_path):
        shutil.rmtree(allure_xml_report_path)
    os.mkdir(allure_xml_report_path)
    pytest.main(['-s','-v','--alluredir=%s'%allure_xml_report_path])
    os.system('allure generate %s -o %s --clean'%(allure_xml_report_path,report_html_path))   #执行命令行