import unittest
import json
import xmltodict
import sys
sys.path.append("..")
from Komponente.formatiranje import *

class TestFormat(unittest.TestCase):
    def test_good_post(self):
        zahtev = {
            "verb": "POST",
            "noun": "/resurs/1",
            "query": "name='zeka'; type=1",
            "fields": "id; name; surname"
            }
        self.assertTrue(format(zahtev))
    def test_bad_post(self):
        zahtev = {
            "verb": "POST",
            "noun": "",
            "query": "name='zeka'; type=1",
            "fields": "id; name; surname"
            }
        self.assertFalse(format(zahtev), "Noun is missing")



if __name__ == "__main__":
    unittest.main()