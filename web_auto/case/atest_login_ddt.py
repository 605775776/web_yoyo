from selenium import webdriver
import unittest
from pages.login_page import LoginPage, login_url
from ddt import ddt, data
from common.read_excel import ExcelUtil
from common.dir_config import test_data_dir
# test_data = [{"username": "admin", "password": "123456", "expected": "admin"},
#              {"username": "admin", "password": "", "expected": False},
#              {"username": "admin1", "password": "123456", "expected": False}, ]
filepath = test_data_dir
test_data = ExcelUtil(filepath)


@ddt
class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.loginpage = LoginPage(cls.driver)
        cls.driver.get(login_url)

    def setUp(self):
        self.loginpage.is_alert_exist()
        self.driver.delete_all_cookies()  # 退出登录
        self.driver.refresh()
        self.driver.get(login_url)

    def login_case(self, username, password, expected):
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_login_button()
        result = self.loginpage.get_login_username()
        self.assertTrue(result == expected)

    @data(*(test_data.dict_data()))
    def test_01(self, data):
        # data = test_data[0]
        # print(data)
        self.login_case(data["username"], data["password"], data["expected"])

    # def test_01(self):
    #     """输入用户名admin，输入密码123456，点击登录"""
    #     self.loginpage.input_username("admin")
    #     self.loginpage.input_password("123456")
    #     self.loginpage.click_login_button()
    #     result = self.loginpage.get_login_username()
    #     print(result)
    #     self.assertTrue(result == "admin")
    #     # 断言

    # def test_02(self):
    #     """输入用户名admin，不输入密码，点击登录"""
    #     self.loginpage.input_username("admin")
    #     # self.loginpage.input_password("")
    #     self.loginpage.click_login_button()
    #     result = self.loginpage.get_login_username()
    #     print(result)
    #     self.assertTrue(result == "")

    # def test_03(self):
    #     """输入用户名admin1，输入密码123456，点击登录"""
    #     self.loginpage.input_username("admin1")
    #     self.loginpage.input_password("123456")
    #     self.loginpage.click_login_button()
    #     result = self.loginpage.get_login_username()
    #     print(result)
    #     self.assertTrue(result == "admin")

    # def test_03(self):
    #     """输入用户名admin，输入密码123456，点击记住按钮,点击登录"""
    #     self.loginpage.input_username("admin")
    #     self.loginpage.input_password("123456")
    #     self.loginpage.click_keep_login()
    #     self.loginpage.click_login_button()
    #     result = self.loginpage.get_login_username()
    #     print(result)
    #     self.assertTrue(result == "admin")
    #     # 断言

    # def test_04(self):
    #     """忘记密码"""
    #     self.loginpage.click_forget_password()
    #     result = self.loginpage.is_forget_password_exist()
    #     # print(result)
    #     self.assertTrue(result == "普通用户请联系管理员重置密码")
    #     # 断言

    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
