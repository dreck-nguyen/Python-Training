# # 1. Update the birthday.csv
#
# # 2. Check if today matches a birthday in the birthdays.csv
#
# # 3.If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# # bane from birthday.csv
#
# # 4. Send the letter generated in step 3 to that person's email address.

import datetime
import random
import smtplib

import pandas
my_email = "dev.mail.testforsend@gmail.com"
pwd = "okudfibpgqsfdjri"

now = datetime.datetime.now()
today = (now.month, now.day)
data = pandas.read_csv("birthday.csv")
birthday_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()
}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_{random.randint(1,2)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
         connection.starttls()
         connection.login(user=my_email,password=pwd)
         connection.sendmail(from_addr=my_email,
                             to_addrs=birthday_person["email"],
                             msg=f"Subject:Happy Birthday\n\n{contents}")