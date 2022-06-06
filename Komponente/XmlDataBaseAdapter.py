import xml.etree.ElementTree as ET
from Komponente.repozitorijum import connection
import mysql.connector

#ovde treba da imam vezu sa bazom i jedan fajl u kom cu
#privremeno da cuvam xml parsiran iz JSON-a

def ToSql():
    tree = ET.parse('Temp.xml')
    data2 = tree.findall('request')

    sqlZahtev = ""

    for i, j in zip(data2, range(1, 4)):
        verb = i.find('verb').text
        noun = i.find('noun').text
        query = i.find('query').text
        fields = i.find('fields').text

        
        if(verb == 'GET'):
            sqlZahtev = "select " + fields + " from " + noun + " where " + query;

        if(verb == 'POST'):
            sqlZahtev = "insert into " + noun + " ( " + fields + " ) VALUES ( " + query + " )";
            
        if(verb == 'DELETE'):
            sqlZahtev = "delete from " + noun + " where " + query;

        if(verb == 'PATCH'):
            sqlZahtev = "update " + noun + " set " + query;

    return sqlZahtev

def PosaljiZahtev(sqlZahtev):
    odgovor = ""

    #salje sql na repozitorijum i preuzima odgovor iz repozitorijuma
    return odgovor

def BackToXml(sqlOdgovor):
    
    #preuzmi odgovor iz baze (kog je formata?) i dobavi vrednosti ovih polja:

    status = ""
    status_code = ""
    payload = ""
    xmlOdgovor = "<status>" + status + "</status> <status_code>" + status_code + "</status_code> <payload>"+payload+"</payload>";

    return xmlOdgovor


def XmlAdapter():

    sqlRequest = ToSql()

    #konekcija sa repo u metodi posalji zahtev
    odgovor = PosaljiZahtev(sqlRequest)

    xmlOdgovor = BackToXml(odgovor)

    return xmlOdgovor