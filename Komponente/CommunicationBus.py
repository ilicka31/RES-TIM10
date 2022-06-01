#DA BI MOGLI DA PRISTUPAMO KLASAMA I FAJLOVIMA
#IZ DRUIH FOLDERA
#import sys
#sys.path.append("..")
#from Komponente.formatiranje import *
#from Komponente.Zahtevi import *
#from Model.Resurs import *

#PRAVLJENJE SOKETA ZA KOMUNIKACIJU
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

while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data.decode(), "\n")
   
   # conn.send(data)  # echo
conn.close()

