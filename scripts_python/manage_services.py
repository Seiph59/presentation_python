#!/bin/python3

""" A REFACTORER """

import subprocess
import os
import time
import sys

def manage_services(command):
    subprocess.call("clear")
    if command.lower() == "start" or command.lower() == "stop":
        print("You asked to %s services\n" % command)

        # //////////////////////
        # Manage Apache2 Service
        # //////////////////////

        subprocess.check_call(["systemctl", command , "apache2"])
        subprocess.call(["systemctl", "status", "apache2"])

        # /////////////////////
        # Manage Tomcat Service
        # /////////////////////

        print("\n\n\n------------Tomcat ----------")
        os.chdir("/opt/tomcat/apache-tomcat-8.5.51/bin")
        p = os.getcwd()
        if command.lower() == "start":
            subprocess.call(p + "/startup.sh")
            print("Tomcat is started")
        elif command.lower() == "stop":
            subprocess.call(p + "/shutdown.sh")
            print("Tomcat is stopped")

        # ////////////////////
        # Manage PostgreSQL
        # ///////////////////

        print("\n\n\n----------PostgreSQL---------")
        subprocess.check_call(["systemctl", command , "postgresql"])
        subprocess.call(["systemctl", "status", "postgresql"])

    else:
        raise ValueError("Arguments can only be either 'start' or 'stop'")

manage_services(sys.argv[1])
