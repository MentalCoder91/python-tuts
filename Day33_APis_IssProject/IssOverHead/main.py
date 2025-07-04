import requests
from datetime import datetime
import smtplib

MY_LONG = 176.3378 # Your latitude
MY_LAT = 44.4268  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
print(iss_latitude)
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_longitude)

# Your position is within +5 or -5 degrees of the ISS position.

def is_over_head():
    if (MY_LAT-10) < iss_latitude < (MY_LAT+10) and (MY_LONG-10) < iss_longitude < (MY_LONG+10):
        print('Is overhead')
        return True
    else:
        print('Not overhead')
        return False


def send_email():
    my_email = "anish.alwekar@gmail.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="ylugbhuqgbneqoox")
        connection.sendmail(from_addr=my_email, to_addrs="alwekaranish22@gmail.com",
                            msg=f"Subject:Look Up ISS Overhead")

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour
print(time_now)


if is_over_head():
    if sunset <= time_now < sunrise:
        print('Sending Mail')
        send_email()
    else:
        print('Wait ')


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
