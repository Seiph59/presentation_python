#!/bin/python3

""" A REFACTORER """

import psutil
from datetime import datetime
# import smtplib, ssl

def check_process():

    compteur = 0
    for proc in psutil.process_iter(['name']):
        if proc.info.get("name") == 'apache2':
            compteur +=1

    if compteur == 0:
        time = datetime.now().strftime("%d-%m-%Y %H:%M")
        print(time + " Apache2 isn't working")
        send_email()


def send_email():

    port = 465
    password = input("Enter your password")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("my@gmail.com", password)
        sender_email = "my@gmail.com"
        receiver_email = "your@gmail.com"
        message = " Apache2 Service is not working "
        server.sendmail(sender_email, receiver_email, message)


check_process()
