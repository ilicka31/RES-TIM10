import unittest
from Komponente.formatiranje import format
import json

zahtev = {
"verb": "CAO",
"noun": "/resurs/1",
"query": "name='pera'; type=1",
"fields": "id; name; surname"
}
zahtev1 = {
"verb": "GET",
"noun": "",
"query": "name='jova'; type=1",
"fields": "id; name; surname"
}
zahtev2 = {
"verb": "POST",
"noun": "/resurs/1",
"query": "name='zeka'; type=1",
"fields": "id; name; surname"
}

zahtev3 = {
"verb": "PATCH",
"noun": "/resurs/1",
"query": "name='seka'; type=1",
"fields": "id; name; surname"
}

def test_format(self):
    self.assertFalse(zahtev, "Verb is not valid")
    self.assertFalse(zahtev1, "Noun is missing")
    self.assertTrue(zahtev2)
    self.assertTrue(zahtev3)
