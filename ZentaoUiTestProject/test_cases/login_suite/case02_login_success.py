# --*utf-8*--
import unittest
from selenium.webdriver.common.by import By
from common import set_driver,login,loginout


class LoginSucess(unittest.TestCase):
    def setUp(self):
        self.driver = set_driver.set_driver()

    def test02_login(self):
        '''这是一个测试登陆成功的用例'''
        login.login(self.driver,'admin','p1666666,')
        actually_result =self.driver.find_element(By.XPATH,'//span[@class="user-name"]').text
        self.assertEqual(actually_result,'admin','test02_login用例执行失败')


    def tearDown(self):
        loginout.loginout(self.driver)


if __name__ == "__main__":
    unittest.main()
