from unittest import TestCase
import mysql.connector
from mock import patch
import sys
sys.path.insert(0, "../..")
from Komponente.repoFunkcije import config

MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_DB = "testdb"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"

configuration = {
    'host': MYSQL_HOST,
    'user': MYSQL_USER,
    'password': MYSQL_PASSWORD
    #'database': MYSQL_DB
}
class MockDB(TestCase):
    @classmethod
    def setUpClass(cls):
        cnx = mysql.connector.connect(host = MYSQL_HOST,
                                      user= MYSQL_USER,
                                      password = MYSQL_PASSWORD)
        cursor = cnx.cursor()

        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS testdb")
            cnx.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print("Failed creating database: " + err.msg)
            

        cursor= cnx.cursor()
        cursor.execute("use testdb")
        cursor.close()

        querys = """CREATE TABLE IF NOT EXISTS `student` (
                  `idstudent` integer NOT NULL PRIMARY KEY ,
                  `ime` varchar(30) NOT NULL,
                  `prezime` varchar(30) NOT NULL,
                  `brojindeksa` varchar(30) NOT NULL
                )"""

        queryp = """CREATE TABLE IF NOT EXISTS `profesor` (
                  `idprofesor` integer NOT NULL PRIMARY KEY ,
                  `ime` varchar(30) NOT NULL,
                  `prezime` varchar(30) NOT NULL,
                  `predmet` varchar(30) NOT NULL
                )"""

        queryf = """CREATE TABLE IF NOT EXISTS `fakultet` (
                  `idfakultet` integer NOT NULL PRIMARY KEY ,
                  `naziv` varchar(30) NOT NULL,
                  `brojstudenata` integer NOT NULL,
                  `grad` varchar(30) NOT NULL
                )"""

        query = [querys, queryp, queryf]
        for q in query:
            try:
                cursor=cnx.cursor()
                cursor.execute(q)
                cnx.commit()
                cursor.close()
            except mysql.connector.Error as err:
                    print("Failed create table"+err.msg)


        inserts = """INSERT INTO `student` VALUES
                            (1, 'Marko', 'Markovic', 'RA22/2017'),
                            (2, 'Janko','Jankovic', 'SW55/2018'),
                            (3, 'Stanko','Stankovic', 'SW45/2019'),
                            (4, 'Darko','Darkovic', 'IN55/2018'),
                            (5, 'Petko','Petkovic', 'IT28/2018');
                            """
        insertp = """INSERT INTO `profesor` VALUES
                            (1,'Milana','Bojanic','SCADA'),
                            (2,'Milos','Markovic','WEB'),
                            (3,'Imre','Lendak','ADS'),
                            (4,'Ivan','Kastelan','LPRS'),
                            (5,'Petar','Maric','PJISP');
                            """
        insertf = """INSERT INTO `fakultet` VALUES
                            (1,'FTN',15000,'Novi Sad'),
                            (2,'ETF',10000,'Beograd'),
                            (3,'FON',7000,'Beograd'),
                            (4,'PMF',5000,'Novi Sad'),
                            (5,'TMF',9000,'Novi Sad');
                            """

        insetr = [inserts, insertp, insertf]
        for i in insetr:
            try:
                cursor= cnx.cursor()
                cursor.execute(i)
                cnx.commit()
                cursor.close()
            except mysql.connector.Error as err:
                print("Data insertion to student failed \n" + err.msg)
        

        

        testconfig ={
            'host': MYSQL_HOST,
            'user': MYSQL_USER,
            'password': MYSQL_PASSWORD,
            'database': MYSQL_DB
        }
        cls.mock_db_config = patch.dict(config, testconfig)
        cnx.close()

    @classmethod
    def tearDownClass(cls):
        cnx = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )
        cursor = cnx.cursor(dictionary=True)

        # drop test database
        try:
            cursor.execute("DROP DATABASE "+ MYSQL_DB)
            cnx.commit()
           
        except mysql.connector.Error:
            print("Database {} does not exists. Dropping db failed".format(MYSQL_DB))
        cursor.close()
        cnx.close()

