import socket
from repoFunkcije import konektuj_se, config, izvrsiupit
####KONEKCIJA SA BAZOM
[con, cur] = konektuj_se(config)
####KONEKCIJA SA XMLADAPTEROM
TCP_IP = socket.gethostname()
TCP_PORT2 = 8007
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((TCP_IP, TCP_PORT2))
s.listen(0)

connAdapter, addrAdapter = s.accept()
print('Connection address:', addrAdapter,"\n")


while 1:
    sqlzahtev = connAdapter.recv(BUFFER_SIZE)
    #sqlzahtev = "SELECT * from student"
    if not sqlzahtev:
        print("Nema vise zahteva")
        break
    
    poruka = izvrsiupit(sqlzahtev,con)
    print(poruka)
    connAdapter.send(poruka.encode('utf-8'))

cur.close()
con.close()  
connAdapter.close()