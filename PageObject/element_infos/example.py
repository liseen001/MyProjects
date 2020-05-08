# -*- coding utf-8 -*-
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObject.common.config_utils import conf
from PageObject.common.browser import browser
from PageObject.common.base_page import BasePage

cureent_parh=os.path.dirname(__file__)
fox_path=os.path.join(cureent_parh,'../webdriver/geckodriver')

driver=webdriver.Firefox(executable_path=fox_path)
driver.get(conf.zend_path)
driver.maximize_window()
driver.find_element(By.XPATH,'//input[@name="account"]').send_keys('admin')
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('P1666666,')
driver.find_element(By.XPATH,'//button[@id="submit"]').click()

driver.find_element(By.XPATH,'//li[@data-id="my"]')
driver.find_element(By.XPATH,'//li/a[@href="/zentao6/www/my/"]').click()