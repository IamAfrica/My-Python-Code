# Jordan Darling made this on 4/9/17, uses basic json principles
# Professor names: Kebra Ward, Christopher Thomas, Jeff Parkman, Emily Maher, Louis Stelling, Mark Cohen
import json
import Rad

# Reads the json file 
def read():
    jsonTxt = ""
    f = open('Prof.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    return 

# Assigns the user input to a value and matches that value with one from the json file
def assign():
    jsonTxt = ""
    words = json.loads(jsonTxt)
    name = Rad.userString("Enter a professor's name that I have this current semester:")
    for word in words:
        if word["Name"] == name:
            print "Class: %s - Days: %s - Time: %s - Grade: %s" % (word["Class"], word['Days'], word['Time'], word['Grade'])
    return

def main():
    read()
    assign()

main()