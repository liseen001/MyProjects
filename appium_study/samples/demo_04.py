#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os,time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

des = {
    'platformName':'Android',
    'platformVersion': '9.0',
    'deviceName':'vivo 1027',
    # 'appPackage':'com.aweproject',
    # 'appActivity':'com.aweproject.MainActivity',
    'noReset':True,
    'unicodeKeyboard':True,
    'resetKeyboard': True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)
driver.implicitly_wait(8)
driver.start_activity('com.aweproject','com.aweproject.MainActivity')
driver.implicitly_wait(10)
driver.find_element_by_xpath('//android.widget.TextView[@text="登录"]').click()
driver.implicitly_wait(10)
driver.find_element_by_xpath('//android.widget.EditText[@text="请输入用户名"]').send_keys('larry002')
driver.implicitly_wait(10)
driver.find_element_by_xpath('//android.widget.EditText[@text="请输入密码"]').send_keys('larry1')
driver.implicitly_wait(10)
driver.find_element_by_xpath('//android.widget.TextView[@text="立即登录"]').click()
driver.implicitly_wait(10)
driver.find_element_by_xpath('//android.widget.ImageView[@bounds="[548,1252][1065,1545]"]').click()
time.sleep(5)
driver.implicitly_wait(10)
print(driver.contexts)
# print(driver.contexts)
time.sleep(5)
driver.back()
