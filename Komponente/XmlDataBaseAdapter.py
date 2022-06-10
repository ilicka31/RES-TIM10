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

    polja = ""
    vrednosti = ""
    poljaL = []
    vrednostiL = []
    if(query != ""):
        jednako = 0
        zarez = 0
        l = len(query)
        for i in range(0, l+1):
            if(query[i] == '='):
                if(zarez==0):
                    polja = polja + query[zarez:i]
                else:
                    polja = polja + ", " + query[zarez+1:i]
                jednako = i
                poljaL.append(query[zarez:i])
            if(query[i] == ';'):
                if(vrednosti == ""):
                     vrednosti = vrednosti + query[jednako+1 : i]
                else:
                    vrednosti = vrednosti + ", " + query[jednako+1 : i]
                vrednostiL.append(query[jednako+1 : i])
                zarez = i
            if(i == l-1):
                if(vrednosti == ""):
                     vrednosti = vrednosti + query[jednako+1 : i]
                else:
                    vrednosti = vrednosti + ", " + query[jednako+1 : i+1]
                vrednostiL.append(query[jednako+1 : i])
                break
        
    uslov = ""
    if("id" in poljaL):
        for i in range(0, len(poljaL)):
            if(poljaL[i] == "id"):
                uslov = poljaL[i] + '=' + vrednostiL[i] + ";"

    #izmena = query - uslov[0:len(uslov)-1]

    if(fields != ""):
        fields = fields.replace(';', ',')
    else:
        fields = '*'
    if(verb == 'GET'):
        if(query != ""):
            sqlZahtev = "SELECT " + fields + " FROM " + noun + " WHERE " + query.replace(";", " AND ")
        else:
            sqlZahtev = "SELECT" + fields + "FROM " + noun
    elif(verb == 'POST'):
        sqlZahtev = "INSERT INTO " + noun + "(" + polja + ")" + " VALUES (" + vrednosti + ")" #treba da se dovrsi
    elif(verb == 'PATCH'):
      
        sqlZahtev = 'UPDATE ' + noun + ' SET ' + fields.replace(";", ", ") + ' WHERE ' + query.replace(";"," AND ")  
    elif(verb == 'DELETE'):
        sqlZahtev = 'DELETE FROM ' + noun + " WHERE " + query.replace(";", " AND ")
    else:
        print("Neadekvatan xml zahtev")


    return sqlZahtev

def BackToXml(poruka):
    
    #preuzmi odgovor iz baze (kog je formata?) i dobavi vrednosti ovih polja:
    #koneektuje se na repo, posalje sqlZahtev koji je prosledjen i preuzme odgovor koji se dalje parsira

    #1054 (42S22) exception code ukazuje na nepostojeca polja i kolone, tj los format zahteva
    
    poruka = poruka.decode('utf-8')
    status = ""
    status_code = ""
    payload = ""
    if("Number of rows affected" in poruka):
        status = 'SUCCESS'
        status_code = '2000'
        payload = poruka
    elif("Error reading data from MySQL table" in poruka):
        status = 'BAD_FORMAT'
        status_code = '5000'
        payload = poruka
    
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

#xmlzahtev = "<request><verb>GET</verb><noun>resurs</noun><query>id=5;naziv='mika'</query><fields>id; naziv; surname</fields></request>"
    sqlzahtev = ToSql(xmlzahtev)
    print("SQLZAHTEVV")
    print(sqlzahtev)
    if not sqlzahtev:
       break
    srep.send(sqlzahtev.encode())
    vraceniPodaci = srep.recv(BUFFER_SIZE)
    vraceniPodaci = BackToXml(vraceniPodaci)
    scommbus.send(vraceniPodaci.encode())

srep.close()
scommbus.close()