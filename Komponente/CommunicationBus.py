import sys
import ast
sys.path.append("..")
from Komponente.formatiranje import format
from Model.Resurs import *
from Komponente.JsonXmlAdapter import *
from Komponente.XmlDataBaseAdapter import ToSql, BackToXml

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
print('Connection address:', addr,"\n")
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    j =ast.literal_eval(data.decode('utf-8'))
    z = format(j)
    if(z):
        xml = ToXmlFromJson(j)
        ToSql(xml) #poslao je u drugi adapter koji komunicira sa bazom
        odgovor = BackToXml()
        conn.send(odgovor)
conn.close()

