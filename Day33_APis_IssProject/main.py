import random
import smtplib
import datetime as dt
import requests
import json

response = requests.get("http://api.open-notify.org/iss-now.json")

resp = response.json()

resp_pos = response.json()['iss_position']

print(resp_pos)
status = response.status_code


print(status)
print(resp)
print(type(resp))