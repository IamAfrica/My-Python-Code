import Rad
import random

def main():
    # initializes prizes...
    goodPrizes = ["New Car!", "$1000", "Sandwich!"]
    badPrizes = ["Dead Goat!", "Smelly Piece of Cheese!", "Piece of Paper!"]
    
    # Creates door list...
    doors = ["","",""]
    
    # Place random bad prizes behind all three doors...
    random.shuffle(badPrizes)
    doors[0] = badPrizes[0]
    doors[1] = badPrizes[1]
    doors[2] = badPrizes[2]
    
    # Replace a random bad prize with a good one...
    random.shuffle(goodPrizes)
    igoodPrize = random.randrange(0,3)
    doors[igoodPrize] = goodPrizes[0]
    
    # Picks a door
    door = Rad.userInt("Pick a door, any door!: ")
    print "You win..." 
    time.sleep(5)
    print "...a %s" % doors[door -1]
    
main()