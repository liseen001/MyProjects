#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo_03.py
# @time: 2020/9/1 21:53
# @desc:
import time
import selenium
from appium import webdriver
des ={
    'platformName':'Android',  #系统
    'platformVersion': '9.0',  #版本号
    'deviceName': 'vivo 1725',      #设备名称：型号  可随便填
    'udid':'192.168.127.102:5555', #设备号
    'browserName':'chrome',
    'appPackage':'com.aweproject',
    'appActivity':'com.aweproject.MainActivity',
    'noReset':True,
    'unicodeKeyboard':True,  #这个和下面的选项一起写，支持中文
    'resetKeyboard': True,
    # 'chromedriverExcutetable':''
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)
driver.get('https://www.baidu.com')