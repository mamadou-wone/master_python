from selenium import webdriver
import time

chrome_driver_path = "C:/Users/megaw/Desktop/Dev/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url='https://orteil.dashnet.org/experiments/cookie/')

store = driver.find_elements_by_css_selector("#store b")

# for i in store:
#     print(i.text.strip().split(" ")[-1].replace(',', ''))


time.sleep(5)
cookie = driver.find_element_by_id("cookie")
start = True

ofer_table = []
number = None
max = None

while start:
    store = driver.find_elements_by_css_selector("#store b")
    money = driver.find_element_by_id("money").text
    cookie.click()
    for i in store:
        number = i.text.strip().split(" ")[-1].replace(',', '')
        if number != '':
            ofer_table.append(number)
    for i in range(len(ofer_table) - 1):
        if int(money) > int(ofer_table[i]):
            store[i].click()
            start = False
    if int(money) > 105:
        start = False
    ofer_table = []
    time.sleep(0.001)
print(max)
# print(ofer_table)
# for i in ofer_table:
#     print(int(i))
# print(max(ofer_table))