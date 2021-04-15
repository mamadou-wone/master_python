from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/megaw/Desktop/Dev/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_xpath('/html/body/form/input[1]')
first_name.send_keys("Your Boss")

last_name = driver.find_element_by_xpath('/html/body/form/input[2]')
last_name.send_keys("The best Python Dev Ever")

email = driver.find_element_by_xpath('/html/body/form/input[3]')
email.send_keys("yourboss@email.com")

button = driver.find_element_by_xpath('/html/body/form/button')
button.send_keys(Keys.ENTER)

