from pprint import pprint
import json
from selenium import webdriver

chrome_driver_path = "C:/Users/megaw/Desktop/Dev/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="https://www.python.org/")
even_dict = {}

all_even = driver.find_element_by_xpath(xpath='//*[@id="content"]/div/section/div[3]/div[2]/div/ul')

evens = all_even.find_elements_by_tag_name("li")

for even in range(len(evens)):
    time = evens[even].find_element_by_tag_name('time').text
    name = evens[even].find_element_by_tag_name('a').text
    even_dict[even] = {
            "time": f"{time}",
            "name": f"{name}"
        }



pprint(even_dict)

# try:
#     with open("evens.json", "r") as data_file:
#         data = json.load(data_file)
#         data.update(even_dict)
# except FileNotFoundError:
#     with open("evens.json", "w") as data_file:
#         json.dump(even_dict, data_file, indent=4)
# else:
#     with open("evens.json", "w") as data_file:
#         json.dump(data, data_file, indent=4)
driver.quit()
















# driver.get("https://www.amazon.com/Apple-MacBook-16-Inch-512GB-Storage/dp/B081FZV45H/ref=sr_1_4?dchild=1&keywords=macbook+pro&qid=1615122892&sr=8-4")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))


# driver.quit()