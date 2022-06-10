import unittest
import sys


sys.path.append('..')

from Komponente.XmlDataBaseAdapter import ToSql


zahtev1="<request><verb>GET</verb><noun>/resurs/1</noun><query>name='pera';type=1</query><fields>id; name; surname</fields></request>"

zahtev2="<request><verb>GET</verb><noun>/resurs/1</noun><query>name='pera';type=1</query></request>"
zahtev3="<request><verb>GET</verb><noun>/resurs/1</noun></request>"
zahtev4="<request><verb>DELETE</verb><noun>/resurs/1</noun><query>name='pera';type=1</query></request>"
zahtev5="<request><verb>POST</verb><noun>/resurs/1</noun><query>name='pera';type=1</query><fields>id; name; surname</fields></request>"
zahtev6="<request><verb>PATCH</verb><noun>/resurs/1</noun><query>name='pera';type=1</query><fields>id; name; surname</fields></request>"



class TestXmlDataBaseAdapter(unittest.TestCase):
    def test_ToSql(self):
        self.assertEquals(ToSql(zahtev1) , "SELECT id, name, surname FROM /resurs/1 WHERE name='pera' AND type=1")
        self.assertEquals(ToSql(zahtev2) , "SELECT * FROM /resurs/1 WHERE name='pera' AND type=1")
        #umesto print("nema polja fields") ubaciti neki exception zbog testiranja
        #182, 184, 178, 174 su zakomentarisane linije u XmlDataBaseAdapteru da bi se moglo testirati
        self.assertEquals(ToSql(zahtev3) , "SELECT*FROM /resurs/1")
        #umesto printa da nema poja query i fields ubaaciti exception zbog testiranja
        #razdvojiti select * from
        self.assertEquals(ToSql(zahtev4) , "DELETE FROM /resurs/1 WHERE name='pera' AND type=1")
        self.assertEquals(ToSql(zahtev5) , "INSERT INTO /resurs/1(name, type) VALUES ('pera', 1)")
        #ubaciti spejs-------------------------------------------^ ovde
        self.assertEquals(ToSql(zahtev6) , "UPDATE /resurs/1 SET name='pera',type=1 WHERE ")#nedovrseno
        #ubaciti umesto posljednjeg elsa gde pise da je neispravan zahtev exception

if __name__ == '__main__':
    unittest.main()