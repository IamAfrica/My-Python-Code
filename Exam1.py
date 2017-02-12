#Jordan Darling made this on 2/12/17
def readData(filename):
    file = open(filename)
    l = []
    for num in file:
        l.append(num.strip())
    return l
    
def getAverage(l):
    data = []
    with open('Rush.txt') as l:
        for line in l:
            fields = line.split()
            rowdata = map(float, fields)
            data.extend(rowdata)
            average = (sum(data)/len(data))
    return average

def getAverage2(t):
    data = []
    with open('NoRush.txt') as t:
        for line in t:
            fields = line.split()
            rowdata = map(float, fields)
            data.extend(rowdata)
            average = (sum(data)/len(data))
    return average


def countSpeeders(l, maxSpeed):
    l = 0
    maxSpeed = 70
    
    if(l > maxSpeed):
        l += 1
    
    return l

def countSpeeders2(t, maxSpeed):
    t = 0
    maxSpeed = 70
    
    while(t >= maxSpeed):
        if(t[maxSpeed] > 0):
            t += 1
        t += 1
    
    return t


def main():
    l = readData("Rush.txt")
    t = readData("NoRush.txt")
    maxSpeed = 70
    crusade = getAverage(l)
    deusvult = getAverage2(t)
    rushing = countSpeeders(l, maxSpeed)
    norushhour = countSpeeders2(t, maxSpeed)
    print "The number of people people speeding during rush hour is %s" % rushing 
    print "The number of people speeding not during rush hour is %s" % norushhour
    print "The average speed during rush hour was %.2f" % crusade
    print "The average speed not during rush hour was %.2f" % deusvult

main()