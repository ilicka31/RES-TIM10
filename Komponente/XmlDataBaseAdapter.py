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
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

xmlzahtev = s.recv(BUFFER_SIZE)
sqlzahtev = ToSql(xmlzahtev)

####KONEKCIJA SA REP
TCP_PORT2 = 8007
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.bind((TCP_IP, TCP_PORT2))
s2.listen(0)

conn2, addr2 = s2.accept()
print('Connection address:', addr2,"\n")

conn2.send(sqlzahtev)

#treba da dobije odgovor od rep zatim da prebaci u XML format i posalje nazad CommBus

#conn.close()
conn2.close()