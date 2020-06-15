import subprocess
import smtplib

""" A REFACTORER """

threshold = 80
partition = "/"

def report_via_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        message = "Server running out of disk space"
        server.ehlo()
        server.starttls()
        server.login("damiengalasso64", "mdp4thewin")

        server.sendmail("damiengalasso64@gmail.com", "damien.galasso@outlook.fr", message)

def check_disk():
    df = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
    for line in df.stdout:
        splitline = line.decode().split()
        if splitline[5] == partition:
            if int(splitline[4] [:-1]) > threshold:
                report_via_email()

# check_disk()
report_via_email()
