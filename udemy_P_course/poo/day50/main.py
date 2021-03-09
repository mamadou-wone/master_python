from selenium import webdriver

chrome_driver_path = "C:/Users/megaw/Desktop/Dev/chromedriver_win32/chromedriver.exe"
URL = "https://tinder.com/fr-CA"
NUMERO = "765079023"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)

