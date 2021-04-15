from selenium import webdriver
import time
chrome_drive_path = "C:/Users/megaw/Desktop/Dev/chromedriver_win32/chromedriver.exe"
twitter_url = "https://twitter.com/"
NUMBER = "765079023"
PASSWORD = "iwannabethebest472"
class Twitter:
    def __init__(self, message):
        self.message = message
        self.driver = webdriver.Chrome(executable_path=chrome_drive_path)
        self.driver.get(twitter_url)


    def connextion(self, xpath):
        button = self.driver.find_element_by_xpath(xpath)
        button.click()

    def enter_credential(self, email_xpath, pwd_xpath, button_xpath):
        email = self.driver.find_element_by_xpath(email_xpath)
        email.send_keys(NUMBER)
        password = self.driver.find_element_by_xpath(pwd_xpath)
        password.send_keys(PASSWORD)
        button = self.driver.find_element_by_xpath(button_xpath)
        time.sleep(3)
        button.click()

    def tweet(self, xpath, message):
        make_tweet = self.driver.find_element_by_xpath(xpath)
        make_tweet.send_keys(message)