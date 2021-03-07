from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "C:/Users/megaw/Desktop/Dev/chromedriver_win32/chromedriver.exe"
URL = "https://en.wikipedia.org/wiki/Main_Page"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=URL)

articles = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')

# articles.click()

all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name(name="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


# driver.quit()
