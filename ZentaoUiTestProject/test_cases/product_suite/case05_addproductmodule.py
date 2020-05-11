# -*- coding utf-8 -*-
import unittest,time
from selenium.webdriver.common.by import By
from common import login,loginout,set_driver
class AddProductModul(unittest.TestCase):
    '''增加产品模块类'''
    @classmethod
    def setUpClass(cls):
        cls.driver = set_driver.set_driver()
        login.login(cls.driver,'admin','P1666666,')


    def test07_addpruductmodule(self):
        self.driver.find_element(By.XPATH,'//li[@data-id="product"]/a[@href="/zentao6/www/product-index-no.html"]').click()  #点击首页产品
        self.driver.find_element(By.XPATH,'//a[@href="/zentao6/www/product-browse-2.html"]').click()  #点击六组第一个产品
        self.driver.find_element(By.XPATH,'//div/a[@href="/zentao6/www/tree-browse-2-story.html"]').click() #点击维护模块
        self.driver.find_element(By.XPATH,'//div[@id="sonModule"]/div/div/input[@nid="modules[]"]').send_keys('第一个模块')
        self.driver.find_element(By.XPATH,'//input[@id="shorts[]"]').send_keys('第一个简称')



    @classmethod
    def tearDownClass(cls):
        loginout.loginout(cls.driver)

if __name__=="__main__":
    unittest.main()

