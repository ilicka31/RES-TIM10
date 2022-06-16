from dicttoxml import dicttoxml
import xmltodict 
from json import dumps, loads

zahtev1 = {
"verb": "GET",
"noun": "student",
"query": "ime='Jelena';prezime='Ilic'", 
"fields": "brindeksa; ime; prezime" 
}

def to_xml_from_json(zahtev):
   obj = dumps(zahtev)
   z = dicttoxml(loads(obj), attr_type=False)
   return z

def to_json_from_xml(zahtev_xml):
   obj = xmltodict.parse(zahtev_xml)
   j =dumps(obj)
   j= j.replace('{"root":','')
   j= j[:len(j)-1]
   return j
