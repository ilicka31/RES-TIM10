from mockdb import MockDB, configuration
from mock import patch
import sys
sys.path.insert(0, "../..")
from Komponente.repoFunkcije import izvrsiupit, konektuj_se

conn, cur = konektuj_se(configuration)
class TestBaza(MockDB):
    def test_izvrsiupit(self):
        with self.mock_db_config:
            self.assertEqual(izvrsiupit("""SELECT `idstudent`, `ime`, `prezime`, `brojindeksa` FROM `test_table` WHERE
                            idstudent = '1' """, conn), """Total number of rows affected: 1 1. {'6', 'Marko', 'Markovic','RA22/2017'}""")
#           # self.assertEqual(utils.db_write("""DELETE FROM `test_table` WHERE id='1' """), True)
#           # self.assertEqual(utils.db_write("""DELETE FROM `test_table` WHERE id='4' """), True)
#
