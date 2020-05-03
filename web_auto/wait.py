from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(url="http://127.0.0.1/zentao/user-login.html")


def findElement(driver, locator=("by", "value"), timeout=10, poll_frequency=0.5):
    element = WebDriverWait(driver, timeout, poll_frequency).until(lambda x: x.find_element(*locator))
    return element


# driver.find_element(By.ID, "account").send_keys("admin")
# driver.find_element(By.NAME, "password").send_keys("123456")
# loc_1 = (By.ID, "account")
# loc_2 = (By.NAME, "password")
# loc_3 = (By.ID, "submit")
#
# findElement(driver, loc_1).send_keys("admin")
# findElement(driver, loc_2).send_keys("123456")
#
# findElement(driver, loc_3).click()
