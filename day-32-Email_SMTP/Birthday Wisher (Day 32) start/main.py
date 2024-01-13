# import smtplib
#
# my_email = "dev.mail.testforsend@gmail.com"
# password = "okudfibpgqsfdjri"
# receive_email = "hduy01012000@gmail.com"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # smtp.gmail.com is protocol that you need to follow in order to use that email to send_mail
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=receive_email,
#                         msg="Subject:Hello\n\nThis is the body")
#

# import datetime as dt
#
# # now = dt.datetime.now()
# # print(now.year)
# # if now.year == 2022:
# #     print(now)
# # else:
# #     print("noop")
#
# date_of_birth = dt.datetime(year=2000, month=1, day=1)
# print(date_of_birth)


import datetime as dt
import smtplib
import json
import random
# This will create json file to store data
# week_of_days = {
#     "Monday": 0,
#     "Tuesday": 1,
#     "Wednesday": 2,
#     "Thursday": 3,
#     "Friday": 4,
#     "Saturday": 5,
#     "Sunday": 6
# }
# with open("day_of_week.json","w") as output_file:
#     json.dump(week_of_days,output_file , indent=4)

# read and store data into 2 variables
week_of_day = {}
content = ""
with open("day_of_week.json","r") as data:
    week_of_day = json.load(data)

with open("quotes.txt","r") as quotes_data:
    content = random.choice(quotes_data.readlines())

# print(content)
# print(week_of_day)

now = dt.datetime.now()
day_of_week = week_of_day[str(now.weekday())]
# print(day_of_week)

my_email = "dev.mail.testforsend@gmail.com"
password = "okudfibpgqsfdjri"
receive_email = "hduy01012000@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    # smtp.gmail.com is protocol that you need to follow in order to use that email to send_mail
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=receive_email,
                        msg=f"Subject:{day_of_week}\n\n{content}")


