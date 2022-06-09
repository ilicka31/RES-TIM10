
from random import randint, random
import sys
sys.path.append("..")
from Komponente.formatiranje import *
from Komponente.Zahtevi import *
from Model.Resurs import *

import socket
import random
import time
TCP_IP = socket.gethostname()
TCP_PORT = 5005
BUFFER_SIZE = 1024
zahtevi=[zahtev1, zahtev2, zahtev3, zahtev4,zahtev5, zahtev6, zahtev7, zahtev8]
br =0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((TCP_IP, TCP_PORT))
except socket.error as e:
    print(str(e))

while br < 10:
    MESSAGE =str(random.choice(zahtevi))
    s.send(MESSAGE.encode())
    print(f"poslato poruka {br}")
    br= br+1
    odgovor = s.recv(BUFFER_SIZE)
    print(odgovor)
    time.sleep(3)
    


#mora encode jer prima byte a ne string

s.close()
