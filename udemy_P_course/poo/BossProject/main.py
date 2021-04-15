from selenium import webdriver
import time

path = "/home/mamadou/BOSS/webdriver/chromedriver"

driver = webdriver.Chrome(executable_path=path)

driver.get("https://www.jumia.sn/")


time.sleep(5)
btn = driver.find_elements_by_xpath('//*[@id="pop"]/div/section/button')















# from bs4 import BeautifulSoup
# import requests
#
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
#     "Accept-Language": "en-GB,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6"
# }
#
# response = requests.get('https://www.jumia.sn/', headers=header)
# content = response.text
# soup = BeautifulSoup(content, "html.parser")
#
# print(soup)