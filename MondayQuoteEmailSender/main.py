import smtplib
import datetime as dt
import random

# Constants
MY_EMAIL = "pythontest217@gmail.com"
MY_PASSWORD = "wnrryyxnrgyokzke"

# Get quotes from txt file
with open("quotes.txt", "r") as quotes:
    quotes_list = quotes.readlines()

# Check if it is a monday
now = dt.datetime.now()
if now.weekday() == 1:

    # Send quote as an email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivational Quote\n\n{random.choice(quotes_list)}"
        )
