from asyncio.windows_events import NULL
import xml.etree.ElementTree as ET
from Komponente.repozitorijum import connection
import mysql.connector

#ovde treba da imam vezu sa bazom i jedan fajl u kom cu
#privremeno da cuvam xml parsiran iz JSON-a

def ToSql(data):
    tree = ET.parse(data)   #parsira direkt iz prethodnog adaptera
    data2 = tree.findall('request')

    sqlZahtev = ""

    for i, j in zip(data2, range(1, 4)):
        verb = i.find('verb').text
        noun = i.find('noun').text
        
        if(i.find('query') != NULL):
            query = i.find('query').text
        else:
            query = ""

        if(i.find('fields') != NULL):
            fields = i.find('fields').text
        else:
            fields = ""

        
        if(verb == 'GET'):
            sqlZahtev = "select " + fields + " from " + noun + " where " + query;

        if(verb == 'POST'):
            sqlZahtev = "insert into " + noun + " ( " + fields + " ) VALUES ( " + query + " )";
            
        if(verb == 'DELETE'):
            sqlZahtev = "delete from " + noun + " where " + query;

        if(verb == 'PATCH'):
            sqlZahtev = "update " + noun + " set " + query;

    return sqlZahtev

def BackToXml(sqlZahtev):
    
    #preuzmi odgovor iz baze (kog je formata?) i dobavi vrednosti ovih polja:
    #koneektuje se na repo, posalje sqlZahtev koji je prosledjen i preuzme odgovor koji se dalje parsira

    status = ""
    status_code = ""
    payload = ""
    xmlOdgovor = "<response><status>" + status + "</status> <status_code>" + status_code + "</status_code> <payload>"+payload+"</payload></response>";

    return xmlOdgovor


