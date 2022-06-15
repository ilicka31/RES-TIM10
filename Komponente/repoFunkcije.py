from multiprocessing import connection
import mysql.connector
from mysql.connector import Error

config = {
    'host': "localhost",
    'user': "root",
    'password': "root",
    'database': "repo"
}

def konektuj_se(c):
    try:
        connection = mysql.connector.connect(**c)
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
        poruka = str(e).encode('utf-8')
        return poruka

def izvrsiupit(sqlzahtev, conn):
    try:
        cursor = conn.cursor()
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