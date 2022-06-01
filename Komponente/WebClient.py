
from random import randint, random
import sys
sys.path.append("..")
from Komponente.formatiranje import *
from Komponente.Zahtevi import *
from Model.Resurs import *
import socket
import random
import time
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
zahtevi=[zahtev1, zahtev2, zahtev3, zahtev4,zahtev5, zahtev6, zahtev7, zahtev8]
br =0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while br < 10:
    MESSAGE =str(random.choice(zahtevi))
    s.send(MESSAGE.encode())
    br= br+1
    time.sleep(3)
    


#mora encode jer prima byte a ne string

s.close()
