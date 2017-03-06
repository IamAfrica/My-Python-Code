# Jordan Darling made this 3/5/17
# Uses While loops, time, and random to make a hot-dog eating contest

import Rad
import random
import time


def countDogs():
    name = Rad.userString("Pick a winner (Tom, Sally, or Fred):")
    print "Ready, Set, Eat! \n"
    TomDogs = 0
    SallyDogs = 0
    FredDogs = 0
    keepGoing = True
    winner = ""
    while keepGoing:
        print "Chomp...Chomp...Chomp... \n"
        dogs = chompDogs()
        TomDogs = TomDogs + dogs
        print "Tom has eaten %s dogs" % TomDogs 
        dogs = chompDogs()
        SallyDogs = SallyDogs + dogs
        print "Sally has eaten %s dogs" % SallyDogs
        dogs = chompDogs()
        FredDogs = FredDogs + dogs
        print "Fred has eaten %s dogs\n" % FredDogs
        time.sleep(2)
        if TomDogs >= 50 or SallyDogs >= 50 or FredDogs >= 50:
            if TomDogs >= 50:
                winner = "Tom"
            if SallyDogs >= 50:
                winner = "Sally"
            if FredDogs >= 50:
                winner = "Fred"
                
            keepGoing = False
            
    print "%s is the winner!" % winner
    if winner == name:
        print "You guessed right!" 
    
def chompDogs():
    dogs = random.randrange(1,7) + 20
    return dogs

def main():
    countDogs()
    chompDogs()
    
main()