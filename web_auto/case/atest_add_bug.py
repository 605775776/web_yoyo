# coding:utf-8
import time
import unittest
from selenium import webdriver

from pages.add_bug_page import ZenTaoBug


class TestAddBug(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.bug = ZenTaoBug(cls.driver)
        cls.bug.login()

    def setUp(self):
        pass


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_add_bug(self):
        timestr = time.strftime("%Y-%m-%d-%H-%m-%S")
        title = "测试提交bug1" + timestr
        self.bug.add_bug(title, "正文")
        result = self.bug.is_add_bug_success(title)
        print(title)
        # print(self.bug.findElement(self.bug.loc_new).text)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
