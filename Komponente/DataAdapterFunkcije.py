def to_sql(data):
    sql_zahtev = ""
    verb = ""
    noun = ""
    fields = ""
    query = ""

    xml_req = data[10 : -10]
    l = len(xml_req)
    glagol = xml_req[5 : l]

    for i in range(0, l):
        if(glagol[i] == '<'):
            verb = glagol[0:i]
            glagol = glagol[i : l]
            break
        
    glagol = glagol[13 : l]
    for i in range(0, l):
        if(glagol[i] == '<'):
            noun = glagol[0:i]
            glagol = glagol[i : l]
            break

    glagol = glagol[7 : l]
    l1 = len(glagol)

    if(l1 != 0):
        if("query" in glagol):
            glagol = glagol[7 : l1]
            for i in range(0, l1):
                if(glagol[i] == '<'):
                    query = glagol[0:i]
                    glagol = glagol[i : l1]
                    break
            glagol = glagol[8 : l1]
            l2 = len(glagol)
            if(l2 != 0):
                glagol = glagol[8 : l2]
                for i in range(0, l2):
                    if(glagol[i] == '<'):
                        fields = glagol[0:i]
                        glagol = glagol[i : l2]
                        break
        else:
            if("fields" in glagol):
                l3 = len(glagol)
                glagol = glagol[8 : l3]
                for i in range(0, l3):
                    if(glagol[i] == '<'):
                        fields = glagol[0:i]
                        glagol = glagol[i : l3]
                        break
    polja = ""
    vrednosti = ""
    polja_l = []
    vrednosti_l = []
    if(query != ""):
        jednako = 0
        zarez = 0
        l = len(query)
        for i in range(0, l+1):
            if(query[i] == '='):
                if(zarez==0):
                    polja = polja + query[zarez:i]
                else:
                    polja = polja + ", " + query[zarez+1:i]
                jednako = i
                polja_l.append(query[zarez:i])
            if(query[i] == ';'):
                if(vrednosti == ""):
                     vrednosti = vrednosti + query[jednako+1 : i]
                else:
                    vrednosti = vrednosti + ", " + query[jednako+1 : i]
                vrednosti_l.append(query[jednako+1 : i])
                zarez = i
            if(i == l-1):
                if(vrednosti == ""):
                     vrednosti = vrednosti + query[jednako+1 : i]
                else:
                    vrednosti = vrednosti + ", " + query[jednako+1 : i+1]
                vrednosti_l.append(query[jednako+1 : i])
                break
        
    

    if(fields != ""):
        fields = fields.replace(';', ',')
    else:
        fields = "*"
    if(verb == 'GET'):
        if(query != ""):
            sql_zahtev = "SELECT " + fields + " FROM " + noun + " WHERE " + query.replace(";", " AND ")
        else:
            sql_zahtev = "SELECT" + fields + "FROM " + noun
    elif(verb == 'POST'):
        sql_zahtev = "INSERT INTO " + noun + "(" + polja + ")" + " VALUES (" + vrednosti + ")" #treba da se dovrsi
    elif(verb == 'PATCH'):
      
        sql_zahtev = 'UPDATE ' + noun + ' SET ' + fields.replace(";", ", ") + ' WHERE ' + query.replace(";"," AND ")  
    elif(verb == 'DELETE'):
        if(query != ""):
            sql_zahtev = 'DELETE FROM ' + noun + " WHERE " + query.replace(";", " AND ")
        else:
            sql_zahtev = "DELETE FROM " + noun
    else:
        sql_zahtev='Neadekvatan xml zahtev'


    return sql_zahtev

def back_to_xml(poruka):
    
    poruka = poruka.decode()
    status = ""
    status_code = ""
    payload = ""
    if("rows affected" in poruka):
        status = 'SUCCESS'
        status_code = '2000'
        payload = poruka
    elif("an error in your SQL syntax" in poruka or "doesn't have a default value" in poruka):
        status = 'BAD_FORMAT'
        status_code = '5000'
        payload = poruka
    elif("Error while connecting to MySQL" in poruka or "Error Code: 1062" in poruka or "Error Code: 1175" in poruka):
        status = 'REJECTED'
        status_code = '3000'
        payload = poruka

    xml_odgovor = "<response><status>" + status + "</status> <status_code>" + status_code + "</status_code> <payload>"+payload+"</payload></response>"
    return xml_odgovor


