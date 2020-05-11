# --*utf-8*--
import time
import unittest
from selenium.webdriver.common.by import By
from common import login,set_driver,loginout

class HomePageClick(unittest.TestCase):
    def setUp(self):
        self.driver = set_driver.set_driver()

    def test03_homepageclick(self):
        '''这是点击首页的用例'''
        login.login(self.driver,'admin','p1666666,')
        self.driver.find_element(By.XPATH,'//a[text()="首页"]').click()
        result = self.driver.title
        self.assertEqual(result,'我的地盘 - 禅道','test03_homepageclick用例执行失败')

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__=="__main__":
    unittest.main()