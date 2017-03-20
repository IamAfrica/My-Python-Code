import Rad
import random



def cards(choices):
    attempts = 1
    keepGoing = True
    while keepGoing:
        first = Rad.userInt("Pick the first card to turn over (0-9):")
        second = Rad.userInt("Pick the second card to turn over (0-9):")
        if first < 0 or second < 0 or first > 9 or second > 9 or first == second:
            print "ERROR! You must pick different cards and the card numbers must be between 0 and 9"
        else: 
            print "Card {} is a {}".format(first, choices[first])
            print "Card {} is a {}".format(second, choices[second])
            
            if choices[first] == choices[second]:
                print "You win! It took you %s tries!" % attempts
                keepGoing = False
            else:
                attempts += 1

def rando(choices):
    duplicate = choices[random.randrange(0, 9)]
    
    tempArray = ["","","","","","","","","","",]
    for i in range(0, 9):
        tempArray[i] = choices[i]
    tempArray[9] = duplicate
    
    random.shuffle(tempArray)
    choices = tempArray
    
    return choices
    
def main():
    choices = ['bird', 'dog', 'snake', 'fish', 'cat', 'mouse', 'starfish', 'woodchuck', 'crab']
    tempchoices = rando(choices)
    cards(tempchoices)
    
main()