#Jordan Darling made this on 2/19/17
#Using dictionaries to count birds
import Rad

def countBirds(dictionary):
    for line in open("Birds.txt"):
        temp = line.split(',')
        name = temp[0].strip()
        number = temp[1].strip()
        dictionary[name] = int(dictionary[name]) + int(number)

def askUser(dictionary):
    birdName = Rad.userString("Enter a bird name:")
    if birdName in dictionary:
        print "I have seen that bird %s time(s)" % dictionary[birdName] + "."
    else:
        print "I have seen that bird 0 time(s)."
    
def main():
    d = {"Cardinal" : '0', "House Sparrow" : '0', "House Wren" : '0', "Robin" : '0', "House Finch" : '0', "Starling" : '0', "Downy Woodpecker" : '0', "American Crow" : '0', "Blue Jay" : '0', "Song Sparrow" : '0'}
    countBirds(d)
    askUser(d)
    
main()