import random
import smtplib
import datetime as dt

def send_email(quote):
    my_email = "anish.alwekar@gmail.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="ylugbhuqgbneqoox")
        connection.sendmail(from_addr=my_email, to_addrs="alwekaranish22@gmail.com",
                            msg=f"Subject:Motivation \n\n {quote}")

def get_random_quote():

    with open("quotes.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        return random.choice(lines)


time = dt.datetime.now()
week_day  = time.weekday()
if week_day == 5:
    send_email(get_random_quote())

##################
# time = dt.datetime.now()
# year = time.year
# month = time.month
# print(month)
# print(year)
# print(type(year))
#
# print(time)
#
# birth = dt.datetime(year=2004, month=12, day=2)
# print(birth)
