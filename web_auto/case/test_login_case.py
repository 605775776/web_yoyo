from selenium import webdriver
import unittest
from pages.login_page import LoginPage, login_url


class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.loginpage = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url)
        self.loginpage.is_alert_exist()
        self.driver.delete_all_cookies()  # 退出登录
        self.driver.refresh()

    def test_01(self):
        """输入用户名admin，输入密码123456，点击登录"""
        self.loginpage.input_username("admin")
        self.loginpage.input_password("123456")
        self.loginpage.click_login_button()
        result = self.loginpage.get_login_username()
        # print(result)
        self.assertTrue(result == "admin")
        # 断言

    def test_02(self):
        """输入用户名admin，不输入密码，点击登录"""
        self.loginpage.input_username("admin")
        # self.loginpage.input_password("")
        self.loginpage.click_login_button()
        result = self.loginpage.get_login_username()
        print(result)
        self.assertTrue(result == "")

    def test_03(self):
        """输入用户名admin，输入密码123456，点击记住按钮,点击登录"""
        self.loginpage.input_username("admin")
        self.loginpage.input_password("123456")
        self.loginpage.click_keep_login()
        self.loginpage.click_login_button()
        result = self.loginpage.get_login_username()
        print(result)
        self.assertTrue(result == "admin")
        # 断言

    def test_04(self):
        """忘记密码"""
        self.loginpage.click_forget_password()
        result = self.loginpage.is_forget_password_exist()
        # print(result)
        self.assertTrue(result == "普通用户请联系管理员重置密码")
        # 断言

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
