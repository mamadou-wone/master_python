from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:/Users/megaw/Desktop\Dev/chromedriver_win32/chromedriver.exe"
USERNAME = "765079023"
PASSWORD = "hacklife472"
BOSS = "mamad0u_w0ne"


class Instagram:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get(url)

    def connection(self, phone_xpath, psw_xpath, btn_xpath):
        phone = self.driver.find_element_by_xpath(phone_xpath)
        phone.send_keys(USERNAME)
        password = self.driver.find_element_by_xpath(psw_xpath)
        password.send_keys(PASSWORD)
        time.sleep(3)
        button = self.driver.find_element_by_xpath(btn_xpath)
        button.click()

    def search_user(self, xpath, b_xpath):
        search_bar = self.driver.find_element_by_xpath(xpath)
        search_bar.send_keys(BOSS)
        time.sleep(2)
        boss = self.driver.find_element_by_xpath(b_xpath)
        boss.click()

    def follow_users(self, s_xpath):
        suscribers = self.driver.find_element_by_xpath(s_xpath)
        suscribers.click()
        time.sleep(5)
        # container = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        # container.send_keys(Keys.PAGE_UP)
        suscribers_list = self.driver.find_elements_by_css_selector(".PZuss div div button")
        print(suscribers_list)
        print(len(suscribers_list))
        for i in suscribers_list:
            i.click()
