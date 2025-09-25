import pandas as pd
import datetime as dt
import smtplib
import random

MY_EMAIL = "pythontest217@gmail.com"
MY_PASSWORD = "wnrryyxnrgyokzke"

# 1. Read birthdays.csv
df = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
for index, series in df.iterrows():
    if now.day == series.loc["day"] and now.month == series.loc["month"]:
        # 3. Pick a random letter replace the [NAME] with actual one
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as template:
            letter = template.readlines()
            letter[0] = letter[0].replace("[NAME]", series["name"])
            letter.insert(4, f"Congratulations on turning {now.year - series['year']} :)\n\n")
            letter = "".join(letter)

# 4. Send the letter to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=series["email"],
                msg=f"Subject:Happy Birthday {series['name']}!\n\n{letter}"
            )
