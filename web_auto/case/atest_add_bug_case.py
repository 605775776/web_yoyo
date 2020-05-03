import unittest
from selenium import webdriver
from pages.login_page import LoginPage, login_url
from pages.add_bug_page import AddBugPage
import time

my = "http://127.0.0.1:81/zentao/my/"


class AddBugCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.bug = AddBugPage(cls.driver)
        a = LoginPage(cls.driver)
        a.login()

    def setUp(self):
        self.driver.get(my)

    def test_01(self):
        """正常提交bug"""
        timestr = time.strftime("%Y-%m-%d-%H-%m-%S")
        title = "测试提交bug" + timestr
        self.bug.add_bug(title, "正文")
        result = self.bug.is_add_bug_success(title)
        self.assertTrue(result)

    def tearDownClass(cls):
        cls.driver.quit()
