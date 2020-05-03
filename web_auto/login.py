import time

class Login(object):
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element_by_id("account").send_keys(username)
        time.sleep(2)
        self.driver.find_element_by_name("password").send_keys(password)
        time.sleep(2)
        self.driver.find_element_by_id("submit").click()
        time.sleep(2)

    def get_login_username(self):
        try:
            t = self.driver.find_element_by_xpath("//*[@id='userMenu']/a").text
            return t
        except:
            return ''

    def is_alert_exist(self):
        try:
            time.sleep(2)
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
        except:
            return ''
