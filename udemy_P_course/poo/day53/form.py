from selenium import webdriver
import time

chrome_driver_path = "C:/Users/megaw/Desktop/Dev/chromedriver_win32/chromedriver.exe"
form_ink = "https://docs.google.com/forms/d/e/1FAIpQLSeQmaOiPCoYziGj9ewdQLE03LmbOFizumPP1tInQe0kQFlDYA/viewform?usp=sf_link"

class Form:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get(form_ink)


    def add_location(self, location, price_per_month, url_link):
        address = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        time.sleep(2)
        address.send_keys(f"{location}")
        price.send_keys(f"{price_per_month}")
        link.send_keys(f"{url_link}")
        submit_btn = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
        submit_btn.click()

        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()