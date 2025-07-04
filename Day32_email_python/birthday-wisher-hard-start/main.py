##################### Hard Starting Project ######################
import random
import smtplib
import datetime as dt
import os
import pandas as pd
# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

def list_files_in_directory(path):
    """Lists all files and directories in a given path."""
    try:
        files = os.listdir(path)
        return files
    except FileNotFoundError:
        return f"Directory not found: {path}"
    except Exception as e:
        return f"An error occurred: {e}"



def send_email(quote, to_email):
    my_email = "anish.alwekar@gmail.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="ylugbhuqgbneqoox")
        connection.sendmail(from_addr=my_email, to_addrs=to_email,
                            msg=f"Subject:Happy Birthday \n\n {quote}")

def read_birthday_file_birthday_today():

    df = pd.read_csv('birthdays.csv', sep=',')
    today = dt.datetime.now()

    for idx,row in df.iterrows():
        if row['month'] == today.month and row['day'] == today.day:
            return row.to_dict()


def get_random_letter():
    files = list_files_in_directory('letter_templates')
    print(files)
    return random.choice(files)

#print(list_files_in_directory('letter_templates'))
birthday_data = read_birthday_file_birthday_today()
if birthday_data:
    file = get_random_letter()
    print(type(file))
    try:
        with open(f'letter_templates/{file}', 'r') as file_data:
            message = file_data.read()
            message_to_send = message.replace('[NAME]', birthday_data['name'])
        send_email(message_to_send, birthday_data['email'])

    except Exception as e:
        print(e)





