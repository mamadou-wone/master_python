#a = input("Donner un nbre \n")
#b = input("Donner un nbre \n")

#print(int(a)+int(b))
#day_in_Decembre = 31
#print(str(day_in_Decembre)+ " day in this month")
from datetime import datetime,timedelta
current_date = datetime.now()

one_day = timedelta(days=1)
yesterday = current_date - one_day


print("today is " + str(current_date))
print("yersterday was " + str(yesterday))
