from mockdb import MockDB
import unittest
import sys
sys.path.insert(0, "../..")
from Komponente.repoFunkcije import izvrsiupit


class TestBaza(MockDB):

    def test_select(self):
       with self.mock_db_config:
            self.maxDiff= None
            self.assertEqual(izvrsiupit("""SELECT brojindeksa, ime, prezime  FROM student WHERE idstudent = '1' """), """Total number of rows affected: 1 \nstudent: { \n\"brojindeksa\" : \"RA22/2017\", \n\" ime\" : \"Marko\", \n\" prezime \" : \"Markovic\", \n}""")
            self.assertEqual(izvrsiupit("""SELECT * FROM student"""), """Total number of rows affected: 5 \nstudent: { \n\"idstudent\" : \"1\", \n\" ime\" : \"Marko\", \n\" prezime\" : \"Markovic\", \n\" brojindeksa\" : \"RA22/2017\", \n}\nstudent: { \n\"idstudent\" : \"2\", \n\" ime\" : \"Janko\", \n\" prezime\" : \"Jankovic\", \n\" brojindeksa\" : \"SW55/2018\", \n}\nstudent: { \n\"idstudent\" : \"3\", \n\" ime\" : \"Stanko\", \n\" prezime\" : \"Stankovic\", \n\" brojindeksa\" : \"SW45/2019\", \n}\nstudent: { \n\"idstudent\" : \"4\", \n\" ime\" : \"Darko\", \n\" prezime\" : \"Darkovic\", \n\" brojindeksa\" : \"IN55/2018\", \n}\nstudent: { \n\"idstudent\" : \"5\", \n\" ime\" : \"Petko\", \n\" prezime\" : \"Petkovic\", \n\" brojindeksa\" : \"IT28/2018\", \n}""")
            self.assertEqual(izvrsiupit("""SELECT idfakultet, naziv, brojstudenata, grad  FROM fakultet WHERE idfakultet = '1' """),"""Total number of rows affected: 1 \nfakultet: { \n\"idfakultet\" : \"1\", \n\" naziv\" : \"FTN\", \n\" brojstudenata\" : \"15000\", \n\" grad \" : \"Novi Sad\", \n}""")
            self.assertEqual(izvrsiupit("""SELECT * FROM fakultet"""),"""Total number of rows affected: 5 \nfakultet: { \n\"idfakultet\" : \"1\", \n\" naziv\" : \"FTN\", \n\" brojstudenata\" : \"15000\", \n\" grad\" : \"Novi Sad\", \n}\nfakultet: { \n\"idfakultet\" : \"2\", \n\" naziv\" : \"ETF\", \n\" brojstudenata\" : \"10000\", \n\" grad\" : \"Beograd\", \n}\nfakultet: { \n\"idfakultet\" : \"3\", \n\" naziv\" : \"FON\", \n\" brojstudenata\" : \"7000\", \n\" grad\" : \"Beograd\", \n}\nfakultet: { \n\"idfakultet\" : \"4\", \n\" naziv\" : \"PMF\", \n\" brojstudenata\" : \"5000\", \n\" grad\" : \"Novi Sad\", \n}\nfakultet: { \n\"idfakultet\" : \"5\", \n\" naziv\" : \"TMF\", \n\" brojstudenata\" : \"9000\", \n\" grad\" : \"Novi Sad\", \n}""")
            self.assertEqual(izvrsiupit("""SELECT idprofesor, ime, prezime, predmet FROM profesor WHERE idprofesor = '1' """),"""Total number of rows affected: 1 \nprofesor: { \n\"idprofesor\" : \"1\", \n\" ime\" : \"Milana\", \n\" prezime\" : \"Bojanic\", \n\" predmet\" : \"SCADA\", \n}""")
            self.assertEqual(izvrsiupit("""SELECT * FROM profesor"""),"""Total number of rows affected: 5 \nprofesor: { \n\"idprofesor\" : \"1\", \n\" ime\" : \"Milana\", \n\" prezime\" : \"Bojanic\", \n\" predmet\" : \"SCADA\", \n}\nprofesor: { \n\"idprofesor\" : \"2\", \n\" ime\" : \"Milos\", \n\" prezime\" : \"Markovic\", \n\" predmet\" : \"WEB\", \n}\nprofesor: { \n\"idprofesor\" : \"3\", \n\" ime\" : \"Imre\", \n\" prezime\" : \"Lendak\", \n\" predmet\" : \"ADS\", \n}\nprofesor: { \n\"idprofesor\" : \"4\", \n\" ime\" : \"Ivan\", \n\" prezime\" : \"Kastelan\", \n\" predmet\" : \"LPRS\", \n}\nprofesor: { \n\"idprofesor\" : \"5\", \n\" ime\" : \"Petar\", \n\" prezime\" : \"Maric\", \n\" predmet\" : \"PJISP\", \n}""")
    
    def test_delete(self):
        with self.mock_db_config:
            self.assertEqual(izvrsiupit("DELETE from profesor"),"Number of rows affected: 5")        
            self.assertEqual(izvrsiupit("DELETE from student"),"Number of rows affected: 5")
            self.assertEqual(izvrsiupit("DELETE from fakultet"),"Number of rows affected: 5")
            self.assertEqual(izvrsiupit("DELETE from fakultet WHERE idfakultet='1'"),"Number of rows affected: 1")
            self.assertEqual(izvrsiupit("DELETE from fakultet WHERE naziv='FTN'"),"Number of rows affected: 1")
            self.assertEqual(izvrsiupit("DELETE from fakultet WHERE brojstudenata=5000"),"Number of rows affected: 1")
            self.assertEqual(izvrsiupit("DELETE from fakultet WHERE grad='Beograd'"),"Number of rows affected: 2")
            self.assertEqual(izvrsiupit("DELETE from fakultet WHERE grad='Subotica'"),"Number of rows affected: 0")
            self.assertEqual(izvrsiupit("DELETE from tabela"),"Error reading data from MySQL table: Table 'testdb.tabela' doesn't exist")


    def test_insert_into(self):
        with self.mock_db_config:
            self.assertEqual(izvrsiupit("INSERT INTO profesor VALUES(6,'Jovana','Maric','OSKO')"),"Number of rows affected: 1")
            self.assertEqual(izvrsiupit("INSERT INTO profesor (idprofesor, ime, prezime, predmet) VALUES(6,'Jovana','Maric','OSKO')"),"Number of rows affected: 1")
            self.assertEqual(izvrsiupit("INSERT INTO student (idstudent, ime, prezime, brojindeksa) VALUES(6,'Jovana','Maric','IT89/2020')"),"Number of rows affected: 1")
            self.assertEqual(izvrsiupit("INSERT INTO profesor VALUES('Jovana',6,'Maric','OSKO')"),"Error reading data from MySQL table: Incorrect integer value: 'Jovana' for column 'idprofesor' at row 1")

    def test_update(self):
        with self.mock_db_config:
            self.assertEqual(izvrsiupit("UPDATE profesor SET predmet ='OP' WHERE ime='Petar' "),"Number of rows affected: 1")
            self.assertEqual(izvrsiupit("UPDATE profesor SET predmet ='OP' WHERE ime='Petar' AND prezime='Maric' "),"Number of rows affected: 1")
           
    def test_baza(self):
        with self.mock_db_config:
            self.assertEqual(izvrsiupit("CREATE DATABASE IF NOT EXISTS testdb"),"Number of rows affected: 1")  
            self.assertEqual(izvrsiupit("CREATE DATABASE testdb"),"Error reading data from MySQL table: Can't create database 'testdb'; database exists")  
            self.assertEqual(izvrsiupit("CREATE TABLE IF NOT EXISTS `student` (`idstudent` integer NOT NULL PRIMARY KEY ,`ime` varchar(30) NOT NULL,`prezime` varchar(30) NOT NULL,`brojindeksa` varchar(30) NOT NULL)"), "Number of rows affected: 0")
            self.assertEqual(izvrsiupit("CREATE TABLE  `student` (`idstudent` integer NOT NULL PRIMARY KEY ,`ime` varchar(30) NOT NULL,`prezime` varchar(30) NOT NULL,`brojindeksa` varchar(30) NOT NULL)"), "Error reading data from MySQL table: Table 'student' already exists")
            self.assertEqual(izvrsiupit("INSERT INTO `tabela` VALUES(1,'FTN',15000,'Novi Sad')"), "Error reading data from MySQL table: Table 'testdb.tabela' doesn't exist") 
            #self.assertEqual(izvrsiupit("DROP DATABASE testdb"),"Error reading data from MySQL table: Unknown database 'testdb'")  
if __name__ == '__main__':
    unittest.main()