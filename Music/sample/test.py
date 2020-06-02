#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:调试代码
from  selenium import webdriver
import time
from selenium.webdriver.common.by import By
from Music.common.base_page import BasePage
from Music.common.browser import Browser
from Music.common.config_utils import conf


driver = webdriver.Firefox(executable_path='../webdriver/geckodriver')
driver.get(conf.music_url)
time.sleep(1)
driver.set_window_size(450,900)
driver.find_element(By.XPATH,'//input[@placeholder="用户名"]').send_keys('liseen001')
driver.find_element(By.XPATH,'//input[@placeholder="密码"]').send_keys('000000')
driver.find_element(By.XPATH,'//div[@class="login-btn"]').click()
# driver.find_element(By.XPATH,'//a[@href="#/register"]').click()

# time.sleep(5)
# driver.find_element(By.XPATH,'//i[@class="van-icon van-icon-music"]').click()
#
# time.sleep(5)
# driver.back()
# time.sleep(5)
# driver.find_element(By.XPATH,'//i[@class="van-icon van-icon-service"]').click()
#
# time.sleep(5)
# driver.back()
# time.sleep(5)
# driver.find_element(By.XPATH,'//i[@class="van-icon van-icon-comment"]').click()
#
# time.sleep(5)
# driver.back()
# time.sleep(5)
# driver.find_element(By.XPATH,'//i[@class="van-icon van-icon-search"]').click()

time.sleep(3)
value=driver.find_element(By.XPATH,'//div[@class="more"]').text
print(value)