# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import os
import pandas
import random
import smtplib
import datetime as dt

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

email_closing = "Best regards,\nCorey London"
LETTERS = []
def choose_letter():
    with open("letter_templates/letter_1.txt") as file:
        letter_1 = file.read()
    with open("letter_templates/letter_2.txt") as file:
        letter_2 = file.read()
    with open("letter_templates/letter_3.txt") as file:
        letter_3 = file.read()

    LETTERS.append(letter_1)
    LETTERS.append(letter_2)
    LETTERS.append(letter_3)

    generic_letter = random.choice(LETTERS)
    letter_print = generic_letter.replace("[NAME]", recipient_name)
    print(letter_print)


    def send_letter():
        """establishes the connection to mail server, starts tls security, establishes login credentials, then sends mail.
         consider placing recipient as parameter to easily handle multiple"""
        with smtplib.SMTP("smtp.gmail.com",
                          port=587) as connection:  # connection to email server, must specify port number
            connection.starttls()  # starts email protocol to stop interception
            connection.login(user=MY_EMAIL,
                             password=MY_PASSWORD)  # login information for email, use app password instead of personal
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=recipient_email,
                                msg=f'Subject:Happy Birthday\n\n{letter_print} \n\n{email_closing}')
    send_letter()


now = dt.datetime.now()
today = (now.month, now.day)
data = pandas.read_csv("../birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
recipient_email = birthday_dict.get(today, {}).get('email')  # access a value after creating a dictionary using key names
recipient_name = birthday_dict.get(today, {}).get('name')   # access a value after creating a dictionary using key names



if today in birthday_dict:
    choose_letter()
