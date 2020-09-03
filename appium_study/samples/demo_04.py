#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os,time
from appium import webdriver

des = {
    'platformName':'Android',
    'platformVersion': '9.0',
    'deviceName':'vivo 1027',
    'appPackage':'com.aweproject',
    'appActivity':'com.aweproject.MainActivity',
    'noReset':True,
    'unicodeKeyboard':True,
    'resetKeyboard': True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)
driver.implicitly_wait(8)
print(driver.network_connection)  #返回网络状态，返回整型数字
driver.set_network_connection(connection_type=2)  #设置网络状态方式一 0 1 2 4 6
print( driver.network_connection )
from appium.webdriver.connectiontype import ConnectionType
driver.set_network_connection(ConnectionType.WIFI_ONLY)    #方式二设置网络状态
driver.save_screenshot('test00.png')  #截屏操作,传文件路径，图片格式为png  screenshot('1.png') 是对元素截图
print(driver.get_device_time(format='YYYY-MM-DDTHH:mm:ssZ'))  #时间格式可以不传