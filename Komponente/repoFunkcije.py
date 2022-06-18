import mysql.connector

config = {
    'host': "localhost",
    'user': "root",
    'password': "root",
    'database': "repo"
}

def izvrsiupit(sqlzahtev):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute(sqlzahtev)
        records = cursor.fetchall()
        #print("Total number of rows affected: ", cursor.rowcount)
        
        
        poruka = "Total number of rows affected: " + str(cursor.rowcount) +" "

        zahtev = sqlzahtev
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

            if(fields == "*" or fields == ''):
                if(noun == "student"):
                    fields = "idstudent, ime, prezime, brojindeksa"
                elif(noun == "profesor"):
                    fields = "idprofesor, ime, prezime, predmet"
                elif(noun == "fakultet"):
                    fields = "idfakultet, naziv, brojstudenata, grad"

            polja = fields.split(",")

        if(bool(records)):
            for row in records:
               
                poruka = poruka + '\n'
                poruka = poruka + noun + ": { \n"
                for i in range(0, len(polja)):
                    poruka = poruka + '"' + str(polja[i]) + "\" : \"" + str(row[i]) + '", \n'
               
                poruka = poruka + "}"
             
        else:
            r_cnt = cursor.rowcount
            poruka = "Number of rows affected: " + str(r_cnt); 
    except mysql.connector.Error as e:
        #print("Error reading data from MySQL table", e)
        poruka = "Error reading data from MySQL table: " + e.msg
    return str(poruka)

