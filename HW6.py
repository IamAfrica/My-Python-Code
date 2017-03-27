#Jordan Darling made this 3/26/17
#Using splits and for loops to create a deck shuffler
import Rad

def buildDeck(rank, suit):
    deck = []
    for n in rank:
        for x in suit:
            temp = n + " of " + x
            deck.append(temp)

    return deck
    
def shuffle(deck):
    shuffledDeck = []
    cut1 = deck[0:26]
    cut2 = deck[26:53]
    
    for x in range(0,26):
        shuffledDeck.append(cut1[x])
        shuffledDeck.append(cut2[x])
        
    return shuffledDeck
    
def deal(deck):
    count = Rad.userInt("How many times do you want to shuffle the deck?: ")
    temp = 0
    
    while temp != count:
        deck = shuffle(deck)
        temp = temp + 1
    
    for x in range(0, 5):
        print deck[x]
    
def main():
    rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
    
    deck = buildDeck(rank, suit)
    
    shuffledDeck = shuffle(deck)
    deal(deck)
    
main()