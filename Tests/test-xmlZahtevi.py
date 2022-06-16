import unittest
import sys


sys.path.append('..')

from Komponente.DataAdapterFunkcije import back_to_xml, to_sql


class TestXmlDataBaseAdapter(unittest.TestCase):
    def test_get(self):
        zahtev1="<request><verb>GET</verb><noun>/resurs/1</noun><query>name='pera';type=1</query><fields>id; name; surname</fields></request>"
        zahtev2="<request><verb>GET</verb><noun>/resurs/1</noun><query>name='pera';type=1</query></request>"
        zahtev3="<request><verb>GET</verb><noun>/resurs/1</noun></request>"
        self.assertEqual(to_sql(zahtev1) , "SELECT id, name, surname FROM /resurs/1 WHERE name='pera' AND type=1")
        self.assertEqual(to_sql(zahtev2) , "SELECT * FROM /resurs/1 WHERE name='pera' AND type=1")
        self.assertEqual(to_sql(zahtev3) , "SELECT*FROM /resurs/1")
        zahtev3="<request><verb>cao</verb><noun>/resurs/1</noun><query>name='pera';type=1</query><fields>id; name; surname</fields></request>"
        self.assertEqual(to_sql(zahtev3) , "Neadekvatan xml zahtev")
        zahtev3=""
        self.assertEqual(to_sql(zahtev3) , "Neadekvatan xml zahtev")

    def test_delete(self):
        zahtev4="<request><verb>DELETE</verb><noun>/resurs/1</noun><query>name='pera';type=1</query></request>"
        self.assertEqual(to_sql(zahtev4) , "DELETE FROM /resurs/1 WHERE name='pera' AND type=1")
        zahtev4="<request><verb>cao</verb><noun>/resurs/1</noun><query>name='pera';type=1</query><fields>id; name; surname</fields></request>"
        self.assertEqual(to_sql(zahtev4) , "Neadekvatan xml zahtev")
        zahtev4=""
        self.assertEqual(to_sql(zahtev4) , "Neadekvatan xml zahtev")
        zahtev4="<request><verb>DEKETE</verb><noun>/resurs/1</noun></request>"
        self.assertEqual(to_sql(zahtev4) , "Neadekvatan xml zahtev")
        zahtev4="<request><verb>DELETE</verb><noun>/resurs/1</noun><fields>id; name; surname</fields></request>"
        self.assertEqual(to_sql(zahtev4) , "Neadekvatan xml zahtev")


    def test_post(self):
        zahtev5="<request><verb>POST</verb><noun>/resurs/1</noun><query>name='pera';type=1</query><fields>id; name; surname</fields></request>"
        self.assertEqual(to_sql(zahtev5) , "INSERT INTO /resurs/1(name, type) VALUES ('pera', 1)")
        zahtev5="<request><verb>cao</verb><noun>/resurs/1</noun><query>name='pera';type=1</query><fields>id; name; surname</fields></request>"
        self.assertEqual(to_sql(zahtev5) , "Neadekvatan xml zahtev")
        zahtev5=""
        self.assertEqual(to_sql(zahtev5) , "Neadekvatan xml zahtev")
        zahtev5="<request><verb>POST</verb><noun>/resurs/1</noun><fields>id; name; surname</fields></request>"
        self.assertEqual(to_sql(zahtev5) , "Neadekvatan xml zahtev")
        zahtev5="<request><verb>POST</verb><noun>/resurs/1</noun><query>name='pera';type=1</query></request>"
        self.assertEqual(to_sql(zahtev5) , "Neadekvatan xml zahtev")
        zahtev5="<request><verb>POST</verb><noun>/resurs/1</noun></request>"
        self.assertEqual(to_sql(zahtev5) , "Neadekvatan xml zahtev")
    
    def test_patch(self):
        zahtev6="<request><verb>PATCH</verb><noun>/resurs/1</noun><query>name='pera';type=1</query><fields>id; name; surname</fields></request>"
        self.assertEqual(to_sql(zahtev6) , "UPDATE /resurs/1 SET id, name, surname WHERE name='pera' AND type=1")
        zahtev6="<request><verb>CAO</verb><noun>/resurs/1</noun><query>name='pera';type=1</query><fields>id; name; surname</fields></request>"
        self.assertEqual(to_sql(zahtev6) , "Neadekvatan xml zahtev")
        zahtev6=""
        self.assertEqual(to_sql(zahtev6) , "Neadekvatan xml zahtev")
        zahtev6="<request><verb>PATCH</verb><noun>/resurs/1</noun><fields>id; name; surname</fields></request>"
        self.assertEqual(to_sql(zahtev6) , "Neadekvatan xml zahtev")
        zahtev6="<request><verb>PATCH</verb><noun>/resurs/1</noun><query>name='pera';type=1</query></request>"
        self.assertEqual(to_sql(zahtev6) , "Neadekvatan xml zahtev")
        zahtev6="<request><verb>PATCH</verb><noun>/resurs/1</noun></request>"
        self.assertEqual(to_sql(zahtev6) , "Neadekvatan xml zahtev")


if __name__ == '__main__':
    unittest.main()