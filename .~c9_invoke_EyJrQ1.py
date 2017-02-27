#Jordan Darling made this on 2/26/17
#
import Rad

def readData(filename):
    d = {}
    l = []
    for line in open("Examtxt.txt"):
        lst = line.split(',')
        name = lst[0].strip()
        time = lst[1].strip()
        if time in d:
            d[time].append(name)
        else:
            d[time] = [name]
            
    return l

def sort(d):
    d={}
    
    r1 = range(0, 10)
    r2 = range(10, 20)
    r3 = range(20, 30)
    r4 = range(30, 40)
    r5 = range(40, 60)
    r6 = range(60, 64)
    
    listreadData("Examtxt.txt")
    
    
def main():
    listDic = readData("Examtxt.txt")
    dictionary = sort(listDick)
    
    print "Cube Head (0-9.99):\n %s " %()
    print "Square Master (10-19.99):\n %s" %()
    print "Advanced Twister (20-29.99):\n %s" %()
    print "Intermediate Turner (30-39.99):\n %s" %()
    print "Average Mover (40-59.99):\n %s" %()
    print "Pathetic (60-beyond):\n %s" %()
    
main()