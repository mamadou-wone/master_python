import requests
from bs4 import BeautifulSoup
import lxml
from smtplib import SMTP

INITIAL_PRICE = 2184.92


def get_reduction(current_price):
    if current_price <= INITIAL_PRICE - (INITIAL_PRICE * 0.1):
        return True
    return False


URL = "https://www.amazon.com/Apple-MacBook-16-Inch-512GB-Storage/dp/B081FZV45H/ref=sr_1_4?crid=2QS3AW4UAG71Z&dchild=1&keywords=macbook+pro&qid=1615114409&sprefix=mac%2Caps%2C1472&sr=8-4"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6"
}

response = requests.get(url=URL, headers=header)
page_content = response.text

soup = BeautifulSoup(page_content, "lxml")
# print(soup)

item_price = soup.find(id="priceblock_ourprice").get_text().split('$')[1].split(',')
price = ""
for item in item_price:
    price += item

price = float(price)

if get_reduction(price):
    message = f"Hello Boss vous avez une reduction de -10% sur le Macbook Pro..Allez vite l'acheter :) sur \n {URL}"
    my_email = "megawone735@gmail.com"
    to_send = "mamadouwone12345@gmail.com"
    password = ""
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_send,
                            msg=f"Subject:Reduction sur le macBook pro\n\n{message}")
else:
    print("Aucune réduction")
