def format(data):
    verb = False
    noun = False
    if(data['verb'] == "GET" or data['verb']  == "POST" or data['verb']  == "PATCH" or data['verb']  == "DELETE"):
        verb = True
    if(data['noun'] == "student" or data['noun'] == "fakultet" or data['noun'] == "profesor"):
        noun = True

    if(noun == True and verb == True):
        return True
    else:
        return False
