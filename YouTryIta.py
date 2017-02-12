import Rad

def getFlavors():
    l = []
    l.append(Rad.userString("Enter flavor one:"))
    l.append(Rad.userString("Enter flavor two:"))
    l.append(Rad.userString("Enter flavor three:"))
    l.append(Rad.userString("Enter flavor four:"))
    l.append(Rad.userString("Enter flavor five:"))
    return l
    
def countInStock(flavors):
    count = 0
    for f in flavors:
        if f.upper() == "VANILLA" or f.upper() == "CHOCOLATE" or f.upper() == "STRAWBERRY":
            count = count + 1
    return count
        
def main():
    flavs = getFlavors()
    c = countInStock(flavs)
    print "We have %s of your flavors." %c
main()