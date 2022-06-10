from random import randint, random
import sys
sys.path.append("..")
from Komponente.formatiranje import *
from Komponente.Zahtevi import *
from Model.Resurs import *

import socket
import time

TCP_IP = socket.gethostname()
TCP_PORT = 5005
BUFFER_SIZE = 1024

zahtevi=[zahtev1, zahtev2, zahtev3, zahtev4,zahtev5, zahtev6, zahtev7, zahtev8,zahtev9, zahtev10, zahtev11, zahtev12]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((TCP_IP, TCP_PORT))
except socket.error as e:
    print(str(e))

while 1:
    for z in zahtevi:
        MESSAGE = str(z)
        s.send(MESSAGE.encode())
        odgovor = s.recv(BUFFER_SIZE)
        print("Vraceni podaci od servera:")
        print(odgovor.decode())
        time.sleep(3)
    break
s.close()
