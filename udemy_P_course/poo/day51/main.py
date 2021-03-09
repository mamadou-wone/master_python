from selenium import webdriver
import time
from twitter import Twitter

PROMISED_DOWN = 2

speed_test_url = "https://www.speedtest.net/"
chrome_drive_path = "C:/Users/megaw/Desktop/Dev/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.get(speed_test_url)
time.sleep(10)

start = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
start.click()

time.sleep(60)
download = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
upload = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

message = "Hey @sonatel vos débit sont tellement mauvais: " \
          f"vous avez promi down:{PROMISED_DOWN} et la je n'ai " \
          f"que down:{download} up:{upload}"

time.sleep(2)

twitter = Twitter(message)
time.sleep(5)
twitter.connextion('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div')


email_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
passwd_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
btn_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span'
time.sleep(10)
twitter.enter_credential(email_xpath, passwd_xpath, btn_xpath)

tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/span'
time.sleep(5)
twitter.tweet(tweet_xpath, message)