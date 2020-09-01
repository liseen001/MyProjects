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
    'appPackage':'com.youdao.calculator',
    'appActivity':'com.youdao.calculator.activities.MainActivity',
    'noReset':True,
    'unicodeKeyboard':True,  #这个和下面的选项一起写，支持中文
    'resetKeyboard': True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)
driver.find_element_by_xpath('//android.widget.FrameLayout[@bounds="[714,1423][895,1579]"]').click()
time.sleep(1)
driver.find_element_by_xpath('//android.widget.ImageView[@bounds="[787,1474][822,1527]"]').click()
time.sleep(0.5)
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout[9]/android.widget.FrameLayout/android.widget.ImageView').click()
time.sleep(0.5)
driver.find_element_by_xpath('//android.widget.FrameLayout[@bounds="[898,1741][1079,1897]"]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//android.widget.FrameLayout[@bounds="[530,1423][711,1579]"]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//android.widget.FrameLayout[@bounds="[898,1900][1079,2056]"]').click()