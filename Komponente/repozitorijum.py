import socket
from repoFunkcije import  izvrsiupit
####KONEKCIJA SA BAZOM
####KONEKCIJA SA XMLADAPTEROM
TCP_IP = socket.gethostname()
TCP_PORT2 = 8007
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((TCP_IP, TCP_PORT2))
s.listen(0)

connAdapter, addrAdapter = s.accept()
print('Connection address:', addrAdapter,"\n")
print("Repozitorijum konektovan sa XmlDataBaseAdapterom")
while 1:
    sqlzahtev = connAdapter.recv(BUFFER_SIZE)
    print("Dobijen upit za bazu!")
    if not sqlzahtev:
        print("Nema vise zahteva")
        break
    poruka = izvrsiupit(sqlzahtev.decode())
    print("Odgovor iz baze:")
    print(poruka)
    connAdapter.send(poruka.encode())

connAdapter.close()