from asyncio.windows_events import NULL
from typing import ByteString
import xml.etree.ElementTree as ET
import mysql.connector

#ovde treba da imam vezu sa bazom i jedan fajl u kom cu
#privremeno da cuvam xml parsiran iz JSON-a

import socket
import random
import time

def upisi(data):
    data1 = data.decode("utf-8") 
    open("Temp.xml", "w").write(data1)


def ToSql(data):
    upisi(data)
    tree = ET.parse("Temp.xml")   #parsira direkt iz prethodnog adaptera
    data2 = tree.findall('request')

    sqlZahtev = ""

    for i, j in zip(data2, range(1, 4)):
        verb = i.find('verb').text
        noun = i.find('noun').text
        
        if(i.find('query') != NULL):
            query = i.find('query').text
        else:
            query = ""

        if(i.find('fields') != NULL):
            fields = i.find('fields').text
        else:
            fields = ""

        
        if(verb == 'GET'):
            sqlZahtev = "select " + fields + " from " + noun + " where " + query;

        if(verb == 'POST'):
            sqlZahtev = "insert into " + noun + " ( " + fields + " ) VALUES ( " + query + " )";
            
        if(verb == 'DELETE'):
            sqlZahtev = "delete from " + noun + " where " + query;

        if(verb == 'PATCH'):
            sqlZahtev = "update " + noun + " set " + query;

    return sqlZahtev

def BackToXml():
    
    #preuzmi odgovor iz baze (kog je formata?) i dobavi vrednosti ovih polja:
    #koneektuje se na repo, posalje sqlZahtev koji je prosledjen i preuzme odgovor koji se dalje parsira

    status = ""
    status_code = ""
    payload = ""
    xmlOdgovor = "<response><status>" + status + "</status> <status_code>" + status_code + "</status_code> <payload>"+payload+"</payload></response>";

    return xmlOdgovor



####KONEKCIJA SA COMMBUS
TCP_IP = socket.gethostname()
TCP_PORT = 5006
BUFFER_SIZE = 1024
scommbus = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    scommbus.connect((TCP_IP, TCP_PORT))
except socket.error as e:
    print(str(e))

#ovde se iz commbusa prtima xml zahtev
xmlzahtev = scommbus.recv(BUFFER_SIZE)
#treba da ga pretvori u sql i posalje repozitorijumu
#sqlzahtev = ToSql(xmlzahtev)

####KONEKCIJA SA REP isto ce mu biti klijent!!
TCP_PORT2 = 8007
srep = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srep.connect((TCP_IP, TCP_PORT2))
#poslace sqlzahtev repozitorijumu koji on treba da obradi i vrati podatke
#srep.send(sqlzahtev)
#nad ovim podacima treba izvrsiti back to xml i onda ih vratiti commbusu

vraceniPodaci = srep.recv(BUFFER_SIZE)
print(vraceniPodaci)
#scommbus.send(vraceniPodaci)

srep.close()
scommbus.close()