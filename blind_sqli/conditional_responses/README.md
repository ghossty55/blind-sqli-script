# Blind SQLi Password Extractor

## What does it do?
Two Python scripts that extract passwords through Blind SQL Injection attacks. Both execute two SQL queries automatically:

1. **Loop 1** — Determines the password length using `LENGTH()`
2. **Loop 2** — Extracts each character of the password one by one using `SUBSTRING()` or `SUBSTR()`

---

## Scripts

### conditional_responses/blind_sqli.py
- **Database:** PostgreSQL
- **Detection method:** Checks for `Welcome back!` in the server response
- **Lab:** Blind SQL injection with conditional responses

### conditional_errors/blind_sqli_with_status_code_500.py
- **Database:** Oracle
- **Detection method:** Checks for HTTP status code `500`
- **Payload structure:** Uses `||` concatenation and `CASE WHEN` with `TO_CHAR(1/0)`
- **Lab:** Blind SQL injection with conditional errors

---

## Requirements
- Python 3
- `requests` library → `pip3 install requests`
- Burp Suite to capture cookie values
- Vulnerable point: `TrackingId` cookie

## Required inputs
| Field | Description |
|---|---|
| URL TARGET | Base URL of the target site |
| TrackingId | Value of the TrackingId cookie |
| Session Cookie | Value of the session cookie |
| Users table name | Name of the users table |
| Username target | User whose password you want to extract |
| Column password | Name of the column storing the password |

## Usage
```bash
python3 blind_sqli.py
# or
python3 blind_sqli_with_status_code_500.py
```
Enter the requested data when prompted by the script.

## Context
Developed as part of web pentesting learning by practicing on PortSwigger Web Security Academy.
