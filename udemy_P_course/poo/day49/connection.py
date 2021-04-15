from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Connection:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def open_browser(self, url):
        self.driver.get(url)

    def close_popup(self, xpath):
        close = self.driver.find_element_by_xpath(xpath)
        close.click()

    def search_item(self, item_name, xpath):
        search = self.driver.find_element_by_xpath(xpath)
        search.send_keys(item_name)
        search.send_keys(Keys.ENTER)

    def click_item(self, xpath):
        tws = self.driver.find_element_by_xpath(xpath)
        tws.click()

    def get_item_price(self, xpath):
        price = self.driver.find_element_by_xpath(xpath)
        return price.text