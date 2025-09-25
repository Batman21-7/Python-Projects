import time
import requests
import datetime as dt
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
key1 = "YD8AB1ZCFXSXNLHP"
key2 = "69532eb4ad3f4748ac08cb437ddea467"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(
    url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={key1}")
response.raise_for_status()
data = response.json()

date = dt.date.today()
today = float(data["Time Series (Daily)"][str(date)]["4. close"])

date = dt.date.fromtimestamp(time.time()-86400)
yesterday = float(data["Time Series (Daily)"][str(date)]["4. close"])

change = round(((today-yesterday)/yesterday * 100), 2)
if True:    # abs(change) >= 5:

    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    r = requests.get(
        url=f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&"
            f"from={str(date)}&sortBy=popularity&pageSize=3&language=en&apiKey={key2}")
    r.raise_for_status()
    data = r.json()

    for i in data["articles"]:
        print(f"{COMPANY_NAME}: {change}%")
        print(f"Headline:{i["title"]}\nBrief:{i["description"]}")

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

