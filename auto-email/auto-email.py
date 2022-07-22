#!/usr/bin/env python3
from info import username,password
import smtplib

def send_one():
    text = input("Enter e-mail text: ")
    service = smtplib.SMTP("smtp.gmail.com", 587)
    service.ehlo()
    service.starttls()
    service.login(username,password)
    sender_email = input("From: ")
    to = input("to: ")
    subject = input("Subject: ")

    try:
        service.sendmail(sender_email,to,text.encode("utf-8"),subject)
        print("Send!")
    except Exception as Err:
        print("Try again. Error:", Err)

def send_multi():
    text = input("Enter e-mail text: ")
    service = smtplib.SMTP("smtp.gmail.com", 587)
    service.ehlo()
    service.starttls()
    service.login(username,password)
    sender_email = input("From: ")
    receivers = []
    while True:
        to = input("To('E' for exit) :")
        if to == "E":
            break
        else:
            receivers.append(to)
    subject = input("Subject: ")

    try:
        service.sendmail(sender_email,receivers,text.encode("utf-8"),subject)
        print("Send!")
    except Exception as Err:
        print("Try again. Error:", Err)

if __name__ == "__main__":
    choice = input("1-Send to one receiver\n2-Send to multi receiver")
    if choice == "1":
        send_one()
    elif choice == "2":
        send_multi()
    else:
        print("Try again.")