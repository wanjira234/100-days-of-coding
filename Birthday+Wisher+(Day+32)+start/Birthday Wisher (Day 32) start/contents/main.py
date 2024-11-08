import smtplib
import getpass
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
try:
    if weekday == 0:
        with open(file="Birthday Wisher (Day 32) start/contents/quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            quote = random.choice(all_quotes)
        print(quote)
except Exception as e:
    print(f"an error occured{e}")
else:
    HOST = "smtp.office365.com"
    PORT = 587
    FROM_EMAIL = "kyra342@outlook.com"
    TO_EMAIL = "theelitecoder7@gmail.com"
    # password = "fyhz kxbi bxxk myoj"
    PASSWORD = getpass.getpass("enter password: ")
    MESSAGE = f"""Subject: hello\n\n
    
    
    {quote}

    test Account """

    smtp = smtplib.SMTP(HOST, PORT)
    status_code, response = smtp.ehlo()
    print(f"[*]Echoing the server: {status_code}{response}")

    status_code, response = smtp.starttls()
    print(f"[*]starting TLS connection: {status_code}{response}")

    status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"[*]logging in: {status_code}{response}")

    smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
    smtp.quit()
    print(f"FROM_EMAIL: {FROM_EMAIL}")
    print(f"TO_EMAIL: {TO_EMAIL}")
    print(f"MESSAGE: {MESSAGE}")
    
# pycharm version
# MY_EMAIL = "kyra342@outlook.com"
# MY_PASSWORD = "eppy@kiruri"

# now = dt.datetime.now()
# weekday = now.weekday()

# if weekday == 1:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#     print(quote)
#     with smtplib.SMTP("smtp-email.outlook.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs="teelitecoder7@gmail.com",
#             msg=f"Subject: Motivation\n\n {quote}")
        
