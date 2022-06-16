from mockdb import MockDB
import unittest
import sys
sys.path.insert(0, "../..")
from Komponente.repoFunkcije import izvrsiupit


class TestBaza(MockDB):
    def test_succsess(self):
        with self.mock_db_config:
            self.assertEqual(izvrsiupit("""SELECT `idstudent`, `ime`, `prezime`, `brojindeksa` FROM `student` WHERE idstudent = '1' """), """Total number of rows affected: 1 1. {'6', 'Marko', 'Markovic','RA22/2017'}""")
#           # self.assertEqual(utils.db_write("""DELETE FROM `test_table` WHERE id='1' """), True)
#           # self.assertEqual(utils.db_write("""DELETE FROM `test_table` WHERE id='4' """), True)
#
if __name__ == '__main__':
    unittest.main()