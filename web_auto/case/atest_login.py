import unittest
from selenium import webdriver
import time
from login import Login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as ac


class LoginTest(unittest.TestCase):
    """登录类的案例"""

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.zentao = Login(cls.driver)

    def setUp(self):
        url = "http://127.0.0.1/zentao/user-login.html"
        self.driver.get(url)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        """
        输入正确用户名 admin 输入正确密码 123456
        :return:
        """
        # self.login("admin", "123456")
        self.zentao.login("admin", "123456")
        t = self.zentao.get_login_username()
        # print(t)
        self.assertTrue(t == "admin")

    # self.assertTrue("admin" == self.driver.find_element_by_xpath("//*[@id='userMenu']/a").text)
    # if "admin" == driver.find_element_by_xpath("//*[@id='userMenu']/a").text:
    #     print("login success")
    # else:
    #     print("login failure")

    # 输入错误的用户名
    def test_02(self):
        """"
        输入错误用户名 admin123
        """
        self.zentao.login("admin", "123456")
        t = self.zentao.is_alert_exist()
        # print(t)
        self.assertTrue(t == "登录失败，请检查您的用户名或密码是否填写正确。")  # 断言截图
        # self.assertIn("登录失败",t)
