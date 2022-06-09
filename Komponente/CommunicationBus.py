import sys
import ast
sys.path.append("..")
from Komponente.formatiranje import format
from Model.Resurs import *
from Komponente.JsonXmlAdapter import *
#from Komponente.XmlDataBaseAdapter import ToSql, BackToXml

import socket
from _thread import *

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

#TCP_PORT2 = 8006
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((TCP_IP, TCP_PORT))
#s.listen()
#s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s2.bind((TCP_IP, TCP_PORT2))
#s2.listen(0)
#conn, addr = s.accept()
#print('Connection address:', addr,"\n")
#conn2, addr2 = s.accept()
#print('Connection address:', addr2,"\n")
#while 1:
    #data = conn.recv(BUFFER_SIZE)
    #if not data: break
    #j =ast.literal_eval(data.decode('utf-8'))
    #z = format(j)
    #if(z):
        #xml = ToXmlFromJson(j)
        #conn.send(xml)
        
        #ToSql(xml) #poslao je u drugi adapter koji komunicira sa bazom
        #odgovor = BackToXml()

        #odgovorBytes = str.encode(odgovor)
        #type(odgovorBytes) # ensure it is byte representation

        #xmlodgovor = conn2.recv(BUFFER_SIZE)
        #odgovorBytes = ToJsonFromXml(xmlodgovor)

        #conn.send(odgovorBytes)
#conn.close()
#conn2.close()

def client_handler(conn):
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        j = ast.literal_eval(data.decode('utf-8'))
        z = format(j)
        if(z):
            xml = ToXmlFromJson(j)
            print(xml)
            #conn.sendall(xml)
        
            #ToSql(xml) #poslao je u drugi adapter koji komunicira sa bazom
            #odgovor = BackToXml()
            #odgovorBytes = str.encode(odgovor)
            #type(odgovorBytes) # ensure it is byte representation

            #xmlodgovor = conn.recv(BUFFER_SIZE)
            #odgovorBytes = ToJsonFromXml(xmlodgovor)

            #conn.sendall(odgovorBytes)
    conn.close()

def accept_connections(ServerSocket):
    Client, address = ServerSocket.accept()
    print(f'Connected to: {address[0]}:{str(address[1])}')
    start_new_thread(client_handler, (Client, ))

def start_server(host, port):
    ServerSocket = socket.socket()
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print(f'Server is listening on the port {port}...')
    ServerSocket.listen()

    while True:
        accept_connections(ServerSocket)

start_server(TCP_IP, TCP_PORT)