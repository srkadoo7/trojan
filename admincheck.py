import ctypes

def checkadmin():
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        return '[-] We are NOT admin! '
    else:
        return '[+] We are admin :) '
    
