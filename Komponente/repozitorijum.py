from multiprocessing import connection
import mysql.connector
from mysql.connector import Error
from setuptools import find_namespace_packages
#from Komponente.XmlDataBaseAdapter import *

import socket
import random
import time


try:
    connection = mysql.connector.connect(host='localhost',
                                        database='repozitorijum',
                                        user='root',
                                        password='root')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server verison ", db_Info)

        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
#finally:
#    if connection.is_connected():
#        cursor.close()
#        connection.close()
#        print("MySQL connection is closed")


####KONEKCIJA SA XMLADAPTEROM
TCP_IP = socket.gethostname()
TCP_PORT2 = 8007
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT2))
s.listen(0)

connAdapter, addrAdapter = s.accept()
print('Connection address:', addrAdapter,"\n")

sqlzahtev = connAdapter.recv(BUFFER_SIZE)
#ovde samo izvrsiti direktno na bazu upit i kad se vrate ti podaci vratiti ih adapteru
#connAdapter.send(PODACI KOJI SU SE VRATILI)

#cursor.execute(sqlzahtev)
#connAdapter.send()
connAdapter.close()