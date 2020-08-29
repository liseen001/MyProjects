#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import selenium
from appium import webdriver
des ={
    'platformName':'Android',  #系统
    'platformVersion': '9.0',  #版本号
    'deviceName': 'vivo 1725',      #设备名称：型号  可随便填
    'udid':'dfa4d640', #设备号
    'appPackage':'com.youdao.calculator',
    'appActivity':'com.youdao.calculator.activities.MainActivity',
    'noReset':True,
    'unicodeKeyboard':True,  #这个和下面的选项一起写，支持中文
    'resetKeyboard': True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)


