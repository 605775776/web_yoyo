from common.base import Base
from selenium import webdriver
from pages.login_page import LoginPage
import time


class AddBugPage(Base):
    # 添加bug
    loc_test = ("link text", "测试")
    loc_bug = ("link text", "Bug")
    loc_add_bug = ("xpath", "//*[@id='createActionMenu']/a")
    loc_truck = ("xpath", "//*[@id='openedBuild_chosen']/ul")
    loc_truck_add = ("xpath", "//*[@id='openedBuild_chosen']/div/ul/li")
    loc_input_title = ("id", "title")

    # 切换iframe
    loc_input_body = ("class name", "article-content")
    loc_save_button = ("xpath", "//*[@id='submit']")
    loc_save_button = ("id", "submit")
    loc_new = ("xpath", ".//*[@id='bugList']/tbody/tr[1]/td[4]/a")

    def add_bug(self, title="测试提交bug", text="body"):
        self.click(self.loc_test)
        time.sleep(2)
        self.click(self.loc_bug)
        self.click(self.loc_add_bug)
        self.click(self.loc_truck)
        self.click(self.loc_truck_add)

        self.sendKeys(self.loc_input_title, title)
        # 切换iframe
        self.driver.switch_to.frame(0)
        self.clear(self.loc_input_body)
        self.sendKeys(self.loc_input_body, text)
        # 回到主页面上
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.click(self.loc_save_button)
        # 新增的列表

    def is_add_bug_success(self, _text):
        # print(self.findElement(self.loc_new).text)
        # print(_text)
        return self.is_text_in_element(self.loc_new, _text)

# //*
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    bug = AddBugPage(driver)
    a = LoginPage(driver)
    a.login()
    timestr = time.strftime("%Y-%m-%d-%H-%m-%S")
    title = "测试提交bug"+timestr
    bug.add_bug(title, "正文")
    result = bug.is_add_bug_success(title)
    print(result)
