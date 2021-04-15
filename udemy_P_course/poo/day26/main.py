# numbers = [1, 2, 3]
# new_list = [n * 2 for n in numbers]
# print(new_list)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# list1 = list(range(1, 5))
# range_list = [num * 2 for num in range(1, 5)]
# list2 = [n * 2 for n in list1]
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# uper_name = [name.upper() for name in names if len(name) >= 5]
#
# print(list2)


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
#
# squared_numbers = [number ** 2 for number in numbers]
#
# #Write your code 👆 above:
#
# print(squared_numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# #Write your 1 line code 👇 below:
# result = [even_num for even_num in numbers if even_num % 2 == 0]
#
#
# #Write your code 👆 above:
#
# print(result)

#
# with open("file1.txt") as file1:
#     num1 = [int(num) for num in list(file1.read().splitlines())]
#
# print(num1)
# with open("file2.txt") as file2:
#     num2 = [int(num) for num in list(file2.read().splitlines())]
#
# print(num2)
#
# result = [num for num in num1 if num in num2]
# print(result)

# import random
# #
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
#
# student_score = {student: random.randint(1, 100) for student in names}
# #print(student_score)
# passed_student = {student:score for (student, score) in student_score.items() if score >= 60}
# print(passed_student)
# passed_student = {student:score for (student, score) in student_score.items() if student_score >= 60}
# passed_student = {student:student_score[student] for student in student_score if student_score[student] > 60}

# words = ["What", "is", "the", "Airspeed",
#          "Velocity", "of", "Unladen",
#          "Swallow?"]
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# result = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
# print(result)


















