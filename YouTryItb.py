import Rad

def readFlavors(flav):
    file = open('flav.txt', 'r')
    final = []
    for flavor in file:
        final.append(flavor.strip())
    return final

def countInStock(instock, flavors):
    count = 0
    for f in flavors:
        if (f.upper() in instock):
            count = count + 1
    return count
    
def main():
    instock = ["VANILLA", "CHOCOLATE", "STRAWBERRY"]
    flavs = readFlavors("flav.txt")
    c = countInStock(instock, flavs)
    print "We have %s of your flavors: " %c
main()