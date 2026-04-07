#Blind SQLi Password extractor 

## What does it do?
Python script that extracs password through a Blind SQL Injection attack using conditional responses. It automatically executes two SQL queries:

1. **loop 1** determines the password length using 'LENGTH()'
2. **loop 2** extracts each character of the password one by one using 'SUBSTRING()' 

The script infers results based on whether the server response contains the text 'Welcome back!'.


##Requirements 
.python3
.'request' library --> pip3 install request 
.Vulnerable point: 'TrackingId' cookie
.Burp Suite to capture cookie values


##Required inputs 
.URL TARGET --> Base URL of the target site.
.TrackingID -->Value of the trackingid cookie.
.Session Cookie --> Value of the session cookie.
.Users table name --> Name of the users table.
.Username target --> User whose password you want to extract.
.Column password --> Name of column storing the password.


##Usage
-->Bash<--
Python3  blind_sqli.py

Enter the requested data when promped by the script.

##Context
Developed as part of web pentesting learning by practicing on PortSwigger Web Security Academy --> Lab: Blind SQL injection with conditional responses.
