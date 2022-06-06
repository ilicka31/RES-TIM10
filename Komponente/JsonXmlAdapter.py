from dicttoxml import dicttoxml
import xmltodict 
from json import *

def ToXmlFromJson(zahtev):
   obj = dumps(zahtev)
   z = dicttoxml(loads(obj), attr_type=False)
   return z

def ToJsonFromXml(zahtevXml):
   obj = xmltodict.parse(zahtevXml)
   j =dumps(obj)
   j= j.replace('{"root":','')
   j= j[:len(j)-1]
   return j