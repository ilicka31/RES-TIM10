#DA BI MOGLI DA PRISTUPAMO KLASAMA I FAJLOVIMA
#IZ DRUIH FOLDERA
import sys
import json
sys.path.append("..")
from Komponente.formatiranje import format
from Model.Resurs import *
from Komponente.JsonXmlAdapter import *
from Komponente.XmlDataBaseAdapter import ToSql

import random
import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(0)

conn, addr = s.accept()
print('Connection address:', addr)
p=0
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break

    z=format(data)
    if(z):
        xml=ToXml(data,p)
        print("received data:", z, "\n")
        print(xml)
        p=1
        data=ToJson(ToSql(xml))
        conn.send(data)
   
        

   
   # conn.send(data)  # echo
conn.close()

