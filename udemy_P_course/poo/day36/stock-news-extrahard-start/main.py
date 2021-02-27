import requests
from datetime import datetime, date,timedelta
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

apiKey = "PRWJLHWS4DTSJ20G"
apiurl = "https://www.alphavantage.co/query"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": apiKey

}

responses = requests.get(apiurl, params=parameter)
responses.raise_for_status()
data = responses.json()


today = date.today()
yesterday = today + timedelta(days=-1)
the_day_before = today + timedelta(days=-2)

def stock_evolution(y_stock, db_stock):
    evolution = 0
    percentage = 0
    evolution = y_stock - db_stock
    if evolution > 0:
        percentage = round((evolution / y_stock) * 100, 2)
    else:
        percentage = round((evolution / db_stock) * 100, 2)
    return percentage


yesterday_stock = float(data["Time Series (Daily)"][f"{yesterday}"]["4. close"])
the_day_before_stock = float(data["Time Series (Daily)"][f"{the_day_before}"]["4. close"])



evolution = stock_evolution(yesterday_stock, the_day_before_stock)
fluctuation = None



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_new():
    global today
    global the_day_before_stock
    apiUrl = "https://newsapi.org/v2/everything"
    apiKey = "0aa58ebc8e6a499cb547ccb406936f6b"
    parameter = {
        "q": "Tesla",
        "from": f"{today}",
        "to": f"{the_day_before_stock}",
        "sortBy": "popularity",
        "apiKey": apiKey
    }

    responses = requests.get(apiUrl, params=parameter)
    data = responses.json()

    return data


from twilio.rest import Client

def send_email(news):
    account_sid = "AC82ead7df95ea1627a6f24457535575dc"
    auth_token = "602da8a444a0a9379afdca96a4e25911"
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=news,
        from_='+14159675282',
        to='+221774724175'
    )
    print(message.status)

news = get_new()["articles"][:2]

text_me = False

if evolution < -5:
    fluctuation = f"TSLA: 🔻{evolution}%"
    text_me = True
elif evolution > 5:
    fluctuation = f"TSLA: 🔺{evolution}%"
    text_me = True
else:
    text_me = False

if text_me:
    my_news = ""
    for new in news:
        my_news += f"{fluctuation}% \nHeadline: {new['title']} \n Brief {new['description']}"
    send_email(my_news)
else:
    print("nooooo")
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this:

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

