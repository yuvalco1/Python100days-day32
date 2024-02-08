# First section is what we learned in class
# import random
# import smtplib
# import datetime as dt
#
# my_email = "yuvalco1@gmail.com"
# google_email_password = 'dfnaeuvkfbrjxztx'
# quotes=[]
#
# with open('quotes.txt') as quotes_file:
#     quotes=quotes_file.readlines()
#
# quote = random.choice(quotes)
# print(quote)
#
# now = dt.datetime.now()
# today_day = now.weekday()
# print(today_day)
# # year=now.year # there are many more methods to get month, day, etc...
# # print(now)
# #
# # date_of_birth = dt.date(year=1990, month=12, day=12)
#
# if today_day == 3:
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=google_email_password)
#         connection.sendmail(from_addr=my_email, to_addrs="yuvalco@yahoo.com", msg=f"Subject:Hello\n\n{quote}")
#         print("Email sent")
##################################### End of first section #######################################################
import random
import smtplib

import pandas
import datetime as dt

#####  Day 32 Project
##################### Hard Starting Project ######################

my_email = "yuvalco1@gmail.com"
google_email_password = 'dfnaeuvkfbrjxztx'
birthdays_dict = {}
today_day = dt.datetime.now().day
today_month = dt.datetime.now().month

try:
    data = pandas.read_csv("birthdays.csv")
except FileNotFoundError:
    print("File not found")
else:
    birthdays_dict = data.to_dict(orient="records")

for name in birthdays_dict:
    if name['month'] == today_month and name['day'] == today_day:
        print(name)
        random_number = random.randint(1, 3)
        print(random_number)
        random_letter = open(f"letter_templates/letter_{random_number}.txt").read()
        random_letter = random_letter.replace("[NAME]", name['name'])
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=google_email_password)
            connection.sendmail(from_addr=my_email, to_addrs=name['email'], msg=f"Subject:Happy Birthday\n\n{random_letter}")
            print("Email sent")





