# from utils import morse_code
from pprint import pprint


import pandas

data = pandas.read_csv('code.csv')

letters_dict = data.to_dict()
code_list = {}

for i in range(len(letters_dict['Key'])):
    code_list[letters_dict['Key'][i]] = letters_dict['Value'][i]

info = input("Enter your name: ").upper()

morse_code = ""
for let in info:
    if code_list[let]:
        morse_code += code_list[let]
    else:
        print("error")

print(morse_code)

# for val in data.iterrows():
#     print(val[1]['Key']['Value'])

# for key in data['Key']:
#     print(key[0])























# letters = [key for key in morse_code]
# code = [morse_code[key] for key in morse_code]
# # print(letters)
# myFile = pandas.Series(code, letters)
# myFile.to_csv("test.csv")
# print(myFile)


# test = [i for i in range(10)]
# print(test)
# print(test[::3])
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 3, 6, 9]
# test = ['A', '?', 'N', '?', 'B', '?', 'O', '?', 'C', '?', 'P', '?', 'D', '?', 'Q', '?', 'E', '?', 'R', '?', 'F', '?', 'S', '?', 'G', '?', 'T', '?', 'H', '?', 'U', '?', 'I', '?', 'V', '?', 'J', '?', 'W', '?', 'K', '?', 'X', '?', 'L', '?', 'Y', '?', 'M', '?', 'Z', '?']
# # ['A', '?', 'N']
#
# print(test[::4])

# import csv
#
#
# my_file = csv.reader("code.csv")
#
#
#
#
# # try:
# #     file = open("morse.csv")
# #     file.close()
# # except FileNotFoundError:
# #     with open("morse.csv", "w") as file:
# #         pass
#
#
#
#
#
#
#
#
#
#
#
#
# # for key in morse_code:
# #     print(key)
#
# # word = input("Enter anything: ").upper()
# # morse_word = ""
# #
# # for letter in word:
# #     morse_word += morse_code[letter]
# #
# # print(morse_word)