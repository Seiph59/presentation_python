#!/bin/python3

""" A REFACTORER """

import os
import datetime
import re
import shutil

today = datetime.date.today()
week_number = today.isocalendar()[1]
day_number = today.isocalendar()[2]

def get_tomcat_logs(today, week_number):
    dirs = os.listdir('/opt/tomcat/apache-tomcat-8.5.51/logs')
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    f = open('/home/student/backup_logs/trace.log', "a")
    dest = "/home/student/backup_logs/backup_week_" + str(week_number)

    for dire in dirs:
        sel = re.findall(str(yesterday), dire)
        if sel:
            shutil.copy("/opt/tomcat/apache-tomcat-8.5.51/logs/" + dire, dest)
            print("Le fichier " + dire + " est copié")
            f.write(str(today) + '\tCOPIE' + '\t\t' + dire + '\t' + dest + '\t' + "semaine: " + str(week_number + 4) + '\t\tOK\n')
        else:
            print("Fichier non copié")
    f.close()

def get_apache_logs(week_number):
    dirs = os.listdir('/var/log/apache2')
    today = datetime.date.today().strftime("%a-%b-%d")
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    date_error_format = yesterday.strftime(" %a %b %d")
    date_access_vhost = yesterday.strftime("%d/%b/%Y")

    for dire in dirs:
        sel_error = re.findall("error.", dire)
        sel_access = re.findall("access.", dire)
        line = True
        # error logs

        if sel_error:
            f = open('/var/log/apache2/' + str(dire), "r")
            g = open('/home/student/backup_logs/backup_week_'+ str(week_number)+ '/'+ 'logs.apache.error.'+str(today), "a")
            while line:
                current_line = f.readline()
                if current_line != '':
                    select = re.findall(str(date_error_format), current_line)
                    if select:
                        g.write(current_line)
                else:
                    line = False
            f.close()
            g.close()

        # access logs

        elif sel_access:
            ff = open('/var/log/apache2/' + str(dire), "r")
            gg = open('/home/student/backup_logs/backup_week_'+ str(week_number)+ '/' + 'logs.apache.access.' + str(today), "a")
            while line:
                current = ff.readline()
                if current != '':
                    sele = re.findall(str(date_access_vhost), current)
                    if sele:
                        gg.write(current)
                else:
                    line = False
            ff.close()
            gg.close()

        else:
            print("unknown file")


def check_if_week_folder_exists(week_number):
    dirs = os.listdir('/home/student/backup_logs/')
    find = False
    for dire in dirs:
        check = re.findall("backup_week_" + str(week_number), dire)
        if check:
            find = True
            break
    if find:
        print("Directory " + str(week_number) + " already exists")
    else:
        os.mkdir('/home/student/backup_logs/backup_week_'+ str(week_number), 0o755)
        print("Directory week " + str(week_number) + " created")


def autoremove_files_after_x_weeks(week_number, day_number, today):
    if day_number == 1:
        folder = '/home/student/backup_logs/backup_week_' + str(week_number -4)
        f = open('/home/student/backup_logs/trace.log', "a")
        dirs = os.listdir('/home/student/backup_logs/')
        for dire in dirs:
            check = re.findall("backup_week_" + str(week_number-4), dire)
            if check:
                shutil.rmtree(folder)
                print("dossier backup_logs/backup_week_" + str(week_number-4) + " a supprimé")
                f.write(str(today) + '\tSUPPRESSION' + '\t' + dire + '\t\t' + folder + '\t\t' + "NOW" + '\t\t\tOK\n')
        f.close()

check_if_week_folder_exists(week_number)
get_tomcat_logs(today, week_number)
get_apache_logs(week_number)
autoremove_files_after_x_weeks(week_number, day_number, today)
