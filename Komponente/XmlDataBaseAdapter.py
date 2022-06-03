import xml.etree.ElementTree as ET
from Komponente.repozitorijum import *
#import mysql.connector

#ovde treba da imam vezu sa bazom i jedan fajl u kom cu
#privremeno da cuvam xml parsiran iz JSON-a

def ToSql(tableName):
    tree = ET.parse('Temp.xml')
    data2 = tree.findall('request')

    sqlZahtev = ""

    for i, j in zip(data2, range(1, 4)):
        verb = i.find('verb').text
        noun = i.find('noun').text
        query = i.find('query').text
        fields = i.find('fields').text

        if(noun == tableName):
            if(verb == 'GET'):
                sqlZahtev = "select " + fields + " from " + noun + " where " + query;

            if(verb == 'POST'):
                sqlZahtev = "insert into " + tableName + " ( " + fields + " ) VALUES ( " + query + " )";
            
            if(verb == 'DELETE'):
                sqlZahtev = "delete from " + tableName + " where " + query;

            if(verb == 'PATCH'):
                sqlZahtev = "update " + tableName + " set " + query;

        return sqlZahtev

def BackToXml(sqlOdgovor):
    
    #preuzmi odgovor iz baze (kog je formata?) i dobavi vrednosti ovih polja:

    status = ""
    status_code = ""
    payload = ""
    xmlOdgovor = "<status>" + status + "</status> <status_code>" + status_code + "</status_code> <payload>"+payload+"</payload>";

    return xmlOdgovor
