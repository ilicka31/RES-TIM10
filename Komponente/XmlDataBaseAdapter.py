from DataAdapterFunkcije import *
####KONEKCIJA SA COMMBUS
TCP_IP = socket.gethostname()
TCP_PORT = 5006
BUFFER_SIZE = 1024
scommbus = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    scommbus.connect((TCP_IP, TCP_PORT))
except socket.error as e:
    print(str(e)) 

####KONEKCIJA SA REP 
TCP_PORT2 = 8007
srep = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    srep.connect((TCP_IP, TCP_PORT2))
except socket.error as e:
    print(str(e)) 

while 1:
    xmlzahtev = scommbus.recv(BUFFER_SIZE)
    if not xmlzahtev: 
        print("Puko sam jer nista nije stiglo")
        break

    xmlzahtev = xmlzahtev.decode()
    xmlzahtev = xmlzahtev.replace("&apos;","'")
    xmlzahtev = xmlzahtev.replace('<?xml version="1.0" encoding="UTF-8" ?>','')
    xmlzahtev = xmlzahtev.replace('<root>', '<request>')
    xmlzahtev = xmlzahtev.replace('</root>', '</request>')  

    sqlzahtev = to_sql(xmlzahtev)
    
    if not sqlzahtev:
       break
    srep.send(sqlzahtev.encode())
    vraceni_podaci_iz_baze = srep.recv(BUFFER_SIZE)
    print("Podaci vraceni iz baze!")
    vraceniPodaci = back_to_xml(vraceni_podaci_iz_baze)
    scommbus.send(vraceniPodaci.encode())

srep.close()
scommbus.close()