import socket
import tweetip

def sdiscover():
    with open('ip.txt','r') as hosts:
        for hname in hosts:
            if hname == '':
                try:
                   host = tweetip.gettip()
                   return host
                except:
                    return '0.0.0.0'
            try:
                return socket.gethostbyname(hname.strip())
            except:
                pass    
        return '0.0.0.0'        

