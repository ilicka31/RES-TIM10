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

        zahtev = sqlzahtev.decode('utf-8')
        tabela = 0
        noun = ""
        fields = ''
        if("SELECT" in zahtev):
            for i in range(0, len(zahtev)):
                if(zahtev[i : i+4] == "FROM"):
                    fields = sqlzahtev[7 : i-1]
                    tabela = i + 5
                if(zahtev[i:i+5] == "WHERE"):
                    noun = zahtev[tabela : i-1]
                    break
                elif(i == len(zahtev)-1):
                    noun = zahtev[tabela:len(zahtev)]

            fields = fields.decode('utf-8')
            if(fields == "*" or fields == ''):
                if(noun == "student"):
                    fields = "idstudent, ime, prezime, brindeksa"
                elif(noun == "profesor"):
                    fields = "idprofesor, ime, prezime, predmet"
                elif(noun == "fakultet"):
                    fields = "idfakultet, naziv, brojstudenata, grad"

            polja = fields.split(",")

        if(bool(records)):
            for row in records:
                r_cnt += 1
                poruka = poruka + '\n' + str(r_cnt) + '. ' 

                poruka = poruka + noun + ": { \n"
                for i in range(0, len(polja)):
                    poruka = poruka + '"' + str(polja[i]) + "\" : \"" + str(row[i]) + '" \n'
               
                poruka = poruka + "}"
        else:
            r_cnt = cursor.rowcount
            poruka = "Number of rows affected: " + str(r_cnt); 
    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
        poruka = "Error reading data from MySQL table: " + e.msg
    return poruka