import pandas
import random
import smtplib
import datetime as dt
##################### Extra Hard Starting Project ######################

DEFAULT_NAME = "[NAME]"

# 1. Update the birthdays.csv
#DONE
# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv")
mum = data.name[0]
email = data.email[0]
year = int(data.year[0])
month = int(data.month[0])
day = int(data.day[0])

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
lettre_num = random.randint(1, 3)
with open(f"letter_templates/letter_{lettre_num}.txt", ) as letter:
    letter_content = letter.read()
    new_letter = letter_content.replace(DEFAULT_NAME, mum)
# 4. Send the letter generated in step 3 to that person's email address.

now = dt.datetime.now()
if day == now.day and year == now.year and month == now.month:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="megawone735@gmail.com", password="775596731")
        connection.sendmail(from_addr="megawone735@gmail.com", to_addrs=email,
                            msg=f"Subject:Happy Birthday\n\n{new_letter}"
                            )
else:
    print("error")

