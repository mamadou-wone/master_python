morse_code = {
    "A": "▄  ▄▄▄",
    "B": "▄▄▄  ▄  ▄  ▄",
    "C": "▄▄▄  ▄  ▄▄▄  ▄",
    "D": "▄▄▄  ▄  ▄",
    "E": "▄",
    "F": "▄  ▄  ▄▄▄  ▄",
    "G": "▄▄▄  ▄▄▄  ▄",
    "H": "▄  ▄  ▄  ▄",
    "I": "▄  ▄",
    "J": "▄  ▄▄▄  ▄▄▄  ▄▄▄",
    "K": "▄▄▄  ▄  ▄▄▄",
    "L": "▄  ▄▄▄  ▄  ▄",
    "M": "▄▄▄  ▄▄▄",
    "N": "▄▄▄  ▄",
    "O": "▄▄▄  ▄▄▄  ▄▄▄",
    "P": "▄  ▄▄▄  ▄▄▄  ▄",
    "Q": "▄▄▄  ▄▄▄  ▄  ▄▄▄",
    "R": "▄  ▄▄▄  ▄",
    "S": "▄  ▄  ▄",
    "T": "▄▄▄",
    "U": "▄  ▄  ▄▄▄",
    "V": "▄  ▄  ▄  ▄▄▄",
    "W": "▄  ▄▄▄  ▄▄▄",
    "X": "▄▄▄  ▄  ▄  ▄▄▄",
    "Y": "▄▄▄  ▄  ▄▄▄  ▄▄▄",
    "Z": "▄▄▄  ▄▄▄  ▄  ▄"

}

# code = {}
#
# test = ["a", "b", "c"]
#
# for i in range(len(test)):
#     code[test[i]] = i
#
# print(code)
from selenium import webdriver
import time
import pandas

# URL = "https://fr.wikipedia.org/wiki/Code_Morse_international"
URL = 'https://www.electronics-notes.com/articles/ham_radio/morse_code/characters-table-chart.php'
path = "/home/mamadou/BOSS/webdriver/chromedriver"

driver = webdriver.Chrome(executable_path=path)

driver.get(URL)


time.sleep(5)
content = driver.find_elements_by_xpath('//*[@id="primary"]/article/table/tbody')
table_list = []
for item in content:
    table_list = item.find_elements_by_tag_name('td')

count = 2
letters_dict = {}
key = ""
value = ""
for td in range(len(table_list) - 6):
    try:
        key = table_list[td].find_element_by_xpath('//*[@id="primary"]/article/table/tbody/tr['+f"{count}"+']/td[2]').text
        value = table_list[td].find_element_by_xpath(
            '//*[@id="primary"]/article/table/tbody/tr[' + f"{count}" + ']/td[3]').text
        letters_dict[key] = value

        key = table_list[td].find_element_by_xpath(
            '//*[@id="primary"]/article/table/tbody/tr[' + f"{count}" + ']/td[5]').text
        value = table_list[td].find_element_by_xpath(
            '//*[@id="primary"]/article/table/tbody/tr[' + f"{count}" + ']/td[6]').text
        letters_dict[key] = value
        count += 1
    except:
        count += 1



# print(letters_dict)

elements = [key for key in letters_dict]
code = [letters_dict[key] for key in letters_dict]

myFile = pandas.Series(code, elements)
myFile.to_csv("code.csv")




