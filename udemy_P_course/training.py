# year = int(input("Which year do you want to check "))

# if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
#     print("We have a leap year")
# else:
#     print("We dont have a leap year")    
    
boss = input("Enter you name ")
crush = input("Enter your crush name ")

boss_score = 0
crush_score = 0

total1 = 0
total2 = 0

boss_lower = boss.lower()
crush_lower = crush.lower()

boss_lower2 = boss.lower()
crush_lower2 = crush.lower()

# if boss_lower.count("t") or crush_lower.count("t") or boss_lower.count("r") or crush_lower.count("r") or boss_lower.count("v") or crush_lower.count("v") or boss_lower.count("e") or crush_lower.count("e"):
boss_score =boss_lower.count("t") + boss_lower.count("r")+ boss_lower.count("u")+boss_lower.count("e")
crush_score = crush_lower.count("t") +  crush_lower.count("r") + crush_lower.count("u")+ crush_lower.count("e")
total1 = boss_score + crush_score  



boss_score2 =boss_lower.count("l") + boss_lower.count("o")+ boss_lower.count("v")+boss_lower.count("e")
crush_score2 = crush_lower.count("l") +  crush_lower.count("o") + crush_lower.count("v")+ crush_lower.count("e")
total2 = boss_score2 + crush_score2  

print(str(total1)+str(total2))

    