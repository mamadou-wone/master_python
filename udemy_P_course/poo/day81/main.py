# from utils import morse_code
import pandas

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
test = ['A', '?', 'N', '?', 'B', '?', 'O', '?', 'C', '?', 'P', '?', 'D', '?', 'Q', '?', 'E', '?', 'R', '?', 'F', '?', 'S', '?', 'G', '?', 'T', '?', 'H', '?', 'U', '?', 'I', '?', 'V', '?', 'J', '?', 'W', '?', 'K', '?', 'X', '?', 'L', '?', 'Y', '?', 'M', '?', 'Z', '?']
# ['A', '?', 'N']

print(test[::4])

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