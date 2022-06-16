from unittest import TestCase
import mysql.connector
from mysql.connector import errorcode
from mock import patch
import sys
sys.path.insert(0, "../..")
from Komponente.repoFunkcije import *

MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_DB = "testdb"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"

configuration = {
    'host': MYSQL_HOST,
    'user': MYSQL_USER,
    'password': MYSQL_PASSWORD,
    'database': MYSQL_DB
}
class MockDB(TestCase):
    @classmethod
    def setUpClass(cls):
        cnx = mysql.connector.connect(**configuration)
        cursor = cnx.cursor()

       # try:
       #     cursor.execute("DROP DATABASE IF EXISTS {}".format(MYSQL_DB))
       #     cursor.close()
       #     print("DB dropped")
       # except mysql.connector.Error as err:
       #     print("{}{}".format(MYSQL_DB, err))
#
       # cursor = cnx.cursor()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS " + MYSQL_DB)
            cnx.commit()
            print("KREIRO")
            cursor.close()
        except mysql.connector.Error as err:
            print("Failed creating database: " + str(err))
            exit(1)
        

        query = """CREATE TABLE `student` (
                  `idstudent` integer NOT NULL PRIMARY KEY ,
                  `ime` varchar(30) NOT NULL,
                  `prezime` varchar(30) NOT NULL,
                  `brojindeksa` varchar(30) NOT NULL
                )"""
        try:
            cursor=cnx.cursor()
            cursor.execute(query)
            print("KREIRO test tablu")
            cnx.commit()
            cursor.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("test_table already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

        insert_data_query = """INSERT INTO `student` (`idstudent`, `ime`, `prezime`,`brojindeksa`) VALUES
                            ('1', 'Marko', 'Markovic','RA22/2017'),
                            ('2', 'Janko','Jankovic','SW55/2018'),
                            ('3', 'Stanko','Stankovic','SW45/2019'),
                            ('4', 'Darko','Darkovic','IN55/2018'),
                            ('5', 'Petko','Petkovic','IT28/2018')
                            """
        try:
            cursor= cnx.cursor()
            cursor.execute(insert_data_query)
            cnx.commit()
            cursor.close()
            print("INSERTOVO")
        except mysql.connector.Error as err:
            print("Data insertion to test_table failed \n" + err)
        
        

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
            cursor.execute("DROP DATABASE"+ MYSQL_DB)
            cnx.commit()
           
        except mysql.connector.Error as err:
            print("Database {} does not exists. Dropping db failed".format(MYSQL_DB))
        cursor.close()
        cnx.close()


