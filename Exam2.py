#Jordan Darling made this on 2/26/17
#Using loops, statements, dictionaries to sort names into categories
import Rad

def readData(filename):
    stuff = {"Cube Head" : "", "Square Master" : "", "Advanced Twister" : "", "Intermediate Turner" : "", "Average Mover" : "", "Pathetic" : ""}
    
    for line in open("Examtxt.txt"):
        temp = line.split(',')
        name = temp[0].strip()
        time = temp[1].strip()
        
        if float(time) < 10.0:
            stuff["Cube Head"] + name
            print "Cube Head (0-9.99):\n      %s" %name
        elif float(time) < 20:
            print "Square Master (10-19.99):\n      %s" %name
            stuff["Square Master"] + name
        elif float(time) < 30:
            print "Advanced Twister (20-29.99):\n      %s" %name
            stuff["Advanced Twister"] + name
        elif float(time) < 40:
            print "Intermediate Turner (30-39.99):\n      %s" %name
            stuff["Intermediate Turner"] + name
        elif float(time) < 60:
            print "Average Mover (40-59.99):\n      %s" %name
            stuff["Average Mover"] + name
        elif float(time) >= 60:
            print "Pathetic (60-beyond):\n      %s" %name
            stuff["Pathetic"] + name

    return stuff

def printResults(dic):
    for x in dic:
        print (dic[x])
    
def main():
    dictionary = readData("Examtxt.txt")
    printResults(dictionary)
    
main()