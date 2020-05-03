import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.select import Select

class Base:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.timeout = 20
        self.poll_frequency = 0.5

    def findElement(self, locator=("by", "value")):
        if not isinstance(locator, tuple):
            print("locator参数类型错误，必须传元组类型：loc=('id',''value)")
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s" % (locator[0], locator[1]))
            element = WebDriverWait(self.driver, self.timeout, self.poll_frequency) \
                .until(lambda x: x.find_element(*locator))
            return element

    def findElements(self, locator=("by", "value")):
        elements = WebDriverWait(self.driver, self.timeout, self.poll_frequency) \
            .until(lambda x: x.find_elements(*locator))
        return elements

    def sendKeys(self, locator, text):
        element = self.findElement(locator)
        element.send_keys(text)

    def click(self, locator):
        element = self.findElement(locator)
        element.click()

    def clear(self, locator):
        element = self.findElement(locator)
        element.clear()

    def isSelected(self, locator):
        element = self.findElement(locator)
        r = element.is_selected()
        return r

    def isExisted(self, locator):
        try:
            element = self.findElement(locator).text
            return element
        except EC.NoSuchElementException as e:
            raise e
            # return False

    def isExistElement(self, locator):
        elements = self.findElements(locator)
        if len(elements) == 0:
            return False
        else:
            return True

    def is_text_in_element(self, locator, text):
        try:
            element_text = self.findElement(locator).text
            # print(element_text)
            if element_text == text:
                return True
        except Exception as e:
            raise e

    def get_text(self, locator):
        return self.findElement(locator).text

    def is_alert(self):
        """判断alert是不是在"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def move_to_element(self, locator):
        """
        鼠标悬停操作
        Usage:
        locator = ("id", "xxx")
        driver.move_to_element(\locator)
        :param locator:
        :return:
        """
        try:
            element = self.findElement(locator)
        except TimeoutException:
            print("element not found")
        else:
            AC(self.driver).move_to_element(element).perform()

    def select_by_index(self, locator, index=0):
        """
        通过索引，index是索引第几个，从0开始，默认选第一个
        :param locator:
        :param index:
        :return:
        """
        element = self.findElement(locator)
        Select(element).select_by_index(index)
        element.click()

    def select_by_value(self, locator, value):
        """通过value属性"""
        element = self.findElement(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        """通过文本值定位"""
        element = self.findElement(locator)
        Select(element).select_by_visible_text(text)

    def js_scroll_end(self):
        """滚到底部"""
        js_heig = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js_heig)

    def js_focus(self, locator):
        """聚焦元素"""
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        """回到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/zentao/user-login.html")
    r = Base(driver)
    # loc_1 = (By.ID, "account")
    # loc_2 = (By.NAME, "password")
    # loc_3 = (By.ID, "submit")

    loc_1 = ("id", "account")
    # loc_2 = ("name", "password")
    # loc_3 = ("id", "submit")
    #
    r.sendKeys(loc_1, "admin")
# r.sendKeys(loc_2, "123456")
# r.click(loc_3)
