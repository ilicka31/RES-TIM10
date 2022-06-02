def format(data):
    print(data)
    verb = False
    noun = False
    if(data[0] == "GET" or data[0]  == "POST" or data[0]  == "PATCH" or data[0]  == "DELETE"):
        verb = True
    if(data[1] != ""):
        noun = True

    if(noun == True and verb == True):
        return True
    else:
        return False
