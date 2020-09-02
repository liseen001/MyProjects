#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import time
import selenium
from appium import webdriver
des ={
    'platformName':'Android',  #系统
    'platformVersion': '9.0',  #版本号
    'deviceName': 'vivo 1725',      #设备名称：型号  可随便填
    'udid':'dfa4d640', #设备号
    'appPackage':'com.aweproject',
    'appActivity':'com.aweproject.MainActivity',
    'noReset':True,
    'unicodeKeyboard':True,  #这个和下面的选项一起写，支持中文
    'resetKeyboard': True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)
driver.implicitly_wait(20)
driver.find_element_by_xpath('//android.widget.ImageView[@bounds="[933,2005][1011,2075]"]').click()
time.sleep(1)
driver.find_element_by_xpath('//android.widget.EditText[@text="请输入用户名" and @bounds="[287,791][824,908]"]').send_keys('larry002')
time.sleep(1)
driver.find_element_by_xpath('//android.widget.EditText[@text="请输入密码" and @bounds="[287,941][824,1058]"]').send_keys('larry1')
time.sleep(1)
driver.find_element_by_xpath('//android.widget.TextView[@text="立即登录" and @bounds="[444,1177][636,1242]"]').click()
