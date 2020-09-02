#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os, time
import selenium
from appium import webdriver
driver_path = os.path.join(os.path.dirname(__file__),'..','webdriver/chromdriver.exe')
des ={
    'platformName':'Android',  #系统
    'platformVersion': '9.0',  #版本号
    'deviceName':'vivo 1027',
    'browserName':'chrome',
    # 'appPackage':'com.google.android.googlequicksearchbox',
    # 'appActivity':'com.google.android.apps.gsa.searchnow.SearchNowActivity',
    'noReset':True,
    'unicodeKeyboard':True,  #这个和下面的选项一起写，支持中文
    'resetKeyboard': True,
    'chromedriverExcutable': 'C:\\Users\Administrator\AppData\Local\Programs\Appium\resources\app\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win\chromedriver'
}

driver =webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)  #打开包
driver.get('http://hao.uc.cn/')
time.sleep(5)
driver.find_element_by_xpath('//input[@text="输入关键字"]').click()
driver.find_element_by_xpath('//input[@text="输入关键字"]').send_keys('liseen')
time.sleep(2)
driver.find_element_by_xpath('//button[@text="搜索"]').click()