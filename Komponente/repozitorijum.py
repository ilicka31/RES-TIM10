from doctest import OutputChecker
from multiprocessing import connection
import mysql.connector
from mysql.connector import Error
from setuptools import find_namespace_packages
import socket

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='repo',
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
    #poruka = str(e).encode('utf-8')
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

while 1:
    sqlzahtev = connAdapter.recv(BUFFER_SIZE)
    if not sqlzahtev:
        print("Puko sam jer nije stiglo nista")
        break

    try:
        # cursor.execute(sqlzahtev)
        # cursor.fetchall()
        # #results = connection.cmd_query(sqlzahtev)
        # records = cursor.fetchall()
        # print("Total number of rows affected: ", cursor.rowcount)

        # rCnt = 0
        # if(records):
        #     for row in records:
        #         rCnt += 1
        #         poruka = "Rows affected: \n"
        #         poruka = poruka + rCnt + '. ' + row[0] + row[1] + row[2] + row[3]
        # else:
        #     rCnt = cursor.rowcount
        #     poruka = "Number of rows affected: " + str(rCnt);    
    
        cursor.execute(sqlzahtev)
        #cursor.fetchall();
        #results = connection.cmd_query(sqlzahtev)
        records = cursor.fetchall()
        print("Total number of rows affected: ", cursor.rowcount)
        
        rCnt = 0
        poruka = "Total number of rows affected: " + str(cursor.rowcount)
        if(bool(records)):
            for row in records:
                rCnt += 1
                poruka = poruka + '\n' + str(rCnt) + '. ' 
                for i in range(0, len(row)):
                    poruka = poruka + ' ' + str(row[i])
        else:
            rCnt = cursor.rowcount
            poruka = "Number of rows affected: " + str(rCnt); 
            

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
        poruka = "Error reading data from MySQL table: " + e.msg

    connAdapter.send(poruka.encode('utf-8'))
    
connAdapter.close()