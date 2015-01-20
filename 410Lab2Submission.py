import socket
import sys
try:
    import thread
except ImportError:
    import _thread as thread

def clientthread(conn):
    #code here
    #while .... 
    while 1:
        pass
        data= conn.recv(1024)
        data2= str(data)
        data2= data2[:len(data2)-2]
        
        reply= "< Hello " +data2 + " >"
        conn.sendall(reply.encode("UTF-8"))        
    
    

try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
except socket.error as msg:
    sys.exit()
    
host=''
port=8888

try:
    s.bind((host,port))
except socket.error as msg:
    sys.exit()
    
print("Socket bind is complete")
s.listen(5)
print("socket now listening")
while 1:
    conn, addr= s.accept()
    thread.start_new_thread(clientthread, (conn,))
conn.close()
s.close()