# Jordan Darling made this 4/16/17 
# Using json to search for various parts of a json file
import json
import Rad

def category(temp):
    jsonLoad = temp
    user = Rad.userString("Enter a category:")
    for i in jsonLoad:
        if i['Category'].lower() == user.lower():
            print "%s - $%s" %(i['Product'], i['Price'])

def keyword(temp):
    jsonLoad = temp
    user = Rad.userString("Enter a Keyword:")
    for i in jsonLoad:
        if user.lower() in i['Product'].lower():
            print "%s - $%s" %(i['Product'], i['Price'])

def main():
    jsonTxt = ""
    f = open('PetStore.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    jsonLoad = json.loads(jsonTxt)
    
    search = Rad.userString("Search by category (c) or keyword (k):")
    if search == "c":
        category(jsonLoad)
  
    if search == "k":
        keyword(jsonLoad)

main()