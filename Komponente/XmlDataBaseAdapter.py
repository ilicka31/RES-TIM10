import socket
from DataAdapterFunkcije import back_to_xml, to_sql

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

    if sqlzahtev == "Neadekvatan xml zahtev":
        vraceniPodaci = """<response>
                                <status>BAD_FORMAT</status> 
                                <status_code>5000</status_code> 
                                <payload>Neadekvatan xml zahtev</payload>
                            </response>""";
        scommbus.send(vraceniPodaci.encode())
    else:
        srep.send(sqlzahtev.encode())
        vraceniPodaci = srep.recv(BUFFER_SIZE)
        vraceniPodaci = back_to_xml(vraceniPodaci)
        scommbus.send(vraceniPodaci.encode())

srep.close()
scommbus.close()