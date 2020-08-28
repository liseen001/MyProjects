#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import selenium
from appium import webdriver
des = {
    'platformName':'Android',  #系统
    'platformVersion': '',  #版本号
    'deviceName': 'Samsung',      #设备名称：型号  课随便填
    'udid':'adb device', #设备号
    'appPackage':'APP包名',
    'appActivity':'activity名,前面需要加点',
    'noReset':True,
    'unicodeKeyboard':True,  #这个和下面的选项一起写，支持中文
    'resetKetboard': True
}
driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub',des)