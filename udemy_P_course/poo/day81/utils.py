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

URL = "https://fr.wikipedia.org/wiki/Code_Morse_international"

path = "/home/mamadou/BOSS/webdriver/chromedriver"

driver = webdriver.Chrome(executable_path=path)

driver.get(URL)


time.sleep(5)
content = driver.find_elements_by_xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody')
# letters = [item for item in content]

letters = []
for item in content:
    letters = item.find_elements_by_tag_name('a')

letter = [let.text for let in letters if len(let.text) == 1]
print(letter)
print(letter[:3])