# --*utf-8*--
import os
import time
import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObject.common.config_utils import conf
from PageObject.common.browser import Browser


current_path=os.path.dirname(__file__)
firefox_path=os.path.join(current_path,'../webdriver/geckodriver')



driver=webdriver.Firefox(executable_path=firefox_path)
driver.get(conf.get_zend_path())

driver.maximize_window()
driver.find_element(By.XPATH,'//input[@name="account"]').send_keys(conf.get_username())
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys(conf.get_password())
driver.find_element(By.XPATH,'//button[@id="submit"]').click()
time.sleep(conf.time_out)
driver.find_element(By.XPATH,'//li[@data-id="product"]').click()
time.sleep(conf.time_out)
driver.find_element(By.XPATH,'//div/a[@href="/zentao6/www/product-create.html"]').click()

driver.find_element(By.XPATH,'//input[@id="name"]').send_keys('1231')

driver.find_element(By.XPATH,'//input[@id="code"]').send_keys('9527')

driver.find_element(By.XPATH,'//div[@id="line_chosen"]').click()
driver.find_element(By.XPATH,'//li[@title="产品线01"and @data-option-array-index="1"]').click()

driver.find_element(By.XPATH,'//div[@id="PO_chosen"]').click()
driver.find_element(By.XPATH,'//li[@title="A:admin" and @data-option-array-index="1"]').click()

driver.find_element(By.XPATH,'//div[@id="QD_chosen"]').click()
driver.find_element(By.XPATH,'//li[@title="L:测试" and @data-option-array-index="1"]').click()

driver.find_element(By.XPATH,'//div[@id="RD_chosen"]').click()
time.sleep(conf.time_out)
driver.find_element(By.XPATH,'/html/body/main/div/div/div/form/table/tbody/tr[6]/td[1]/div/div/ul/li[2]').click()