#  ___       __   ________  ________   _______      
# |\  \     |\  \|\   __  \|\   ___  \|\  ___ \     
# \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \   __/|    
#  \ \  \  __\ \  \ \  \\\  \ \  \\ \  \ \  \_|/__  
#   \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ \  \_|\ \ 
#    \ \____________\ \_______\ \__\\ \__\ \_______\
#     \|____________|\|_______|\|__| \|__|\|_______|

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     if student_scores[key] <= 70:
#         student_grades[key] = "Fail"
#     elif student_scores[key] > 70 and student_scores[key] <= 80:
#         student_grades[key] = "Acceptable"
#     elif student_scores[key] > 80 and student_scores[key] <=90:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] > 900 and student_scores[key] <=100:
#          student_grades[key] = "Outstanding"
# # 🚨 Don't change the code below 👇
# print(student_grades)

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country , visits, cities = []):
#     travel_log.append(
#        { "country": country,
#         "visits": visits,
#         "cities": cities}
#     )




# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

# print(travel_log)

from art_hagman import massu

print(massu)

enchere = []
def add_bidders(name, bid):
    enchere.append(
        {
            "name": name,
            "bid": bid
        }
    )

continu = ''
    
while continu != 'no':
    name = input("What is your name ? ")
    bid = int(input("What is your bid ? $"))
    confirm = input("Are there any other bidders? Type 'yes' or 'no'\n")
    continu = confirm
    add_bidders(name , bid)

# print(enchere)
maximun = 0
winner = ''
for key in enchere:
    if key['bid'] > maximun:
        maximun = key['bid']
        winner = key['name']
        
print(f"The winner is {winner} with a bid of ${maximun}")    
    

    
    

