#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:加法
import pytest
from appium import webdriver
import allure

@allure.story('计算器的加法测试')
@allure.title('加法测试，修改测试用例名称')
def test_add_case01(start_app):
    # driver = webdriver.Remote
    driver=start_app
    driver.find_element_by_xpath('')

@allure.story('计算器的加法测试')
@allure.title('加法测试，修改测试用例名称')
def test_add_case02(start_app):
    driver = start_app
    driver.find_element_by_xpath('')
