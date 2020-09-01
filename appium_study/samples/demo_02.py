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

driver =webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)  #打开包
time.sleep(2)
driver.find_element_by_xpath('//android.widget.TextView[@bounds="[15,886][525,951]"]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//android.widget.EditText[@bounds="[287,791][824,908]" and @text="请输入用户名"]').send_keys('liseen009')
time.sleep(0.5)
driver.find_element_by_xpath('//android.widget.EditText[@bounds="[287,941][824,1058]" and @text="请输入密码"]').send_keys('a000000')
time.sleep(0.5)
driver.find_element_by_xpath('//android.widget.TextView[@text="立即登录"and @bounds="[444,1177][636,1242]"]').click()
time.sleep(5)
# driver.find_element_by_xpath('//android.widget.TextView[@text="天下滙视讯" and @bounds="[578,1267][1035,1324]"]').click()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[7]').click()
