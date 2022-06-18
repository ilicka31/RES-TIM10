import unittest
import sys
sys.path.append("..")
from Komponente.formatiranje import format


class testformat(unittest.TestCase):
    def test_good1(self):
        primer = {
            "verb": "GET",
            "noun": "student",
            "query": "ime='Jelena';prezime='Ilic'", 
            "fields": "brindeksa; ime; prezime" 
            }
        self.assertTrue(format(primer))
    def test_good2(self):
        primer = {
            "verb": "GET",
            "noun": "profesor",
            "query": "ime='Imre'",
            "fields": "ime; prezime; predmet"
            }
        self.assertTrue(format(primer))
    def test_good3(self):
        primer = {
            "verb": "GET",
            "noun": "fakultet",
            "query": "naziv='FTN'",
            "fields": "naziv; brojstudenata"
            }
        self.assertTrue(format(primer))
    def test_good4(self):
        primer = {
            "verb": "POST",
            "noun": "student",
            "query": "idstudent=6; ime='Zdravko'; prezime='Milinkovic'; brindeksa='PR36/2019'",
            "fields": ""
            }
        self.assertTrue(format(primer))
    def test_good5(self):
        primer = {
            "verb": "POST",
            "noun": "profesor",
            "query": "idprofesor=6; ime='Janko'; prezime='Radovanovic'; predmet='Matematika'",
            "fields": ""
            }
        self.assertTrue(format(primer))
    def test_good6(self):
        primer = {
            "verb": "POST",
            "noun": "fakultet",
            "query": "idfakultet=6; naziv='PF'; brojstudenata=5000; grad='Novi Sad'",
            "fields": ""
            }
        self.assertTrue(format(primer))
    def test_good7(self):
        primer = {
            "verb": "PATCH",
            "noun": "student",
            "query": "ime='Lana'; prezime='Slovic'",
            "fields": "brindeksa='PR1/2022'"
            }
        self.assertTrue(format(primer))
    def test_good8(self):
        primer = {
            "verb": "PATCH",
            "noun": "profesor",
            "query": "ime='Milana'; prezime='Bojanic'",
            "fields": "predmet='RVA'"
            }
        self.assertTrue(format(primer))
    def test_good9(self):
        primer = {
            "verb": "PATCH",
            "noun": "fakultet",
            "query": "naziv='FTN'; grad='Novi Sad'",
            "fields": "brojstudenata=17000"
            }
        self.assertTrue(format(primer))
    def test_good10(self):
        primer = {
            "verb": "DELETE",
            "noun": "student",
            "query": "ime='Zdravko'",
            "fields": ''
            }
        self.assertTrue(format(primer))
    def test_good11(self):
        primer = {
            "verb": "DELETE",
            "noun": "profesor",
            "query": "ime='Janko'",
            "fields": ""
            }
        self.assertTrue(format(primer))
    def test_good12(self):
        primer = {
            "verb": "DELETE",
            "noun": "fakultet",
            "query": "naziv='PF'",
            "fields": ""
            }
        self.assertTrue(format(primer))
    ##LOSI
    def test_wrong1(self):
        primer = {
            "verb": "",
            "noun": "student",
            "query": "ime='Jelena';prezime='Ilic'", 
            "fields": "brindeksa; ime; prezime" 
            }
        self.assertFalse(format(primer), "Verb missing")
    def test_wrong2(self):
        primer = {
            "verb": "PRINT",
            "noun": "student",
            "query": "ime='Jelena';prezime='Ilic'", 
            "fields": "brindeksa; ime; prezime" 
            }
        self.assertFalse(format(primer), "Verb is wrong")
    def test_wrong3(self):
        primer = {
            "verb": "GET",
            "noun": "",
            "query": "ime='Jelena';prezime='Ilic'", 
            "fields": "brindeksa; ime; prezime" 
            }
        self.assertFalse(format(primer), "Noun missing")
    def test_wrong4(self):
        primer = {
            "verb": "GET",
            "noun": "greska",
            "query": "ime='Jelena';prezime='Ilic'", 
            "fields": "brindeksa; ime; prezime" 
            }
        self.assertFalse(format(primer), "Noun is wrong")

if __name__ == "__main__":
    unittest.main()