import smtplib
import datetime as dt
import random

def send_motivation(quote):
    my_email = "megawone735@gmail.com"
    to_send = "m.wone472@yahoo.com"
    password = "775596731"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_send,
                            msg=f"Subject:Hello Boss Motivation\n\n{quote}")



# now = dt.datetime.now()
# print(now.day)



now = dt.datetime.now()
sunday = now.weekday()

if sunday == 6:
    with open("quotes.txt", "r") as quote:
        data = quote.readlines()
        random_quote = random.choice(data)
        # print(random_quote)
        send_motivation(random_quote)