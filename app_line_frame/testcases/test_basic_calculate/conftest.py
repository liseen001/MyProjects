#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:配置内层conftest
import  pytest
import time
from appium import webdriver

driver = None
'''启动APP'''
@pytest.fixture()
def start_app(driver_setting):
    global  driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',driver_setting)
    return driver

'''关闭APP'''
@pytest.fixture()
def close_app():
    yield driver
    time.sleep(2)
    driver.close_app()
