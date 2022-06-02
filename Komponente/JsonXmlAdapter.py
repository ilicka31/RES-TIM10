import xmltodict
import json

def ToXml(z,p):
   if(p==0):
      z = {'root':z}
   ret = xmltodict.unparse(z)
 # ret= ret.replace("<root>","")
  # ret= ret.replace("</root>","")
   return ret


def ToJson(x):
   dict = xmltodict.parse(x)
   ret = json.loads(json.dumps(dict))
   return ret




