import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/LEGO-Ultimate-Millennium-Falcon-Building/dp/B075SDMMMV/ref=sr_1_1'

TARGET_PRICE = 500

MY_EMAIL = "pythontest217@gmail.com"
MY_PASSWORD = "wnrryyxnrgyokzke"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

r = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
whole = soup.select(selector="span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay "
                             ".a-price-whole")[0].getText()
fraction = soup.select(selector="span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay "
                                ".a-price-fraction")[0].getText()
current_price = float(f"{whole}{fraction}")

if current_price <= TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="legoarahan@gmail.com",
            msg=f"Subject:Amazon Auto Price Checker\n\nPrice of product is below target price {TARGET_PRICE}, "
                f"buy at this url:{URL}"
        )
