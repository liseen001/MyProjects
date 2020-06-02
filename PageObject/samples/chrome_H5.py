#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
#https://blog.csdn.net/WZ18810463869/article/details/81157524
# import os
# from  selenium import webdriver
# from time import sleep
#
# current_parh=os.path.dirname(__file__)
# chrome_driver_path=os.path.join(current_parh,'../webdriver/chromedriver')
#
# driver=webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get('http://cn.voidcc.com/question/p-hzmpbdbv-uu.html')
# mobileEmulation={'deviceName':'Apple iPhone X'}
# options = webdriver.ChromeOptions()
# options.add_experimental_option('mobileEmulation',mobileEmulation)
#
# driver=webdriver.Chrome(executable_path=chrome_driver_path,chrome_options=options)
#
# driver.get('http://m.baidu.com')
# sleep(3)

import os
import time
import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObject.common.config_utils import conf
from PageObject.common.browser import Browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

current_path=os.path.dirname(__file__)
firefox_path=os.path.join(current_path,'../webdriver/geckodriver')

driver=webdriver.Firefox(executable_path=firefox_path)
driver.get('http://192.168.101.2:8042')

driver.maximize_window()
driver.set_window_size(450,900)

# driver.find_element(By.XPATH,'//input[@type="checkbox"]').click()  #点击公告选择按钮
# driver.find_element(By.XPATH,'//span[text()="不再提示"]').click()   #点击不再提示按钮
# driver.find_element(By.XPATH,'//div[@routerlink="/register"]').click()  #点击注册按钮
# driver.find_element(By.XPATH,'//input[@formcontrolname="username"]').send_keys('test002')#输入用户名输入栏
# driver.find_element(By.XPATH,'//input[@formcontrolname="password"]').send_keys('a000000') #输入密码输入框
# driver.find_element(By.XPATH,'//input[@formcontrolname="mobileNo"]').send_keys('15845847885')  #输入手机号
# driver.find_element(By.XPATH,'//input[@formcontrolname="recommendCode"]').send_keys('123qwe')  #输入推荐码
# element=driver.find_element(By.XPATH,'//div[@id="slider"]')
# ActionChains(driver).click_and_hold(element).pause(1).move_to_element(driver.find_element(By.XPATH,'//div[@id="slider-btn"]'))