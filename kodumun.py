import socket
tarama= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hostname = socket.gethostname()

ipAdress=socket.gethostbyname(hostname)

maxPort=65535
minPort=0
portlar=True

for port in range(minPort,maxPort+1):
    try:
        tarama.connect(ipAdress,port)
        print("{}' portu açık !!!".format(port))
        portlar=False
        tarama.close()
        
    except:
        pass
            
if(portlar):
    print("Tüm portlar kapalı")