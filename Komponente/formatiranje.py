import json

def format():
    #Opening JSON file
    f = open('Zahtevi.py')
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    verb = False
    noun = False
    for i in data:
        if(data["verb"] == "GET" or data["verb"] == "POST" or data["verb"] == "PATCH" or data["verb"] == "DELETE"):
            verb = True;

        if(data["noun"] != ""):
            noun = True;

        if(noun == True and verb == True):
            return True
    # Closing file
    f.close()