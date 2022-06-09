from asyncio.windows_events import NULL

from typing import ByteString
import xml.etree.ElementTree as ET
import mysql.connector

#ovde treba da imam vezu sa bazom i jedan fajl u kom cu
#privremeno da cuvam xml parsiran iz JSON-a

import socket
import random
import time

import argparse
import re
import sys

def ToSql(data):
    #upisi(data)
    #tree = ET.parse("Temp.xml")   #parsira direkt iz prethodnog adaptera
    #data2 = tree.findall('request')

    sqlZahtev = ""
    verb = ""
    noun = ""
    fields = ""
    query = ""

    xmlReq = data[10 : -10]
    l = len(xmlReq)
    glagol = xmlReq[5 : l]

    for i in range(0, l):
        if(glagol[i] == '<'):
            verb = glagol[0:i]
            glagol = glagol[i : l]
            break
        
    glagol = glagol[13 : l]
    for i in range(0, l):
        if(glagol[i] == '<'):
            noun = glagol[0:i]
            glagol = glagol[i : l]
            break

    glagol = glagol[7 : l]
    l1 = len(glagol)

    if(l1 == 0):
        print('nema polja query i fields')
    else:
        glagol = glagol[7 : l1]
        for i in range(0, l1):
            if(glagol[i] == '<'):
                query = glagol[0:i]
                glagol = glagol[i : l1]
                break
        glagol = glagol[8 : l1]
        l2 = len(glagol)
        if(l2 == 0):
            print('nema polja fields')
        else:
            glagol = glagol[8 : l2]
            for i in range(0, l2):
                if(glagol[i] == '<'):
                    fields = glagol[0:i]
                    glagol = glagol[i : l2]
                    break


    if(query != ""):
        # polja = ""
        # vrednosti = []
        # l = len(query)
        # for i in range(0, l):
        #     if(query[i] == '='):
        #         polja = query[0:i-1] + ", "
        #         query = query[i : len(query)]
        #     if(query[i] == ';'):
        #         vrednosti = query[0 : i]
        #         query = query[i : len(query)]
        #     l = len(query)
        query = query.replace(';', " AND")
        

    if(fields != ""):
        fields = fields.replace(';', ',')
    else:
        fields = '*'

    if(verb == 'GET'):
        if(query != ""):
            sqlZahtev = "SELECT " + fields + " FROM " + noun + " WHERE " + query;
        else:
            sqlZahtev = "SELECT" + fields + "FROM " + noun;
    elif(verb == 'POST'):
        
        sqlZahtev = "INSERT INTO " + noun + "(" + fields + ")" + " VALUES "; #treba da se dovrsi
    elif(verb == 'PATCH'):
        sqlZahtev = 'UPDATE ' + noun + ' SET ' + query;
    elif(verb == 'DELETE'):
        sqlZahtev = 'DELETE ' + fields +  'FROM ' + noun + " WHERE " + query;
    else:
        print("Neadekvatan xml zahtev")


    return sqlZahtev

def BackToXml():
    
    #preuzmi odgovor iz baze (kog je formata?) i dobavi vrednosti ovih polja:
    #koneektuje se na repo, posalje sqlZahtev koji je prosledjen i preuzme odgovor koji se dalje parsira

    #1054 (42S22) exception code ukazuje na nepostojeca polja i kolone, tj los format zahteva


    status = ""
    status_code = ""
    payload = ""
    xmlOdgovor = "<response><status>" + status + "</status> <status_code>" + status_code + "</status_code> <payload>"+payload+"</payload></response>";

    return xmlOdgovor



####KONEKCIJA SA COMMBUS
TCP_IP = socket.gethostname()
# TCP_PORT = 5006
BUFFER_SIZE = 1024
# scommbus = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# try:
#     scommbus.connect((TCP_IP, TCP_PORT))
# except socket.error as e:
#     print(str(e)) 

#ovde se iz commbusa prtima xml zahtev
#xmlzahtev = scommbus.recv(BUFFER_SIZE)
#treba da ga pretvori u sql i posalje repozitorijumu
#probni xmlZahtev 
#xmlzahtev = "<request><verb>GET</verb><noun>resurs</noun><query>naziv='mika'; tip='1'</query><fields>id; naziv; opis</fields></request>"
xmlzahtev = ""
sqlzahtev = ToSql(xmlzahtev)

####KONEKCIJA SA REP isto ce mu biti klijent!!
TCP_PORT2 = 8007
srep = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srep.connect((TCP_IP, TCP_PORT2))
#poslace sqlzahtev repozitorijumu koji on treba da obradi i vrati podatke

sqlReq = sqlzahtev.encode('utf-8')
srep.send(sqlReq)
#nad ovim podacima treba izvrsiti back to xml i onda ih vratiti commbusu

vraceniPodaci = srep.recv(BUFFER_SIZE)
print(vraceniPodaci)
#scommbus.send(vraceniPodaci)

srep.close()
#scommbus.close()