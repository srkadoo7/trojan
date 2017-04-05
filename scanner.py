import socket
import os
def scanner(s,ip,ports):
    scan_result = '' 
    for port in ports.split(','): 
        try: 
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            output = sock.connect_ex((ip, int(port) )) 
            if output == 0:
                scan_result = scan_result + "[+] Port " +port+ " is opened" +'\n'
            else:
                scan_result = scan_result + "[-] Port " +port+" is closed or Host is not reachable" +'\n'
            sock.close()
    
        except Exception, e:
            pass
    s.send (scan_result) 




        
            
   
        










