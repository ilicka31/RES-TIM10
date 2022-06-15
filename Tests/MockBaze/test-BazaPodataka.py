from mockdb import MockDB, configuration
from mock import patch
import sys
sys.path.insert(0, "../..")
from Komponente.repozitorijum import izvrsiupit, konektuj_se

conn, cur = konektuj_se(configuration)
cur.execute("select database();")
record = cur.fetchone()
print("You're connected to database: ", record)
print()
class TestBaza(MockDB):
    def test_izvrsiupit(self):
        with self.mockdb_config:
            self.assertEqual(izvrsiupit("""SELECT `id`, `ime`, `prezime`, `brojindeksa` FROM `test_table` WHERE
                            id = '1' """, conn), """Total number of rows affected: 1 1. {'6', 'Marko', 'Markovic','RA22/2017'}""")
#           # self.assertEqual(utils.db_write("""DELETE FROM `test_table` WHERE id='1' """), True)
#           # self.assertEqual(utils.db_write("""DELETE FROM `test_table` WHERE id='4' """), True)
#
