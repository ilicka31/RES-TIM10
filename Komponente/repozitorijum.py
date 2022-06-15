from doctest import OutputChecker
from lib2to3.pgen2.token import NEWLINE
from multiprocessing import connection
import mysql.connector
from mysql.connector import Error
from setuptools import find_namespace_packages
import socket

MYSQL_HOST = "localhost"
MYSQL_USER ="root"
MYSQL_PASSWORD = "root"
MYSQL_DB ="repo"

config = {
    'host': MYSQL_HOST,
    'user': MYSQL_USER,
    'password': MYSQL_PASSWORD,
    'database': MYSQL_DB
}
def konektuj_se(h, db,u, p):
    try:
        connection = mysql.connector.connect(host=h,
                                            database=db,
                                            user=u,
                                            password=p)
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server verison ", db_info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            return [connection, cursor]
    except Error as e:
        print("Error while connecting to MySQL", e)
        poruka = "Error while connecting to MySQL" + str(e).encode('utf-8')
        return poruka
    #finally:
    #    if connection.is_connected():
    #        cursor.close()
    #        connection.close()
    #        print("MySQL connection is closed")

def izvrsiupit(sqlzahtev, cursor):
    try:
        cursor.execute(sqlzahtev)
        records = cursor.fetchall()
        print("Total number of rows affected: ", cursor.rowcount)
        
        r_cnt = 0
        poruka = "Total number of rows affected: " + str(cursor.rowcount)
        if(bool(records)):
            for row in records:
                r_cnt += 1
                poruka = poruka + '\n' + str(r_cnt) + '. ' 

                red = str(row).replace('(', '{')
                red = red.replace(')', '}')
                poruka = poruka + red
        else:
            r_cnt = cursor.rowcount
            poruka = "Number of rows affected: " + str(r_cnt); 
        

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
        poruka = "Error reading data from MySQL table: " + e.msg
    return poruka
####KONEKCIJA SA BAZOM
[con, cur] = konektuj_se(config["host"], config["database"], config["user"],config["password"])
####KONEKCIJA SA XMLADAPTEROM
TCP_IP = socket.gethostname()
TCP_PORT2 = 8007
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((TCP_IP, TCP_PORT2))
s.listen(0)

connAdapter, addrAdapter = s.accept()
print('Connection address:', addrAdapter,"\n")

while 1:
    sqlzahtev = connAdapter.recv(BUFFER_SIZE)
    if not sqlzahtev:
        print("Nema vise zahteva")
        break
    poruka = izvrsiupit(sqlzahtev,cur)
    print(poruka)
    connAdapter.send(poruka.encode('utf-8'))
    
connAdapter.close()