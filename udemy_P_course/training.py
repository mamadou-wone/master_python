#  ___       __   ________  ________   _______      
# |\  \     |\  \|\   __  \|\   ___  \|\  ___ \     
# \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \   __/|    
#  \ \  \  __\ \  \ \  \\\  \ \  \\ \  \ \  \_|/__  
#   \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ \  \_|\ \ 
#    \ \____________\ \_______\ \__\\ \__\ \_______\
#     \|____________|\|_______|\|__| \|__|\|_______|

# def format_name(firstName, lastName):
#     first = ''
#     name = ''
#     completeName  = ''
#     for i in range(1 , len(firstName)):
#         first += firstName[i].lower()
#     first = firstName[0].upper()+first
    
#     for i in range(1 ,len(lastName)):
#         name += lastName[i].lower()
#     name = lastName[0].upper()+name
#     completeName = first + ' ' + name
        
#     return completeName    
    
    

# test=  format_name("MAMAdou", "wONE")
# print(test)

# def is_leap(year):
#   leap =  False
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         leap = True
#       else:
#         leap = False
#     else:
#      leap = True
#   else:
#     leap = False
#   return leap  

# def days_in_month(year , month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#   days = 0 
#   if is_leap(year) and month == 2:
#     #   month_days[1] = 29
#     #   month_days = month_days[month]
#     days = 29
#   else:
#       days = month_days[month - 1]
#   return days        
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))