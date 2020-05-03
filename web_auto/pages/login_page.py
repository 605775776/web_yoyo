import time

from common.base import Base
from selenium import webdriver

login_url = "http://127.0.0.1/zentao/user-login.html"


class LoginPage(Base):
    # 定位登录
    loc_username = ("id", "account")
    loc_password = ("name", "password")
    loc_keep_login = ("id", "keepLoginon")
    loc_login_button = ("id", "submit")
    loc_forget_password = ("link text", "忘记密码")
    loc_get_username = ("xpath", "//*[@id='userMenu']/a")
    # loc_forget_password_text = ("link text", "普通用户请联系管理员重置密码")
    loc_forget_password_text = ("xpath", "/html/body/div/div/div[2]/div/h5[1]")

    def input_username(self, text=""):
        self.sendKeys(self.loc_username, text)

    def input_password(self, text=""):
        self.sendKeys(self.loc_password, text)

    def click_keep_login(self):
        self.click(self.loc_keep_login)

    def click_login_button(self):
        self.click(self.loc_login_button)

    def click_forget_password(self):
        self.click(self.loc_forget_password)

    def login(self, user="admin", passwd="123456", keep_login=False):
        '''登录流程'''
        self.driver.get(login_url)
        # self.sendKeys(self.loc_username, user)
        # self.sendKeys(self.loc_password, passwd)
        self.input_username(user)
        self.input_password(passwd)
        if keep_login:
            self.click(self.loc_keep_login)
        self.click(self.loc_login_button)

    def get_login_username(self):
        try:
            username = self.get_text(self.loc_get_username)
            return username
        except:
            return ""

    # def get_login_result(self, username):
    #     result = self.is_text_in_element(self.loc_get_username, username)
    #     return result
        # t = self.driver.find_element(locator).text
        # t = self.driver.find_element_by_xpath("//*[@id='userMenu']/a").text

    def is_alert_exist(self):
        a = self.is_alert()
        if a:
            print(a.text)
            a.accept()


    def is_forget_password_exist(self):
        text = self.isExisted(self.loc_forget_password_text)
        return text

    # def get_title(self):
    #     self.driver.title
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     a = ZenTaoLogin(driver)
#     a.login(keep_login=True)

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get(login_url)
#     login_page = LoginPage(driver)
#     login_page.input_username("admin")
#     login_page.input_password("123456")
#     login_page.click_keep_login()
#     login_page.click_login_button()

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get(login_url)
#     login_page = LoginPage(driver)
#     login_page.click_forget_password()
#     result = login_page.is_forget_password_exist()
#     print(result)
if __name__ == '__main__':
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.login()
