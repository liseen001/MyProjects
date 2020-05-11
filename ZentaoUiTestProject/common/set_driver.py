# --*utf-8*--
import os
from selenium import webdriver
def set_driver():
    current_path = os.path.dirname(__file__)
    foxfire_driver_path = os.path.join(current_path, '../webdriver/geckodriver')
    driver = webdriver.Firefox(executable_path=foxfire_driver_path)
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get('http://106.53.50.202:8999/zentao6/www/user-login-L3plbnRhbzYvd3d3L215Lmh0bWw=.html')
    return driver
