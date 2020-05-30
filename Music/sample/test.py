#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:调试代码
from  selenium import webdriver
import time
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import conf


driver = webdriver.Firefox(executable_path='../webdriver/geckodriver')
driver.get(conf.music_url)
time.sleep(1)
driver.set_window_size(450,900)
driver.find_element(By.XPATH,'//input[@placeholder="用户名"]').send_keys('liseen001')
driver.find_element(By.XPATH,'//input[@placeholder="密码"]').send_keys('000000')
driver.find_element(By.XPATH,'//div[@class="login-btn"]').click()
driver.find_element(By.XPATH,'//a[@href="#/register"]').click()
