print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
percent = input("What percentage tip would you like to give? 10 , 12, or 15")
people = input("How many people to split the bill?")

slipt_by_person = float(bill )/ int(people)
total = slipt_by_person + (slipt_by_person* int(percent)/100)

print(round(total,2))
# print("Each person shoul pay: $")
