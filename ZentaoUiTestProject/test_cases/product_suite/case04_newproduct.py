# -*- coding utf-8 -*-
import unittest,time
from selenium.webdriver.common.by import By
from common import set_driver,login,loginout,addproduct
class NewProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver =set_driver.set_driver()
        login.login(cls.driver,'admin','P1666666,')

    def test04_click_product(self):
        '''这是点击禅道首页产品按钮的用例'''
        self.driver.find_element(By.XPATH,'//li[@data-id="product"]/a[@href="/zentao6/www/product-index-no.html"]').click()
        result=self.driver.title
        self.assertEqual(result,'产品主页 - 禅道','test04_click_product运行失败')
        time.sleep(2)


    def test05_click_newproduct(self):
        '''这是一个点击添加产品按钮的用例'''
        self.driver.find_element(By.XPATH, '//div[@class="btn-toolbar"]/a[@href="/zentao6/www/product-create.html"]').click()
        result=self.driver.find_element(By.XPATH,'//span[@class="user-name"]').text
        self.assertEqual(result,'admin','test05_click_newproduct运行失败')


    def test06_addproduct(self):
        '''这是一个添加产品的用例，添加产品的最后步骤'''
        addproduct.add_product(self.driver)
        result = self.driver.find_element(By.XPATH, '//span[@class="user-name"]').text
        self.assertEqual(result, 'admin', 'test06_addproduct运行失败')



    @classmethod
    def tearDownClass(cls):
        loginout.loginout(cls.driver)


if __name__=="__main__":
    unittest.main()

