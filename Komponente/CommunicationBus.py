import sys
import ast
sys.path.append("..")
from Komponente.formatiranje import format
from Model.Resurs import *
from Komponente.JsonXmlAdapter import *
import socket

TCP_IP = socket.gethostname() #localhost
TCP_PORT = 5005
BUFFER_SIZE = 1024
TCP_PORT2 = 5006

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(0)

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.bind((TCP_IP, TCP_PORT2))
s2.listen(0)

connClient, addrClient = s.accept()
print('Connection address:', addrClient,"\n")

connAdapter, addrAdapter = s2.accept() 
print('Connection address:', addrAdapter,"\n")

while 1:
    data = connClient.recv(BUFFER_SIZE)
    if not data: 
        print("Svi zahtevi su obradjeni!")
        break

    j =ast.literal_eval(data.decode('utf-8'))
    z = format(j)
    if(z):
        xml = ToXmlFromJson(j)
        connAdapter.send(xml)  
        xmlodgovor = connAdapter.recv(BUFFER_SIZE)
        odgovorBytes = ToJsonFromXml(xmlodgovor)
        connClient.send(odgovorBytes.encode())
connAdapter.close()
connClient.close()
