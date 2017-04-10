import json
import Rad
def main():
    jsonTxt = ""
    f = open('contacts.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    contacts = json.loads(jsonTxt)
    
    name = Rad.userString("Enter a name:")
    for contact in contacts:
        if contact["Name"] == name:
            print "%s" % contact["Phone"]
            for email in contact['Email']:
                print email
            
main()